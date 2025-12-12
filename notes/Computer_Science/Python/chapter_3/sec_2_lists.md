---
title: "Lists"
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-12T13:59:00.000Z"
last_updated: "2025-12-12T14:04:00.000Z"
tags: []
chapter: 3
section: 2
---
# **3.2 Lists**

A list is one of the most fundamental and widely used data structures in Python.

Unlike strings, lists are **mutable**, which means their contents can be changed after creation.

Lists are designed to store **collections of objects** and provide flexible ways to organize, access, and modify data.

## **Indexing and Slicing**

Like strings, lists are ordered sequences and support indexing.

```python
numbers = [10, 20, 30, 40]
numbers[0]     # 10
numbers[-1]    # 40


```
Slicing allows access to a sublist:

```python
numbers[1:3]   # [20, 30]
numbers[:2]    # [10, 20]
numbers[::2]   # [10, 30]


```
Slicing always returns a **new list**, not a view of the original.

## **Mutability and Modification**

Lists can be modified in place:

```python
numbers[1] = 25
numbers.append(50)
numbers.remove(30)


```
This mutability allows lists to grow, shrink, and change dynamically,

making them ideal for tasks such as data accumulation and iterative processing.

## **Nested Lists (Lists of Lists)**

A list can contain other lists as elements.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


```
Accessing elements in a nested list uses **multiple indices**:

```python
matrix[0]      # [1, 2, 3]
matrix[0][1]   # 2


```
Nested lists are commonly used to represent:

- matrices and grids
- tabular data
- hierarchical structures


Understanding index-of-index access is essential when working with multi-dimensional data.

## **Lists and Iteration**

Lists are naturally suited for iteration:

```python
for value in numbers:
    print(value)


```
They also integrate seamlessly with list comprehensions:

```python
squares = [x * x for x in numbers]


```
This allows concise and expressive data transformations.

## **Lists and Memory (Conceptual Model)**

From a conceptual standpoint, Python lists are **not the same as C arrays**.

- A C array stores elements **contiguously** in memory.
- A Python list stores **references (pointers)** to objects.


In other words:

- the list itself holds references
- each element lives separately in memory
- the list points to those elements


This design makes Python lists more flexible than fixed-size arrays,

but also means:

- accessing elements involves pointer dereferencing
- lists can store mixed data types
- resizing is handled dynamically


While Python lists are not classic linked lists,

their behavior is closer to a **dynamic array of references** rather than a raw memory block.

## **List Copying and Aliasing**

Because lists are mutable, copying behavior is important.

```python
a = [1, 2, 3]
b = a


```
Here, `a` and `b` refer to the **same list**.

To create a shallow copy:

```python
b = a.copy()
# or
b = a[:]


```
Understanding this distinction is critical to avoiding unintended side effects.

## **Why Lists Matter**

Lists are used everywhere:

- collecting results
- storing intermediate data
- representing datasets
- building higher-level data structures


They form the backbone of many Python programs and serve as the foundation for more advanced structures such as NumPy arrays and pandas DataFrames.
