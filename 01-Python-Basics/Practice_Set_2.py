# 1. Write a program using functions to find greatest of three numbers.

# def greatest(a =10, b= 20,c=9):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c :
#         return b
#     else:
#         return c

# print("greatest number is",greatest())
# # greatest()
# # greatest(c=74)



# # 2. Write a python program using function to convert Celsius to Fahrenheit.

# def celsius_to_faheren(celsius):
#     Fahrenheit = (celsius *(9/5)) +32
#     return Fahrenheit

# celsius = int(input("Enter celsius :"))

# result = celsius_to_faheren(celsius)
# print("Faherenheit is :",result)

# # 3. How do you prevent a python print() function to print a new line at the end.

# print("Hello", end = " ")
# print("World")

# # 4. Write a recursive function to calculate the sum of first n natural numbers.

# def sum_natural(n):
#     if n ==1:
#         return 1
#     else:
#         return n + sum_natural(n-1)

# n = int(input("Enter number :"))
# result = sum_natural(n)
# print("Sum is :",result)
# # 5. Write a python function to print first n lines of the following pattern.
# # ***
# # **
# # *
# # - for n = 3

# def question5():
#     n = 3
#     for i in range(1,n+1):
#         print("*" * (6 -(2 +i)))

# question5()

# # 6. Write a python function which converts inches to cms.

# def inches_to_cm(inches):
#     cm = inches * 2.54
#     return cm

# inches = int(input("Enter inches :"))
# result = inches_to_cm(inches)
# print("Centimeter is :",result)

# 7. Write a python function to remove a given word from a list and strip it at the same time.

def remove_word(words, word):
    new_list = []

    for item in words:
        item = item.strip()    # strip() --> remove extra spaces from starting and from ending.

        if item != word:
            new_list.append(item)

    return new_list

words = [' apple', 'kiwi ', ' peach ', ' kiwi']

result = remove_word(words,'kiwi')
print(result)

# 8. Write a python function to print multiplication table of a given number.

# def multiplication(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",n*i)

# num = int(input("Enter number :"))
# multiplication(num)    

