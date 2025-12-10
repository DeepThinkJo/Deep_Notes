---
title: "Error Types and Basic "
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-10T14:24:00.000Z"
last_updated: "2025-12-10T14:30:00.000Z"
tags: []
chapter: 2
section: 8
---
# 2.8 Error Types and Basic Exception Handling

Errors are an inevitable part of programming.

They occur when Python encounters something it cannot interpret or execute.

Understanding different error types—and how to handle them—is essential for writing reliable programs.

Python handles unexpected situations using a mechanism called **exceptions**,

and programmers can use **exception handling** to control how a program responds when an error occurs.

## **Common Error Types**

Here are some of the most frequent errors you will encounter:

- SyntaxError: Occurs when Python cannot parse the code
- NameError: Occurs when a variable or function name is not defined
- TypeError: Occurs when an operation is applied to the wrong data type
- ValueError: Occurs when a variable has the right type but an inappropriate content
- IndexError: Occurs when indexing outside valid bounds
- ZeroDivisionError: Occurs when dividing by zero
## **Why Exception Handling Matters**

Without handling errors, a program simply stops when something unexpected happens.

This is dangerous when:

- user input is incorrect
- data is incomplete
- network requests fail
- files are missing
- numerical computations reach invalid states


To build robust programs, we must handle errors gracefully instead of crashing.

# **Basic Exception Handling: **`try`** and **`except`

The `try` block allows you to test code for errors.

The `except` block lets you define what happens when an error occurs.

```python
try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("Invalid input. Please enter a number.")


```
Instead of the program crashing when the user enters something invalid,

we can show a helpful message.

## **Catching Multiple Exceptions**

```python
try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("ValueError occurred")
except ZeroDivisionError:
    print("Cannot divide by zero")


```
## **A General **`except`

Sometimes you want to handle *any* error:

```python
try:
    risky_function()
except Exception:
    print("Something went wrong.")


```
Use this with caution—it's helpful for debugging or protecting large systems,

but should not replace specific exception handling.

## `else`** and **`finally`** (Basic Overview)**

```python
try:
    x = int("10")
except ValueError:
    print("Invalid number")
else:
    print("Conversion succeeded")
finally:
    print("This always runs")


```
- `else`: runs only if no exceptions occur
- `finally`: always runs, used for cleanup (closing files, freeing resources, etc.)
You will revisit `else` and `finally` in more depth later.

## **Exception Handling and Problem Solving**

Exception handling lets programmers build programs that:

- are safe
- provide meaningful feedback
- avoid unexpected crashes
- handle unpredictable input or data
- remain stable under real-world conditions


This is especially important for AI/ML systems where data reliability is critical.
