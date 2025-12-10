---
title: "Control Flow, Conditional Statements"
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-10T13:59:00.000Z"
last_updated: "2025-12-10T14:46:00.000Z"
tags: []
chapter: 2
section: 5
---
# 2.5 Control Flow — Conditional Statements

Conditional statements allow a program to make decisions.

They let Python choose whether to execute certain lines of code based on whether a condition is `True` or `False`.

### Why Conditions Matter

Real-world problems often require different actions depending on the situation:

- “If the temperature is below 0°C, warn about freezing.”
- “If the user enters a wrong password, deny access.”
- “If there is no more data, stop reading.”


In programming, these decisions are expressed using **conditional statements**.

## The `if` Statement

The simplest form of a conditional statement is:

```python
if condition:
    # code runs only when condition is True


```
Example:

```python
x = 10
if x > 0:
    print("x is positive")


```
## The `if-else` Structure

Use `else` when you want one of two possible paths to run:

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False


```
Example:

```python
num = 3

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


```
## Multiple Conditions: `elif`

Sometimes there are more than two possibilities.

`elif` (short for “else if”) allows for multiple branches:

```python
if condition1:
    ...
elif condition2:
    ...
elif condition3:
    ...
else:
    ...


```
Example:

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")


```
## Nested Conditionals

Conditional statements can be placed inside one another:

```python
x = 10

if x > 0:
    if x % 2 == 0:
        print("Positive even number")


```
Nested conditionals work, but deep nesting can make code harder to read.

In later chapters, you will learn cleaner techniques such as boolean expressions and guard clauses.

## Truthiness in Python

In Python, conditions do not need to be actual `True` or `False` values.

Many objects have an inherent “truthiness.”

The following evaluate to **False**:

- `0`
- `0.0`
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dict)
- `None`
- `False` itself


Everything else evaluates to **True**.

Example:

```python
name = ""

if name:
    print("You entered a name")
else:
    print("No name entered")


```
This prints:

```
No name entered


```
because an empty string is considered **False**.

## Summary

Conditional statements allow programs to:

- test conditions
- choose different paths
- react to user input
- enforce rules or constraints


They are one of the most fundamental tools in programming, forming the basis of decision-making in software.
