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
