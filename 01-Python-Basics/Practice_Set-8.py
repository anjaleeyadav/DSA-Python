# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer:
    a =10
    b = 20
    c = a+b
    print(a+b)


# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    x = int(input('Enter number :'))
    print(x**2)
    print(x ** 0.5)

# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. 
# Does this change the class attribute?

class Test:
    a = 10

obj = Test()
obj.a = 0

print(obj.a)      
print(Test.a)


# 4. Add a static method in problem 2, to greet the user with hello.


class Employee:
    a = 10

    def show(self):
        print("This is an employee")

    @staticmethod
    def greet():
        print("Hello")


e = Employee()
e.greet()

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train 
# running under Indian Railways.

class Train:
    def __init__(self, train_no, seats, fare):
        self.train_no = train_no
        self.seats = seats
        self.fare = fare

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket booked successfully!")
        else:
            print("Sorry, no seats available.")

    def get_status(self):
        print("Train Number:", self.train_no)
        print("Available Seats:", self.seats)

    def get_fare(self):
        print("Fare per ticket: ₹", self.fare)


# Creating object
train = Train(12345, 5, 500)

train.get_status()
train.get_fare()

train.book_ticket()

train.get_status()


# 6. Can you change the self-parameter inside a class to something else (say “harry”)? Try changing self to “slf” or “harry” 
# and see the effects.