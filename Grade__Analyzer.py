import numpy as np

students = np.array([
    "Saphal",
    "Shishir",
    "Hari",
    "Ram",
    "Gita"
])

marks = np.array([78, 45, 92, 67, 55])

print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks :", np.min(marks))

result = np.where(marks >= 50, "Pass", "Fail")

print("\nResults:")
for name, mark, status in zip(students, marks, result):
    print(f"{name}: {mark} -> {status}")

rank_index = np.argsort(marks)[::-1]

print("\nRanking:")
for rank, index in enumerate(rank_index, start=1):
    print(f"Rank {rank}: {students[index]} ({marks[index]})")
    
