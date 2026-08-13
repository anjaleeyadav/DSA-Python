# 1. Write a program to store seven fruits in a list entered by the user.

fruits = []
for i in range(7):
    fruit = input(f"Enter fruits {i+1}:")
    fruits.append(fruit)
print(fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []
for i in range(6):
    mark = int(input(f'Enter student {i+1} marks :'))
    marks.append(mark)
marks.sort()
print(marks)

# 3. Write a program to sum a list with 4 numbers.

list1 = []

for i in range(4):
    s = int(input("Enter num :"))
    list1.append(s)

total = sum(list1)
print(total)


# 4. Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)

a = (7, 0, 8, 0, 0, 9)
total= a.count(0)
print(total)

# 5. Check that a tuple type cannot be changed in python.

tuple1 = ('apple','banana')
print(tuple1.append('kiwi'))

print(tuple1.replace('banana','grapes'))