# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open('poems.txt','r') as f:
    text = f.read()
print(text)


if 'twinkle' in text:
    print('\ntwinkle is there' )
else:
    print('Not there')
    

# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 
# ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score 
# whenever the game() function breaks the Hi-score.

def game():
    score = int(input("Current score :"))
    return score


def hi_core():
    with open('high_score.txt','r') as f:
        old_score = int(f.read())
    return old_score


def result(score, old_score):
    print(score)
    print(old_score)

    if score > old_score:
        print('New highest score is :',score)

        with open('high_score.txt','w') as f:
            new = f.write(str(score))


    elif score <= old_score:
        print("Old high score remains")


score = game()
old_score = hi_core()
result(score, old_score)


# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in 
# a folder for a 13-year-old.  

import os

os.makedirs('tables', exist_ok= True)

for i in range(2,21):
    with open(f'tables/tables_{i}.txt','w') as f:
        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}\n")


#   --> to remove all the files 

# import os
# for i in range(2,21):
#     if os.path.exists(f"tables_{i}.txt"):
#         os.remove(f"tables_{i}.txt")

# 4. A file contains a word “Donkey” multiple times. You need to write a program which replaces this word with ##### by updating 
# the same file.

with open('repeated.txt','r') as f:
    text = f.read()

text = text.replace('Donkey','#####')

with open('repeated.txt','w') as f:
    f.write(text)


# 5. Repeat program 4 for a list of such words to be censored.

list = ['stubborn','slept','wild','kicked']

with open('repeated.txt','r')as f:
        text = f.read()


for i in list:
        if i in text:
            text = text.replace(i,'@@Censored Word@@')

with open('repeated.txt','w')as f:
    f.write(text)
        

# 6. Write a program to mine a log file and find out whether it contains ‘python’.

with open('log.txt','r') as f:
    text = f.read()

if 'Python' in text:
    print('Python is present in the log file')
else:
    print("Python is not present in the log file")



# 7. Write a program to find out the line number where python is present from ques 6.

with open('log.txt','r') as f:
    text = f.read()

for i in text:
    if i == "Python":
        print

# 8. Write a program to make a copy of a text file “this.txt”.

with open('this.txt','r')as f:
    text = f.read()

with open('copy.txt','w')as f:
    s = f.write(text)


#   'x' → sirf nayi file create karega. Agar file already hai → error.
#   'w' → file nahi hai to create karega; agar already hai to purana content overwrite karega.


# 9. Write a program to find out whether a file is identical and matches the content of another file.

with open('this.txt','r') as f:
    text = f.read()

with open('copy.txt','r') as f:
    content = f.read()

if text == content:
    print('File is identical and matches the content of another file.')
else:
    print('File is not identical and does not matches the content of another file.')



# 10. Write a program to wipe out the content of a file using python.

with open('copy.txt','w') as f:
    pass


# 11. Write a python program to rename a file to “renamed_by_python.txt”

import os 

os.rename('python.txt','renamed_by_python.txt')


