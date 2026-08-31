# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

# 1. Create a class (2-D vector) and use it to create another class
# representing a 3-D vector.

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"Vector is: {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"Vector is: {self.i}i + {self.j}j + {self.k}k")


v2 = TwoDVector(2, 3)
v2.show()

v3 = ThreeDVector(2, 3, 4)
v3.show()


# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’.
# Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def eat(self):
        print("Animals can eat")


class Pets(Animals):
    def play(self):
        print("Pets can play")


class Dog(Pets):
    def bark(self):
        print("Dog barks: Woof Woof!")


# Creating object of Dog
d = Dog()

d.eat()    # Method from Animals
d.play()   # Method from Pets
d.bark()   # Method from Dog



# 3. Create a class ‘Employee’ and add salary and increment properties to it. Write a method ‘salaryAfterIncrement’ method with 
# a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 50000
    increment = 10

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, newSalary):
        self.increment = ((newSalary / self.salary) - 1) * 100


e = Employee()

print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 55000




#  4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.      




# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the
#  dot(.) product of them.




# 6. Write __str__() method to print the vector as follows:
# 7i + 8j + 10k
# Assume vector of dimension 3 for this problem.






# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector