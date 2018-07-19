---
title: Course Notes 
---

## Simple Functions
We used the `print()` function above to print our name. But, what is a function? 

> **Function** – Code that is grouped together and packaged under a name, so it can be called in one line.

Functions are the foundation of computer programming. Not only do they make it easier to read code, but they also allow us to write code that we can be reused over and over. Well-written functions are the mark of an engineer with good **style**\*.

(\*What is style? Style is what we call _the way in which code is written_. A program with good style typically has descriptive names and short, readable functions. We will go more into this later.)

```python
def this_is_a_function():
    if not front_is_blocked():
        move()
    turn_right()
    turn_right()
    move()
    move()
```
Functions are capable of doing many things. Here, we will focus on the essential features of a function. Let's break the above function down by parts.

<img class="computer_diagram" align="right" width="100%" src="figures/fig_simple_function_breakdown.png">

A function in Python is always started with the word `def` (1). Following the word `def` is the name of the function, in this case `this_is_a_function` (2), a set of parentheses (we will talk about these later) (3), and a colon (4). The commands packaged in the function are called the **body** of the function (5). These components are present in _every single_ function.