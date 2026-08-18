# 1. Write a program to find the greatest of four numbers entered by the user.

l1 = []
for i in range(1,5):
    num = int(input("Enter num :"))
    l1.append(num)
print(l1)

greatest = l1[0]
for num in l1:
    if num > greatest:
        greatest = num

print(greatest)

# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each 
# subject to pass. Assume 3 subjects and take marks as an input from the user.

l2 = []

for i in range(1,4):
    a = int(input(f"Enter subject {i} marks:"))
    l2.append(a)
print(l2)

per = sum(l2)
cent = per / 3

print(cent)

if cent >= 40 and l2[0] >= 33 and l2[1] >= 33 and l2[2] >= 33:
    print("Pass")
else:
    print("Fail")


# 3. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”,
#  “click this”. Write a program to detect these spams.

comment = input("message : ")
if 'Make a lot of money' in comment or 'buy now' in comment or 'subscribe this' in comment or 'click this' in comment:
    print("Spam")
else:
    print("Not Spam")

# 4. Write a program to find whether a given username contains less than 10 characters or not.

name = input('Enter username :')
if len(name) < 10:
    print("It is less than 10 characters")
else :
    print("Not less than 10 characters")

# 5. Write a program which finds out whether a given name is present in a list or not.

l3 = ['priya','sunny','amol','latika']
name = input("Enter name :")

if name in l3:
    print(name,'is present in list')
else :
    print('Not in list')

# 6. Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks = int(input('Enter student marks :'))
if marks >= 90 and marks <=100:
    print("Ex")
elif marks >=80 :
    print('A')
elif marks >=70 :
    print('B')
elif marks >=60 :
    print('C')
elif marks >=50 :
    print('D')
else:
    print('F')


# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input('Enter post :')
if "Harry" in post:
    print('talking about Harry')
else:
    print('Not talking about Harry')



