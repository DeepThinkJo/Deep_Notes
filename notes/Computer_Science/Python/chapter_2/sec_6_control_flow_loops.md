---
title: "Control Flow, Loops"
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-10T14:09:00.000Z"
last_updated: "2025-12-10T14:47:00.000Z"
tags: []
chapter: 2
section: 6
---
# 2.6 Control Flow — Loops

Loops allow a program to repeat actions efficiently.

They are essential in programming because many tasks require performing the same operation multiple times—processing datasets, iterating numerical updates, or repeatedly checking conditions.

Python provides two main loop types—`while` and `for`—and several control statements (`break`, `continue`, `pass`) that determine how loops behave.

## The `while` Loop

A `while` loop repeats its body *as long as* a condition remains `True`.

```python
while condition:
    # repeated code


```
Example:

```python
count = 0
while count < 3:
    print("Hello")
    count += 1


```
### When to Use a `while` Loop

Use it when:

- the number of repetitions is unknown
- repetition must continue until some condition changes
- you are waiting for a specific event (user input, sensor data, etc.)
## The `for` Loop

A `for` loop iterates over a sequence:

```python
for item in sequence:
    # repeated code


```
Example:

```python
for ch in "AI":
    print(ch)


```
### When to Use a `for` Loop

Use `for` when you know *what* you are iterating over—lists, strings, ranges, and other iterable objects.

## The `range()` Function

`range()` generates integer sequences commonly used for iterative tasks.

```python
range(stop)
range(start, stop)
range(start, stop, step)


```
Example:

```python
for i in range(3):
    print(i)


```
## Loop Variables

The loop variable takes on each value in the iteration sequence.

Although Python keeps this variable available after the loop, many other languages do not.

```python
for x in [1, 2, 3]:
    print(x)


```
## `break` — exit the loop immediately

`break` stops the loop entirely, regardless of the condition or remaining elements.

```python
for n in [1, 2, 3, 99, 4]:
    if n == 99:
        break
    print(n)


```
Output:

```
1
2
3


```
Useful when:

- a desired value is found
- further processing is unnecessary
- the loop must terminate early
## `continue` — skip the current iteration

`continue` jumps to the next iteration of the loop without executing the remaining code in the loop body.

```python
for n in range(5):
    if n % 2 == 0:
        continue
    print(n)


```
Output:

```
1
3


```
Useful for:

- skipping invalid or unneeded values
- filtering data inside a loop
## `pass` — do nothing

`pass` is a no-operation placeholder.

It does nothing but allows for syntactically complete code.

```python
for n in range(3):
    pass


```
Common uses:

- when planning code structure
- when stubbing out functions or classes
- when a loop must exist syntactically but perform no actions
## Loops in Problem Solving

Loops enable tasks such as:

- iterating through data
- aggregating results
- searching for values
- building simulations
- performing iterative numerical algorithms (gradient descent, optimization)


Understanding loops and loop control statements builds the foundation for algorithmic thinking.
