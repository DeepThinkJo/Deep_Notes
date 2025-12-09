---
title: "Basic Data Types"
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-07T04:52:00.000Z"
last_updated: "2025-12-09T14:34:00.000Z"
tags: []
chapter: 2
section: 2
---
# 2.2 Basic Data Types

## **Why Do We Need Data Types?**

A computer processes many different kinds of information—numbers, text, logical values, and more.

To handle these correctly, the programming language must know **what kind of data** it is dealing with.

Python assigns a data type to every value, which determines:

- what operations the value can participate in
- how much memory the value needs
- how Python interprets the value during execution
Understanding data types is essential for writing correct programs.

## **Python’s Fundamental Data Types**

### **Integers (**`int`**)**

Whole numbers, such as `3`, `0`, `-12`.

Integers support arithmetic operations and are stored exactly.

### **Floating-point numbers (**`float`**)**

Numbers with decimal points, such as `3.14` or `0.001`.

They are approximations because they follow binary floating-point representation.


!!! note "Deep Thoughts of Jo — Why Floating-Point Numbers Are Approximations"
When Python stores a floating-point number, it does not store it exactly.

Computers use finite binary memory to represent numbers, and many decimal values cannot be expressed exactly in binary.

Values like 0.1 or 0.2 become infinite repeating fractions, so Python stores the closest possible approximation.

This phenomenon is known as floating-point precision error — a fundamental limitation of digital computation.

Later, you will learn how numerical errors arise and how engineers design stable algorithms despite these limitations.

For now, remember: floating-point numbers are approximations, not exact values.

### **Strings (**`str`**)**

A sequence of characters enclosed in quotes.

Strings represent text and support operations such as concatenation and indexing.

### **Booleans (**`bool`**)**

Logical values: `True` or `False`.

Used in comparisons and conditional statements.

### **None (**`NoneType`**)**

A special value that represents “no value” or “nothing.”

Frequently used to indicate the absence of a result.

## **Checking the Data Type: **`type()`

The `type()` function reveals the type of any value or variable:

```python
type(3)        # int
type("Hello")  # str
type(True)     # bool


```
## **Casting (Type Conversion)**

Sometimes we need to convert a value from one type to another.

This process is called **casting**.

Common casting functions:

- `int("10")` → `10`
- `float("3.5")` → `3.5`
- `str(42)` → `"42"`
- `bool(0)` → `False`, `bool(1)` → `True`


Casting helps control how data behaves in expressions.
