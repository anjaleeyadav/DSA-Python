# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

dictionary ={
    'namaste' : 'hello',
    'paani' : 'water',
    'ghar' : 'house',
    'haath' : 'hand'
}

a = input('Enter words :')
if a in dictionary:
    print(dictionary[a])
else:
    print('Not in dictionary')

# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).

# num = set()
# for i in range(8):
#     value = int(input(f"Enter number {i+1}:"))
#     num.add(value)
# print(num)


# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

set = {18,'18'}
print(set)

# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# my_set = set()
# my_set.add(20)  # 20 ==20.0 --> 20 ,both same in set
# my_set.add(20.0)
# my_set.add('20')

# print(my_set)
# print(len(my_set))

# 5. s = {}
# What is the type of 's'?

s1 = {}
print(type(s1))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

friends ={}

for i in range(4):
    name = input('Enter your name :')
    language = input("Enter your favourite language :")
    friends[name] = language 

print(friends)


# 7. If the names of 2 friends are same; what will happen to the program in problem 6?




# 8. If languages of two friends are same; what will happen to the program in problem 6?




# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}