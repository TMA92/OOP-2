#Python program to print "Hello Python"
print("Hello Python")

#Python program to do arithmetical operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (division by zero)"
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")

# Python program to find the area of a triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))  # Fixed the missing parenthesis
area = 0.5 * base * height
print(f"The area of the triangle is: {area}")

#Python program to solve quadratic equation
import cmath
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c
root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
print(f"The solutions are: {root1} and {root2}")


#Python program to swap two variables
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")
x, y = y, x
print(f"After swapping: x = {x}, y = {y}")

#Python Program to Generate a Random Number
import random
random_number = random.randint(1, 100)
print(f"The generated random number is: {random_number}")
kilometers = float(input("Enter the distance in kilometers: "))
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles.")

#Python program to convert Celsius to Fahrenheit
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

#Python program to display calendar
import calendar
year = int(input("Enter the year (e.g., 2024): "))
month = int(input("Enter the month (1-12): "))
cal = calendar.TextCalendar()
print(cal.formatmonth(year, month))

#Python Program to check if a Number is Positive, Negative or Zero
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Python Program to Check if a Number is Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Python Program to Check Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Python Program to Check Prime Number
number = int(input("Enter a number: "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#Python Program to Print all Prime Numbers in an Interval
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)

#Python Program to Find the Factorial of a Number
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = factorial_iterative(number)
    print(f"The factorial of {number} is: {factorial}")

#Python Program to Display the Multiplication Table
number = int(input("Enter a number to display its multiplication table: "))
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

#Python Program to Print the Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci(terms)

#Python Program to check Armstrong Number
def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)

    return sum_of_powers == number
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

#Python Armstrong Number
def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == number
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Armstrong numbers between {start} and {end} are:")
for number in range(start, end + 1):
    if is_armstrong(number):
        print(number)

#Python Program to Find the Sum of Natural Numbers
n = int(input("Enter a natural number: "))

if n < 1:
    print("Please enter a natural number (greater than 0).")
else:
    total = 0
    for i in range(1, n + 1):
        total += i

    print(f"The sum of natural numbers up to {n} is: {total}")

#Python Program to Print Reverse of a String
original_string = input("Enter a string: ")
reversed_string = original_string[::-1]
print(f"The reverse of the string is: {reversed_string}")

# Sum of First Ten Natural Numbers
sum_natural = sum(range(1, 11))
print(f"The sum of the first ten natural numbers is: {sum_natural}")

#  Find LCM
def lcm(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")

# Find HCF
def hcf(x, y):
    while y:
        x, y = y, x % y
    return x
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The HCF of {num1} and {num2} is: {hcf(num1, num2)}")

# Convert Decimal to Binary, Octal and Hexadecimal
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]
octal = oct(decimal)[2:]
hexadecimal = hex(decimal)[2:]
print(f"Binary: {binary}, Octal: {octal}, Hexadecimal: {hexadecimal}")

# Find ASCII Value of a Character
char = input("Enter a character: ")
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is: {ascii_value}")

# Simple Calculator
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")
    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation.")
calculator()

# Display Fibonacci Sequence Using Recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
print(f"Fibonacci sequence: {fibonacci(terms)}")

# Find Factorial of a Number Using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is: {factorial(number)}")

# Calculate the Power of a Number
def power(base, exponent):
    return base ** exponent
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))
print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")

# Add Two Matrices
def add_matrices(matrix_a, matrix_b):
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements for the first matrix:")
matrix_a = [[int(input(f"Enter element at position ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

print("Enter elements for the second matrix:")
matrix_b = [[int(input(f"Enter element at position ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

result_matrix = add_matrices(matrix_a, matrix_b)

print("Resultant Matrix after Addition:")
for row in result_matrix:
    print(row)

# Multiply Two Matrices
def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result
rows_a = int(input("Enter number of rows for first matrix: "))
cols_a = int(input("Enter number of columns for first matrix: "))
rows_b = cols_a
cols_b = int(input("Enter number of columns for second matrix: "))
print("Enter first matrix:")
matrix_a = [[int(input()) for _ in range(cols_a)] for _ in range(rows_a)]
print("Enter second matrix:")
matrix_b = [[int(input()) for _ in range(cols_b)] for _ in range(rows_b)]
result_matrix = multiply_matrices(matrix_a, matrix_b)
print("Resultant Matrix after Multiplication:")
for row in result_matrix:
    print(row)

# Transpose a Matrix
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter matrix:")
matrix = [[int(input()) for _ in range(cols)] for _ in range(rows)]
result_matrix = transpose_matrix(matrix)
print("Transposed Matrix:")
for row in result_matrix:
    print(row)

# Sort Words in Alphabetic Order
sentence = input("Enter a sentence: ")
words = sentence.split()
words.sort()
print("Sorted words:", ' '.join(words))

#  Remove Punctuation From a String
import string
text = input("Enter a string: ")
text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))
print("String without punctuation:", text_without_punctuation)

#  Convert List to String
my_list = ['Hello', 'World']
list_to_string = ' '.join(my_list)
print("List as string:", list_to_string)

#  Convert Int to String
number = 123
int_to_string = str(number)
print("Integer as string:", int_to_string)

# Concatenate Two Strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
concatenated_string = str1 + str2
print("Concatenated string:", concatenated_string)

#  Generate a Random String
import random
import string
length = 8
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print("Random string:", random_string)

#  Check Whether Given String is a Palindrome
string_to_check = input("Enter a string: ")
is_palindrome = string_to_check == string_to_check[::-1]
print("Is palindrome:", is_palindrome)

#  Convert Lowercase to Uppercase and Vice Versa
text = input("Enter a string: ")
converted_text = text.swapcase()
print("Converted string:", converted_text)

#  Find the Occurrence of a Substring Within a String
string = input("Enter a string: ")
substring = input("Enter a substring: ")
occurrence = string.count(substring)
print("Occurrence of substring:", occurrence)

# Append Element in the List
my_list = [1, 2, 3]
element = int(input("Enter an element to append: "))
my_list.append(element)
print("Updated list:", my_list)

#  Compare Two Lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
are_equal = list1 == list2
print("Are lists equal:", are_equal)

#  Convert List to Dictionary
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
dictionary = dict(zip(keys, values))
print("Converted dictionary:", dictionary)

#  Remove an Element from a List
my_list = [1, 2, 3, 4, 5]
element = int(input("Enter an element to remove: "))
my_list.remove(element)
print("Updated list:", my_list)

#  Add Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
added_list = [a + b for a, b in zip(list1, list2)]
print("Added list:", added_list)

#  Convert List to Set
my_list = [1, 2, 3, 2, 1]
my_set = set(my_list)
print("Converted set:", my_set)

#  Convert List to String (duplicate task)
my_list = ['Hello', 'World']
list_to_string = ' '.join(my_list)
print("List as string:", list_to_string)

#  Remove Duplicates from a List
my_list = [1, 2, 3, 2, 1]
unique_list = list(set(my_list))
print("List after removing duplicates:", unique_list)
