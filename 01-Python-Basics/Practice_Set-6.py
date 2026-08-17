# 1. Write a program to find the greatest of four numbers entered by the user.

# l1 = []
# for i in range(1,5):
#     num = int(input("Enter num :"))
#     l1.append(num)
# print(l1)

# greatest = l1[0]
# for num in l1:
#     if num > greatest:
#         greatest = num

# print(greatest)

# 2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.

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


# 3. A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.


# 4. Write a program to find whether a given username contains less than 10 characters or not.



# 5. Write a program which finds out whether a given name is present in a list or not.



# 6. Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F



# 7. Write a program to find out whether a given post is talking about “Harry” or not.