# 1. Write a program to print multiplication table of a given number using for loop

# a = int(input("Enter number :"))

# for i in range(1,11,1):
#     print(a,"x",i,"=",a*i)


# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if name.startswith("S"):
#         print("Good Morning",name)


# 3. Attempt problem 1 using while loop.

# a = int(input("Enter number :"))

# for i in range(1,11,1):
#     print(a,"x",i,"=",a*i)


# 4. Write a program to find whether a given number is prime or not.

num = int(input("Enter number :"))

if num <= 1:
    print("Not prime")
else: 
    for i in range(2,num):
        if num % i ==0:
            print("Not prime")
            break
    else:
        print("prime")



# 5. Write a program to find the sum of first n natural numbers using while loop.


# 6. Write a program to calculate the factorial of a given number using for loop.


# 7. Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3


# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3


# 9. Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * *


# 10. Write a program to print multiplication table of n using for loops in reversed order.