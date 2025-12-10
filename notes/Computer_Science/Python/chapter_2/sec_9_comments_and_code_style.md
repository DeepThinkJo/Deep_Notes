---
title: "Comments and Code Style"
category: "Computer_Science"
subcategory: "Python"
created: "2025-12-10T14:32:00.000Z"
last_updated: "2025-12-10T14:49:00.000Z"
tags: []
chapter: 2
section: 9
---
# 2.9 Comments and Code Style

Readable code is just as important as correct code.

As programs grow larger, clarity becomes essential — not only for other people reading your code, but also for your future self.

Python encourages clean style and clear intentions through comments and formatting conventions.

Good code is not only about making the computer understand your instructions.

It is about writing code that humans can understand.

## Comments

### Single-line Comments

In Python, comments begin with `#`.

Anything after the `#` on the same line is ignored by Python.

```python
# This computes the area of a circle
area = 3.14 * r * r


```
Use comments to explain **why** something is being done, not **what** is being done.

If your code is clear, the “what” should already be obvious.

## Docstrings

Functions, classes, and modules can include multi-line documentation strings.

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b


```
Docstrings are used by tools such as IDEs, documentation generators, and help systems.

## Indentation

Python uses indentation to define code blocks, not braces `{}`.

This makes indentation part of Python’s syntax and one of its most distinctive features.

Standard indentation is **4 spaces** per level.

```python
if x > 0:
    print("Positive")


```
Avoid mixing tabs and spaces.

## Line Length

PEP 8 — Python’s official style guide — recommends:

- Maximum line length: **79 characters**
- For docstrings and comments: **72 characters**
This keeps code readable on various screens and tools.

## Naming Conventions

Python follows common naming styles:

- **variables/functions:** `lowercase_with_underscores`
- **classes:** `CamelCase`
- **constants:** `UPPERCASE_WITH_UNDERSCORES`
Examples:

```python
user_name = "Jo"
MAX_SIZE = 1000

class DataLoader:
    pass


```
Good names make code self-explanatory.

## Blank Lines and Organization

Use blank lines to separate logical sections of code.

Good spacing improves readability by grouping related logic.

```python
# Load data
load_data()

# Process data
process_data()

# Save output
save_results()


```
## Why Code Style Matters

Code is communication — between you and whoever reads your code.

Clean style helps:

- reduce bugs
- make programs easier to modify
- improve collaboration
- make your thinking clearer


Professional engineers follow style guides not because computers need it,

but because humans do.
