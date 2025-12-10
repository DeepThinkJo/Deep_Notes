---
title: "Functions"
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-10T14:20:00.000Z"
last_updated: "2025-12-10T14:21:00.000Z"
tags: []
chapter: 2
section: 7
---
# Functions

Functions are reusable blocks of code designed to perform specific tasks.

They allow programs to be organized into small, meaningful pieces and help avoid repetition.

Learning to write good functions is essential for writing clear, modular, and maintainable programs.

## **Why Functions Matter**

Functions are important because they:

- group related operations into a single unit
- reduce code duplication
- improve readability and structure
- allow decomposition of large problems into smaller parts
- support abstraction — hiding unnecessary detail


In real engineering work, functions are the building blocks from which entire systems are constructed.

## **Defining a Function**

You define a function using the `def` keyword:

```python
def function_name(parameters):
    # code block
    return value


```
Example:

```python
def square(x):
    return x * x


```
Calling the function:

```python
result = square(3)


```
## **Parameters and Arguments**

- **parameters**: variables listed in the function definition
- **arguments**: actual values passed when calling the function


Example:

```python
def greet(name):   # name is a parameter
    print("Hello,", name)

greet("Jo")        # "Jo" is an argument


```
## **Return Values**

`return` sends a value back to the caller.

```python
def add(a, b):
    return a + b

x = add(2, 3)


```
If a function does not have a `return` statement, it returns `None` by default.

## **Default Parameters**

Functions can have default values for parameters:

```python
def power(base, exponent=2):
    return base ** exponent


```
Usage:

```python
power(3)      # 9
power(3, 3)   # 27


```
Default parameters are useful when a value is optional or a common default exists.

## **Variable Scope (Basic)**

Variables created inside a function are **local** to that function:

```python
def func():
    x = 10  # local variable


```
Variables created outside a function are **global**:

```python
x = 5

def show():
    print(x)


```
A more detailed discussion of scope rules (LEGB rule) comes later in the advanced Functions chapter.

## **Docstrings**

Functions can include documentation:

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b


```
Docstrings help others understand your function’s purpose.

## **Functions and Problem Solving**

Functions enable:

- decomposition of large algorithms
- reusable components
- cleaner experimental code
- building libraries
- writing maintainable software


They are one of the most powerful tools in Python programming.
