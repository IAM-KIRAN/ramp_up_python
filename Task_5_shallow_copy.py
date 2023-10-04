import copy

students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 22}]
shallow_copy_students = copy.copy(students)

print(students[0] is shallow_copy_students[0])
print(students[1] is shallow_copy_students[1])

shallow_copy_students[0]['name'] = 'kiran'


print(shallow_copy_students)


print(students)