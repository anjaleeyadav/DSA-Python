# 1. Write a program to print multiplication table of a given number using for loop

def question1():
    a = int(input("Enter number :"))

    for i in range(1,11,1):
        print(a,"x",i,"=",a*i)

question1()

# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

def question2():
    l = ["Harry", "Soham", "Sachin", "Rahul"]

    for name in l:
        if name.startswith("S"):
            print("Good Morning",name)

question2()

# 3. Attempt problem 1 using while loop.

def question3():
    a = int(input("Enter number :"))

    i = 1
    while i<=10:
        print(a,"x",i,"=",a*i)
        i= i+1

question3()

# 4. Write a program to find whether a given number is prime or not.

def question4():
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

question4()


# 5. Write a program to find the sum of first n natural numbers using while loop.

def question5():
    a = int(input("enter number :"))

    i= 1
    sum = 0
    while i <= a:
        sum = sum +i
        i = i+1
    print(sum) 

question5()

# 6. Write a program to calculate the factorial of a given number using for loop.

def question6():
    n = int(input("Enter number : "))

    fact = 1

    for i in range(1,n+1):
        fact = fact * i
    print(fact)

question6()

# 7. Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3

def question7():

    n = 3
    for i in range(1,n+1):
        print("*" * ((2 * i )- 1))

question7()

# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

def question8():
    n = 5
    for i in range(1,n+1,2):
        print("*" * ((2 * i) - i))

question8()

# 9. Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * *

def question9():
    n = 3
    for i in range(1,n+1):
        if i ==2:
            print("* *")
        else:
            print("* * *")
question9()

# 10. Write a program to print multiplication table of n using for loops in reversed order.

def question10():
    n = int(input("Enter number :"))
    for i in range(10,0,-1):
        print(n,"*",i,"=",n*i)

question10()

