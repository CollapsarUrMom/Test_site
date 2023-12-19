students = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "Dave": "B",
    "Eve": "A"
}

target_grade = "B"
keys = []

for key in students:
    print
    if students[key] == target_grade:
        keys.append(key)


#keys = [key for key in students if students[key] == target_grade]

print("Keys with target grade:", keys)