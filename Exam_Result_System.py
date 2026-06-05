import numpy as np

# ─────────────────────────────────────────────
#  EXAM RESULT SYSTEM
#  30 students, 5 subjects
#  - Subject-wise averages
#  - Top 3 students using argsort
#  - Grades using np.where
#  - Save results to file
# ─────────────────────────────────────────────


# ── STEP 1: Create marks for 30 students in 5 subjects ───────────────────────
# np.random.seed(0) means same random numbers every time you run
# (so your results don't change each run)
np.random.seed(0)

# Shape (30, 5) means: 30 rows (students) × 5 columns (subjects)
# randint(40, 101) gives marks between 40 and 100
marks = np.random.randint(40, 101, size=(30, 5))

subjects = ["Math", "Physics", "Chemistry", "English", "Computer"]

student_names = [f"Student_{i+1:02d}" for i in range(30)]
# f"Student_{i+1:02d}" just means Student_01, Student_02 ... Student_30
# :02d = always show 2 digits (so 1 becomes 01)


# ── STEP 2: Total and average marks per student ───────────────────────────────
# axis=1 means "add across columns" (i.e. add all 5 subject marks for each student)
total_marks = np.sum(marks, axis=1)       # shape: (30,)
avg_marks   = np.mean(marks, axis=1)      # shape: (30,)


# ── STEP 3: Subject-wise averages ─────────────────────────────────────────────
# axis=0 means "average down rows" (i.e. average all 30 students for each subject)
subject_avg = np.mean(marks, axis=0)      # shape: (5,)


# ── STEP 4: Top 3 students using argsort ──────────────────────────────────────
# argsort gives you the POSITIONS sorted from lowest to highest
# Example: avg = [55, 78, 61] → argsort → [0, 2, 1]  (index of smallest to largest)
# [::-1] reverses it so it goes highest to lowest
# [:3] takes only the first 3 positions

sorted_positions = np.argsort(avg_marks)[::-1]   # all 30, best first
top3_positions   = sorted_positions[:3]           # just the top 3 positions


# ── STEP 5: Assign grades using np.where ──────────────────────────────────────
# np.where(condition, value_if_true, value_if_false)
# We nest multiple np.where to handle all grade ranges
# Read from inside-out:
#   if avg >= 90 → "A+"
#   else if avg >= 80 → "A"
#   else if avg >= 70 → "B"
#   else if avg >= 60 → "C"
#   else if avg >= 50 → "D"
#   else             → "F"

grades = np.where(avg_marks >= 90, "A+",
         np.where(avg_marks >= 80, "A",
         np.where(avg_marks >= 70, "B",
         np.where(avg_marks >= 60, "C",
         np.where(avg_marks >= 50, "D", "F")))))


# ── STEP 6: Print subject-wise averages ───────────────────────────────────────
print("=" * 45)
print("        SUBJECT-WISE CLASS AVERAGES")
print("=" * 45)
for i in range(len(subjects)):
    print(f"  {subjects[i]:<12} :  {subject_avg[i]:.1f}")
print()


# ── STEP 7: Print top 3 students ──────────────────────────────────────────────
print("=" * 45)
print("             TOP 3 STUDENTS")
print("=" * 45)
print(f"  {'Rank':<6} {'Name':<14} {'Average':<10} {'Grade'}")
print("-" * 45)
for rank, pos in enumerate(top3_positions, start=1):
    # pos is the index (position) of the student in our array
    print(f"  {rank:<6} {student_names[pos]:<14} {avg_marks[pos]:.1f}{'':6} {grades[pos]}")
print()


# ── STEP 8: Print all students result ─────────────────────────────────────────
print("=" * 65)
print("                   ALL STUDENTS RESULT")
print("=" * 65)
print(f"  {'Name':<14} {'Total':<8} {'Average':<10} {'Grade'}")
print("-" * 65)
for i in range(30):
    print(f"  {student_names[i]:<14} {total_marks[i]:<8} {avg_marks[i]:.1f}{'':6} {grades[i]}")
print()


# ── STEP 9: Save to file ──────────────────────────────────────────────────────
# We save the raw marks + total + average using np.savetxt
# np.column_stack joins arrays side by side as columns

data_to_save = np.column_stack([marks, total_marks, avg_marks])
# Now data_to_save has shape (30, 7):
# 5 subject marks + total + average = 7 columns

col_header = "\t".join(subjects) + "\tTotal\tAverage"

np.savetxt(
    "exam_results.txt",
    data_to_save,
    fmt       = ["%.0f"] * 6 + ["%.2f"],   # first 6 cols as int, last col as decimal
    delimiter = "\t",                        # tab-separated
    header    = col_header,
    comments  = ""                           # removes the default # at header line
)

# Also save a grade summary (text-based, not numbers)
with open("grade_summary.txt", "w") as f:
    f.write("Name           Total    Average    Grade\n")
    f.write("-" * 42 + "\n")
    for i in range(30):
        line = f"{student_names[i]:<15} {total_marks[i]:<9} {avg_marks[i]:<11.1f} {grades[i]}\n"
        f.write(line)

print("Files saved:")
print("  exam_results.txt   → raw marks + total + average")
print("  grade_summary.txt  → name, total, average, grade")