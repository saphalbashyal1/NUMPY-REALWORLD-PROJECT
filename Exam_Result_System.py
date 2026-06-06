import numpy as np
np.random.seed(0)
marks=np.random.randint(40,101,size=(30,5))

subjects=["Math","Physics","Chemistry","English","Computer"]
student_names=[f"Student_{i+1:02d}" for i in range(30)]

total_marks=np.sum(marks,axis=1)
avg_marks=np.mean(marks,axis=1)

subject_avg=np.mean(marks,axis=0)

sorted_positions=np.argsort(avg_marks)[::-1]
top3_positions=sorted_positions[:3]

grades=np.where(avg_marks>=90,"A+",
       np.where(avg_marks>=80,"A",
       np.where(avg_marks>=70,"B+",
       np.where(avg_marks>=60,"C",
       np.where(avg_marks>=50,"D",  "F"      
        )))))

print("=" * 45)
print("        SUBJECT-WISE CLASS AVERAGES")
print("=" * 45)
for i in range(len(subjects)):
    print(f" {subjects[i]:<12} : {subject_avg[i]:.1f}")
print()

print("=" * 45)
print("             TOP 3 STUDENTS")
print("=" * 45)
print(f" {'Rank':6} {'Name':<14} {'Average':<10} {'Grade'}")
print("-" * 45)
for rank,pos in enumerate(top3_positions,start=1):
    print(f" {rank:<6} {student_names[pos]:<14} {avg_marks[pos]:.1f} {'':6} {grades[pos]}")
print()
print("=" * 65)
print("                   ALL STUDENTS RESULT")
print("=" * 65)
print(f"{'Name':<14} {'Total':<8} {'Average':<10}{'Grade'}")
print("-" * 65)
for i in range(30):
    print(f"{student_names[i]:<14} {total_marks[i]:<8} {avg_marks[i]:.1f}{'':6} {grades[i]}")
print()

save_data=np.column_stack([marks,total_marks,avg_marks])

col_header=f"\t".join(subjects) + "\tTotal\tAverage"

np.savetxt(
    "exam_results.txt",
    save_data,
    fmt=["%.0f"]*6 + ["%.2f"],
    delimiter="\t",
    header=col_header,
    comments=""
)

with open("grade_summary.txt","w") as f:
    f.write("Name           Total    Average    Grade\n")
    f.write("-"*42+"\n")
    for i in range(30):
        line=f"{student_names[i]:15}{total_marks[i]:<4}{'':6}{avg_marks[i]:.1f}{'':6}{grades[i]}\n"
        f.write(line)
        
print("Files saved:")
print("  exam_results.txt   → raw marks + total + average")
print("  grade_summary.txt  → name, total, average, grade")        