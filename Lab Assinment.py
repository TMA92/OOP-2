### 1. Function to compute (a + b)^2 = a^2 + b^2 + 2ab
def compute_formula(a, b):
    return a**2 + b**2 + 2 * a * b

# Example usage for compute_formula
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
result = compute_formula(a, b)
print(f"The result of (a + b)^2 is: {result}")

### 2. Using a lambda function for the same formula
compute_lambda = lambda a, b: a**2 + b**2 + 2 * a * b

# Example usage for lambda
a = int(input("Enter value for a (lambda): "))
b = int(input("Enter value for b (lambda): "))
result = compute_lambda(a, b)
print(f"The result of (a + b)^2 using lambda is: {result}")

### 3. Recursive function to compute factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage for factorial
n = int(input("Enter a number to compute its factorial: "))
result = factorial(n)
print(f"The factorial of {n} is: {result}")

### 4. Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage for prime checking
n = int(input("Enter a number to check if it's prime: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

###List
# Initialize list
a = [1, 3, 5, 7, 9]

# 1. Access elements, find length and type
print(a[-2], a[2])  # Access a[-2], a[2]
print(len(a), type(a))  # Find length and type

# 2. Change elements
a[3] = 50  # Change a[3] to 50
a[2] = 49  # Change a[2] to 49
print(a)

# 3. Add elements
a.append(100)  # Add 100 at the last index
a.insert(2, 200)  # Add 200 at index 2
print(a)

# 4. Remove elements
a.pop()  # Remove last element
del a[1]  # Remove element at index 1
print(a)

# 5. Join a new list
b = [2, 4, 6]
a += b  # Join with a new list [2, 4, 6]
print(a)

# 6. Copy all values into a new list
c = a.copy()
print(c)

# 7. Sort elements of b
b.sort()
print(b)

# 8. Loop through elements, break if 5 is found
for x in a:
    if x == 5:
        break
    print(x)

# 9. Find the largest number in a
print(max(a))

###Tuple
# Initialize tuple
a = (1, 3, 5, 7, 4)

# a) Find the sum of all odd numbers in the tuple
sum_odd = sum(x for x in a if x % 2 != 0)
print("Sum of odd numbers:", sum_odd)

# b) Find the element at the 2nd index
print("Element at index 2:", a[2])

# c) Count the number of odd and even numbers
odd_count = sum(1 for x in a if x % 2 != 0)
even_count = sum(1 for x in a if x % 2 == 0)
print("Odd count:", odd_count, "Even count:", even_count)

# d) Extend the tuple with (2, 4, 6)
a_extended = a + (2, 4, 6)
print("Extended tuple:", a_extended)

# e) Add a new item (400) at index 2 (convert to list for modification)
a_list = list(a)
a_list.insert(2, 400)
a_modified = tuple(a_list)
print("Modified tuple:", a_modified)

# f) Remove the last element
a_list.pop()
a_removed = tuple(a_list)
print("Tuple after removing last element:", a_removed)

# g) Perform slicing [-4:-1]
print("Sliced tuple:", a[-4:-1])

# h) Print the tuple using a loop and skip if element is 5
for x in a:
    if x == 5:
        continue
    print(x, end=" ")

###Set
# Define the sets
a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}

# 1. Print a, b
print("Set a:", a)
print("Set b:", b)

# 2. Print length and their type
print("Length of set a:", len(a))
print("Length of set b:", len(b))
print("Type of set a:", type(a))
print("Type of set b:", type(b))

# 3. Add a new element 10 in set a
a.add(10)
print("Set a after adding 10:", a)

# 4. Remove 8 from the set a
a.discard(8)
print("Set a after removing 8:", a)

# 5. Perform union, intersection, difference, symmetric difference, is subset operation on set a and set b
union_ab = a.union(b)
intersection_ab = a.intersection(b)
difference_ab = a.difference(b)
symmetric_difference_ab = a.symmetric_difference(b)
is_subset_ab = a.issubset(b)

print("Union of a and b:", union_ab)
print("Intersection of a and b:", intersection_ab)
print("Difference of a and b:", difference_ab)
print("Symmetric difference of a and b:", symmetric_difference_ab)
print("Is a subset of b:", is_subset_ab)

# 6. Join a new list [2, 3, 4] with set a
new_list = [2, 3, 4]
a.update(new_list)
print("Set a after joining with [2, 3, 4]:", a)

###Dictionary
# Define the dictionary
employee = {
    "name": "A",
    "age": 40,
    "type": {"developer": ["ios", "android"]},
    "permanent": True,
    "salary": 30000,
    100: (1, 2, 3),
    4.5: [5, 6, True, 7, 1]
}

# 1. Print length, type of employee
print(len(employee))
print(type(employee))

# 2. Access the key employee["type"]["developer"]
print(employee["type"]["developer"])

# 3. Change the value of "permanent" to False
employee["permanent"] = False

# 4. Add new key "gender" having value "male"
employee["gender"] = "male"

# 5. Remove "age" key from dictionary
employee.pop("age")

# 6. Use keys(), values(), items()
print(employee.keys())
print(employee.values())
print(employee.items())

# 7. Iterate the dictionary using loop
for key, value in employee.items():
    print(f"{key}: {value}")

###String
# Declare variables
a = "hello"
b = "world"
c = "python"
d = a + b + c

# Find the length of d and print it
print("Length of d:", len(d))

# Check if "a2" is present in d
print("Is 'a2' in d?", "a2" in d)

# Perform various string operations on d
print("Upper case:", d.upper())
print("Lower case:", d.lower())
print("Title case:", d.title())
print("Stripped:", d.strip())
print("Is digit:", d.isdigit())
print("Find '3g':", d.find("3g"))
print("Capitalized:", d.capitalize())
print("Is alphanumeric:", d.isalnum())
print("Count 'b2':", d.count("b2"))
print("Split:", d.split())
print("Swap case:", d.swapcase())
print("Left stripped:", d.lstrip())
print("Replace 'hello' with 'python':", d.replace("hello", "python"))

###Class Obj
# Class definitions based on the diagrams

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print(f"Name: {self.name}, Price: {self.price}")

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail()
        print(f"Warranty: {self.warranty}")

class Shape:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

    def display_info(self):
        print(f"Shape: {self.name}")

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
product = Product("Laptop", 1000)
product.display_detail()

electronic_product = ElectronicProduct("Smartphone", 800, "2 years")
electronic_product.display_detail()

shape = Shape("Generic Shape")
shape.display_info()

rectangle = Rectangle("Rectangle", 5, 10)
rectangle.display_info()
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

###Encapsulation
class Vehicle:
    def __init__(self, color):
        self.color = color

    def vehicleInfo(self):
        return f"Vehicle Color: {self.color}"

class Taxi(Vehicle):
    def __init__(self, color, model, capacity, variant):
        super().__init__(color)
        self.__model = model
        self.__capacity = capacity
        self.__variant = variant

    def getModel(self):
        return self.__model

    def getCapacity(self):
        return self.__capacity

    def getVariant(self):
        return self.__variant

    def setModel(self, model):
        self.__model = model

    def setCapacity(self, capacity):
        self.__capacity = capacity

    def setVariant(self, variant):
        self.__variant = variant

    def vehicleInfo(self):
        return f"Taxi Model: {self.__model}, Capacity: {self.__capacity}, Variant: {self.__variant}, Color: {self.color}"

# Create two instances of Taxi
t1 = Taxi("Red", "Sedan", 4, "Standard")
t2 = Taxi("Blue", "SUV", 7, "Luxury")

# Display information for both instances
print(t1.vehicleInfo())
print(t2.vehicleInfo())

###Inheritance
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"Name: {self.first_name} {self.last_name}")

class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.graduation_year = graduation_year

    def display(self):
        super().display()
        print(f"Graduation Year: {self.graduation_year}")

class Teacher(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print(f"Joining Year: {self.joining_year}")

class Admin(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print(f"Joining Year: {self.joining_year}")

class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")

class Alumni(Student):
    def __init__(self, first_name, last_name, graduation_year, passing_year):
        super().__init__(first_name, last_name, graduation_year)
        self.passing_year = passing_year

    def display(self):
        super().display()
        print(f"Passing Year: {self.passing_year}")

class CurrentStudent(Student):
    def __init__(self, first_name, last_name, graduation_year, current_semester):
        super().__init__(first_name, last_name, graduation_year)
        self.current_semester = current_semester

    def display(self):
        super().display()
        print(f"Current Semester: {self.current_semester}")

###Polymorphism
# Define the classes based on the diagram
class Department:
    def __init__(self, name):
        self.name = name

    def profile(self):
        return f"Department: {self.name}"

class Teacher(Department):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def profile(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"

class Author(Department):
    def __init__(self, name, books):
        super().__init__(name)
        self.books = books

    def profile(self):
        return f"Author: {self.name}, Books: {self.books}"

class TeacherAuthor(Teacher, Author):
    def __init__(self, name, subject, books):
        Teacher.__init__(self, name, subject)
        Author.__init__(self, name, books)

    def profile(self):
        return f"TeacherAuthor: {self.name}, Subject: {self.subject}, Books: {self.books}"

# Example usage
ta = TeacherAuthor("John Doe", "Mathematics", ["Book1", "Book2"])
print(ta.profile())

# Answering the questions:
# 1. Runtime polymorphism example
def display_profile(department):
    print(department.profile())

display_profile(ta)  # This will call the profile method of TeacherAuthor

# 2. Accessing methods
print(ta.profile())

# 3. If both classes have the same method profile() and you call it through TeacherAuthor object
# The method resolution order (MRO) will determine which profile() method is called.
# In this case, it will call the profile() method of TeacherAuthor.

###Exception handling
# Task 1: Custom Exception for Invalid Voter Age
class InvalidVoterException(Exception):
    pass

def check_voter_age(age):
    if age < 18:
        raise InvalidVoterException("Age must be 18 or older to vote.")
    return "Valid voter age."

# Task 2: Custom Exception for Salary Not In Range
class SalaryNotInRange(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        if not (10000 <= salary <= 50000):
            raise SalaryNotInRange("Salary must be between 10000 and 50000.")

    def display_salary(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

# Task 3: Division Operation on Array
def divide_array(arr, divisor):
    try:
        return [x / divisor for x in arr]
    except ZeroDivisionError:
        return "Division by zero is not allowed."

# Example usage
try:
    print(check_voter_age(17))
except InvalidVoterException as e:
    print(e)

try:
    emp = Employee("John Doe", 60000)
    print(emp.display_salary())
except SalaryNotInRange as e:
    print(e)

arr = [10, 5, 15, 20]
divisor = 5
print(divide_array(arr, divisor))

###Numpy
import numpy as np

# Task 1: Convert data type into float
score = np.array([85, 90, 78, 92, 88], dtype=float)

# Task 2: Create a copy and add 5 points
a_score = score.copy() + 5

# Task 3: Find shape, ndim, size, itemsize, dtype, sort
print("Shape:", score.shape)
print("Number of dimensions:", score.ndim)
print("Size:", score.size)
print("Item size:", score.itemsize)
print("Data type:", score.dtype)
print("Sorted scores:", np.sort(score))

# Task 4: Find index of scores greater than 80
print("Indices of scores > 80:", np.where(score > 80))

# Task 5: Find min, max, std, var, sum, mean, axis-wise mean
print("Min:", np.min(score))
print("Max:", np.max(score))
print("Standard deviation:", np.std(score))
print("Variance:", np.var(score))
print("Sum:", np.sum(score))
print("Mean:", np.mean(score))

# Task 6: Print specific slices
print("score[:2]:", score[:2])
print("score[3:-1]:", score[3:-1])
print("score[1:4]:", score[1:4])

### Task 1,2
from abc import ABC, abstractmethod


# Task 01
class Vehicle(ABC):
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")


class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass


# Creating an object of Car
car = Car()
car.start()
car.stop()


# Task 02
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def startEngine(self):
        pass

    def description(self):
        return f"Brand: {self.brand}"


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def startEngine(self):
        print(f"{self.brand} {self.model} engine started")


# Creating an object of Car
car = Car("Toyota", "Corolla")
print(car.description())
car.startEngine()

# Trying to create an object of Vehicle class will raise an error
try:
    vehicle = Vehicle("Generic Brand")
except TypeError as e:
    print(e)

