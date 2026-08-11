# 1. Write a program using functions to find greatest of three numbers.

def greatest(a =10, b= 20,c=9):
    if a>b and a>c:
        print(a, "is greatest number")
    elif b>a and b>c :
        print(b, "is greatest number")
    else:
        print(c, "is greatest number")

greatest(c=74)

# 2. Write a python program using function to convert Celsius to Fahrenheit.


# 3. How do you prevent a python print() function to print a new line at the end.


# 4. Write a recursive function to calculate the sum of first n natural numbers.


# 5. Write a python function to print first n lines of the following pattern.
# ***
# **
# *
# - for n = 3

def question5():
    n = 3
    for i in range(1,n+1):
        print("*" * (6 -(2 +i)))

# question5()

# 6. Write a python function which converts inches to cms.


# 7. Write a python function to remove a given word from a list and strip it at the same time.


# 8. Write a python function to print multiplication table of a given number.

