# fruits = ['apple','banana','orange']
#
# print('original lists:', fruits)
#
# fruits.append('pineapple')
# print('updated lists:', fruits)
#
# fruits.insert(2,'Mango')
# print('Latest updated list:', fruits)
#
# #joining two list
# numbers = [1,2,3,4,5]
# print('numbers List:', numbers)
#
# even_numbers = [2, 4, 6, 8]
# print('even numbers:', even_numbers)
#
# numbers.extend(even_numbers)
# print('updated numbers List:', numbers)
#
# # deleting in lists
# del numbers[:3]
# print(numbers)
#
# #Class Activity
# list = [17, 38, 10, 25, 72]
#
# list.sort()
# print('sorted list:', list)
#
# list.append(12)
# print('updated list:', list)
#
# list.reverse()
# print('reversed list:', list)
#
# index = list.index(17)
# print(index)
#
# list.remove(38)
# print('removed 38:', list)
#
# #Dictionary
# student = {
#     'name': 'victor',
#     'age': 20,
#     'department': 'data science',
#     "Course": ['Python', 'Data Analysis'],
#     'reg_number': 2020,
# }
#
# print('student information:', student)
# print('student name', student['name'])
#
# student['GPA'] = '4.0'
# print('updated student GPA', student['GPA'])
#
#
# print('student information:', student)
#
# #student.clear()
# #print('student information:', student)
#
# #updating my dictionary
# student['GPA'] = '2.5'
# print('updated student GPA', student)
#
# dictionary class work
# students = {
#     'name': 'Alice',
#     'age': 21,
#     'major': 'data science'
# }
#
# print('Student dictionary', students)
#
# student_keys = students.keys()
# print(student_keys)
#
# student_values = students.values()
# print(student_values)
#
# students['age'] = '22'
# print('student updated age', students)
#
# students["graduation_year"] = '2025'
# print('student updated graduation_year', students)

# Sets in python
myset = {101, 102, 103, 104, 105}
print('here is my set:', myset)

#Update is used to add items from lists
fruits = ['apple', 'banana', 'cherry']

myset.update(fruits)
print('here is the update:', myset)

