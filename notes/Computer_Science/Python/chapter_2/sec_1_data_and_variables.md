---
title: "Data and Variables"
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-07T04:33:00.000Z"
last_updated: "2025-12-10T14:42:00.000Z"
tags: []
chapter: 2
section: 1
---
# 2.1 Data and Variables

## What Is Data?

**Data** is information that a computer stores and processes.

At the lowest level, all data is represented as **bits** (0s and 1s).

Eight bits form a **byte**, the basic unit of digital storage.

Computers ultimately manipulate only these binary patterns, regardless of whether the data represents numbers, text, or something more complex.

## How Computers Store Data

Computers store data in **memory (RAM)**.

Memory consists of many storage locations, each with a unique **address**.

When the computer needs to work with a value (such as a number or a string), that value is placed somewhere in memory.

The CPU reads and writes data to memory using these numeric addresses.

However, these raw addresses are inconvenient for humans to use.

## What Is a Variable?

A variable is a **name **given to a value stored in memory.

Instead of remembering a memory address like `0x7ffde310` , we assign a readable label—such as `age`, `total`, or `message`.

When we write:

```python
x = 10


```
Python stores the value `10` in memory and binds the name `x` to that location.

> Memory stores data, and variables give us names to access that data.
## Variable Naming Rules

Python variable names must follow certain rules:

- Use letters, digits, and underscores (`_`)
- Cannot start with a digit
- No spaces allowed
- Cannot use reserved keywords (`for`, `if`, `class`, etc.)
- Case-sensitive (`Age` and `age` are different)


Good variable names should be descriptive and readable.
