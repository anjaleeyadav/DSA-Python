# 1. Write a python program to display a user entered name followed by Good Afternoon using input() function.  

def greeting():
    name = input("Enter your name :")
    print("Good Afternoon",name)

greeting()

# 2. Write a program to fill in a letter template given below with name and date.  
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
name = input("Enter your name :")
date = input("Enter date :")

letter = letter.replace('<|Name|>',name)
letter = letter.replace('<|Date|>',date)

print(letter)
    

# 3. Write a program to detect double space in a string.

string = "hi my  name  is anjali  yadav"
if "  " in string:
    print("Double spaces")
else:
    print("No double spaces")


# 4. Replace the double space from problem 3 with single spaces.

string = "hi my  name  is anjali  yadav"
print(string.replace("  "," "))

# 5. Write a program to format the following letter using escape sequence characters.
# letter = "Dear anjali, This is the python practice seesion. All the best!"

print("Dear anjali,\n\tThis is the python practice seesion.\nAll the best!")

# letter = "Dear Harry, this python course is nice. Thanks!"