students ={
    "Anu":[85,90,78],
    "gowri":[72,89,91],
    "vishnu":[89,69,78]
}
for name,marks in students.items():
    total = sum(marks)
    average= sum(marks)/len(marks)
    print(f"student: {name}")
    print(f"marks: {marks}")
print(f"total: {total}")
print(f"average: {average:.2f}")
print("."*20)