students_height = [156,178,165,171,187]
total_height = 0
for student in students_height:
    total_height += student
print(f"total height = {total_height}")
print(f"number of students = {len(students_height)}")
print(f"average height = {round(total_height / len(students_height))}")