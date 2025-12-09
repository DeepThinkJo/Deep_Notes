---
title: "Input and Output"
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-08T14:53:00.000Z"
last_updated: "2025-12-09T14:42:00.000Z"
tags: []
chapter: 2
section: 4
---
# 2.4 Input and Output

## **Output with **`print()`

Programs often need to display information to the user.

In Python, the primary tool for producing output is the `print()` function:

```python
print("Hello, world!")


```
`print()` converts values to strings and displays them.

By default, it ends output with a newline.

> Deep Thoughts of Jo — Understanding the True Behavior of print()
## **String Formatting in Python**

When printing dynamic information, we often need to insert variables into strings.

Python provides **three major formatting styles**, each created at a different time in Python’s evolution.

### **1. f-strings (Recommended, Modern)**

Introduced in Python 3.6, f-strings are the cleanest and most efficient way to format strings.

```python
name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")


```
**Pros:**

- Most readable
- Fastest
- Supports inline expressions
### **2. **`str.format()`** (Older, Still Common)**

Before f-strings, the `.format()` method was the standard way to format strings.

```python
print("My name is {} and I am {} years old.".format(name, age))


```
You can also reference arguments by index or name:

```python
print("{1} is older than {0}".format("Alice", "Bob"))
print("{name} is {age}".format(name="Alice", age=20))


```
### **3. **`%`** Formatting (Very Old, from C-style printf)**

This method comes from C’s formatting style and is now mostly legacy:

```python
print("My name is %s and I am %d years old." % (name, age))


```
Still works, but offers fewer features and is considered outdated.

### **Which One Should You Use?**

Use **f-strings** unless you have a specific reason not to.

They are clearer, safer, and designed for modern Python.

## **Input with **`input()`

```python
x = input("Enter something: ")


```
## `input()`** Always Returns a String**

```python
x = input("Enter a number: ")
print(type(x))  # str


```
Casting is required for numeric input:

```python
x = int(input("Enter an integer: "))
y = float(input("Enter a floating-point number: "))


```
## **Combining Input and Output**

```python
name = input("Name: ")
year = int(input("Birth year: "))
age = 2025 - year

print(f"Hello, {name}! You are {age} years old.")


```
## A Note About User Input and Errors

Unlike `print()`, which always behaves predictably, the `input()` function depends entirely on what the user types.

This means the program may receive unexpected or invalid data.

In the worst case, such input can cause errors—for example, entering text when the program expects a number will raise a `ValueError` and immediately stop execution.

This raises an important programming question:

> How can we prevent our program from crashing when the user makes a mistake?
The answer is **exception handling**, a core technique that allows a program to detect and manage unexpected situations without stopping.

You will learn how to use `try`, `except`, and other tools to make your programs robust and stable in a later chapter.
