 Python Day 1: Getting Started
1. Introduction to Python
                                 What is Python?

Python is a high-level, interpreted programming language.
It is known for its readability and simplicity, making it ideal for beginners.
Installing Python

Download and install Python from the official site: python.org.
Ensure that the Python installation includes the pip package manager.
Setting Up the IDE (Integrated Development Environment)

1.For beginners, you can use IDEs like:
2.IDLE (comes with Python installation)
3.VSCode (Visual Studio Code)
4.PyCharm
5.Jupyter Notebooks for interactive coding
                                         
                                          2. Writing Your First Python Program
1.Open your IDE (IDLE, VSCode, etc.).
2.Create a new Python file and write the following code:
3.python
4.Copy code
5.Explanation: This is a basic Python program. print() is a built-in function that outputs text to the console.
        
                                           3. Basic Python Concepts
                                           
                                           
1.Variables and Data Types: Learn about variables and basic data types.
 Integer (int): a = 10
 Float (float): b = 3.14
 String (str): name = "Alice"
 Boolean (bool): is_active = True
 Basic Arithmetic Operations:

 python
 Copy code
print("Hello, World!")
a = 5
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division

Comments in Python:

Comments are used to explain code and are ignored by the interpreter.
Single-line comment: # This is a comment
Multi-line comment:
python
Copy code
"""
This is a 
multi-line comment.
"""
                                              4. Basic Input and Output

Taking User Input:
python
Copy code
name = input("Enter your name: ")
print("Hello, " + name + "!")
Explanation: input() gets input from the user and stores it in a variable.

5. Control Flow: Conditionals
If-Else Statements:
python
Copy code

age = int(input("Enter your age: "))
if age >= 18:
     print("You are an adult.")
else:
    print("You are a minor.")

6. Loops: Repeating Code
For Loop:

python
Copy code

for i in range(5):
     print(i)
This loop prints numbers from 0 to 4.

While Loop:
python
Copy code

count = 0
while count < 5:
    print(count)
    count += 1
Day 1 Summary
# Goal: Get familiar with Python's syntax, write simple programs, and understand how to perform basic operations like printing, input/output, conditionals, and loops.




                                          Day 2


1. Variables and Data Types Recap
Variables: Storing values in variables.
Data Types: Integers, floats, strings, booleans.

2. Basic Operations
Arithmetic operations: +, -, *, /, // (floor division), % (modulo), ** (exponentiation).
String operations: Concatenation, repetition.

3. Control Flow
if, elif, else: Conditional statements to control the flow.
Comparison operators: ==, !=, >, <, >=, <=.
Logical operators: and, or, not.

4. Loops
for loop: Iterate over a sequence (list, range, etc.).
while loop: Execute as long as a condition is true.
break and continue: Control loop flow.