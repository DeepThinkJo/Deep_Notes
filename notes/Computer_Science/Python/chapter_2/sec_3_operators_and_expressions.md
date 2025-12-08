---
title: "Operators and Expressions"
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-07T05:28:00.000Z"
last_updated: "2025-12-07T06:08:00.000Z"
tags: []
chapter: 2
section: 3
---
# Operators and Expressions

## **What Are Operators and Expressions?**

**Operators** are symbols that tell Python to perform specific actions on values or variables.

They allow us to combine values, compare them, and express logic within a program.

An operator used together with values or variables forms an **expression**, which Python evaluates to produce a result.

## **Assignment Operator (**`=`**)**

The assignment operator stores a value in a variable:

```python
x = 10


```
This means the value `10` is stored in memory, and the variable `x` refers to that value.

Assignment is not a comparison—it is a binding of a name to a value.

## **Arithmetic Operators**

Arithmetic operators perform mathematical operations:

- `+` (addition)
- `-` (subtraction)
- `*` (multiplication)
- `/` (true division)
- `//` (floor division)
- `%` (modulo)
- `**` (exponentiation)


Python’s arithmetic operators also apply to certain non-numeric types:

- `"Hello" + "World"` → `"HelloWorld"`
- `"Hi" * 3` → `"HiHiHi"`
- `[1, 2] + [3]` → `[1, 2, 3]`
- `[0] * 4` → `[0, 0, 0, 0]`


These behaviors highlight Python’s flexible and dynamic typing system.

## **Comparison Operators**

Comparison operators evaluate relationships between values and produce boolean results:

- `==` (equal to)
- `!=` (not equal to)
- `>` , `<` (greater than, less than)
- `>=` , `<=` (greater/less than or equal to)


For example:

```python
5 < 10      # True
"cat" == "dog"   # False


```
Python compares strings lexicographically (alphabetical order based on Unicode).

## **Logical Operators**

Logical operators combine boolean expressions:

- `and` — True only if both sides are True
- `or` — True if at least one side is True
- `not` — negates a boolean value


Python also uses the concepts of **truthy** and **falsy** values:

- Falsy examples: `0`, `""`, `None`, `False`, empty lists/sets/dicts
- Everything else is truthy
## **Compound Assignment Operators**

These update a variable by applying an operation and assignment in one step:

- `+=`
- `=`
- `=`
- `/=`
- `//=`
- `%=`
- `*=`


Example:

```python
x = 5
x += 3   # x becomes 8


```
## **Operator Precedence**

Python evaluates expressions according to precedence rules:

1. Parentheses `()`
1. Exponentiation `*`
1. Multiplication, division, modulo (`*`, `/`, `//`, `%`)
1. Addition, subtraction (`+`, `-`)
1. Comparisons (`==`, `!=`, `>`, `<`, `>=`, `<=`)
1. Logical `not`, `and`, `or`


Using parentheses makes expressions clearer and avoids ambiguity.

## **Expression Evaluation**

An expression is any combination of values, variables, and operators that Python evaluates to produce a result.

Examples:

```python
3 + 4 * 2        # 11
(3 + 4) * 2      # 14
True and (5 > 3) # True


```
Understanding how Python evaluates expressions is essential for writing correct programs.
