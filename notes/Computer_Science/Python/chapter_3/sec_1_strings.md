---
title: "Strings"
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-12T13:43:00.000Z"
last_updated: "2025-12-12T13:52:00.000Z"
tags: []
chapter: 3
section: 1
---
# **3.1 Strings**

So far, we have worked with text values in Python as simple inputs or outputs.

However, unlike numbers such as `int` or `float`, a string is **not a single, atomic value**.

A string is a **data structure**—specifically, an **ordered sequence of characters**.

Understanding strings as data structures is essential, because text data appears everywhere:

user input, file contents, logs, configuration files, datasets, and natural language data.

## **Strings as Sequence Data Structures**

In Python, a string behaves like an array (or sequence):

- it has a length
- it supports indexing
- it supports slicing
- it can be iterated over
```python
s = "AI"
print(s[0])   # 'A'
print(s[1])   # 'I'


```
However, Python does **not** provide a built-in `char` type.

There is no single-character primitive type in Python.

In contrast, languages like **C** define:

```c
char c = 'A';


```
In Python, even a single character is still a string:

```python
c = "A"
type(c)   # str


```
This design choice simplifies the language and removes the need to distinguish between `char` and `string`.

## **Immutability of Strings**

Strings in Python are **immutable**.

Once a string object is created, its contents cannot be changed.

```python
s = "hello"
s[0] = "H"   # TypeError


```
Any operation that appears to modify a string actually creates a **new string object**.

```python
s = s.upper()


```
This immutability has important consequences for:

- memory management
- performance
- safety and predictability
## **Common String Functions and Methods**

Python provides many built-in tools for working with strings.

### **Length and Counting**

```python
len(s)       # returns the number of characters in the string
s.count("a") # returns how many times "a" appears in the string


```
### **Whitespace Handling**

```python
s.strip()  # removes left and right whitespace
s.lstrip() # removes left whitespace only
s.rstrip() # removes right whitespace only


```
### **Splitting and Joining**

```python
s.split(",")              # (str->list) splits a string into a list using "," as delimeter
" ".join(["a", "b", "c"]) # (list->str) joins a list of strings into one string with spaces


```
### **Replacing and Searching**

```python
s.replace("old", "new") # returns a new string with substrings replaced
s.find("sub")           # returns the index of first occurence, or -1 if not found


```
### **Case Conversion**

```python
s.upper()      # returns a copy with all characters in uppercase
s.lower()      # returns a copy with all characters in lowercase
s.capitalize() # returns a copy with the first character caplitalized
```
These methods allow strings to be transformed, analyzed, and prepared for further processing.

## **Strings and Memory (Conceptual View)**

Although Python hides low-level memory management, conceptually:

- a string is stored as a **contiguous sequence of characters in memory**
- indexing accesses characters by offset
- immutability ensures that shared string data remains safe


When a string is modified, Python allocates new memory and copies the data.

This makes string operations safe but can be expensive if done repeatedly in loops.

## **Why Strings Matter in Practice**

Strings are central to real-world programming:

- parsing user input
- reading files
- processing text data
- building datasets
- interacting with external systems


In AI and data science, text data is often the **raw input** that must be cleaned, tokenized, and transformed before any model can be applied.

Understanding strings as **immutable sequence data structures** prepares you for more advanced text processing and data manipulation techniques.
