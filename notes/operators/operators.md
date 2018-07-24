---
title: Operators
---

Variables are how computers store information. But what good is storing information without the ability to make them interact?

The four variable classes we have covered so far - ints, floats, booleans, and strings - interact through what are called **operators**.

<div class="definition-section" markdown="1">

<span class="definition-title">Definition</span>
**Operators** - symbols used to allow values to interact.

</div>

Operators allow variables or raw values (ints, floats, booleans, and strings NOT stored in variables) to interact with each other. There are three main types of operators: _logical_, _arithmetic_, and _relational_.

### Logical Operators

As it turns out, you already know about logical operators! If you want to do some review, check out the _Conditional Statements_ notes on logical operators [here](https://geoffreyangus.github.io/CS106R/notes/conditional_statements/conditional_statements#combining-conditions).

### Arithmetic Operators

Arithmetic operators are simple. They are the operators you know and love. They come from math, and follow basically all of the rules you have already learned in school. Most importantly, they follow the rules associated with calculation priority.

1. `**`, Exponentials (this is how exponents are written in Python! 3<sup>2</sup> is the same as `3 ** 2`.)
2. `*` or `/`, Multiplication and Division
3. `+` or `-`, Addition and Subtraction

The arithmetic operators allow us to put together integers and floats in order to make rapid calculations. With arithmetic operators (and all other operators), we can mix the use of variables and raw values. 

For example:
```python
degrees_fahrenheit = 98.6

degrees_celsius = (degrees_fahrenheit - 32) * 5 / 9
```
Above, we are using arithmetic operators in order to do the temperature conversion between Fahrenheit and Celsius. Notice that we can use the variable `degrees_fahrenheit` in order to represent the value 98.6 in the calculation of `degrees_celsius`.

Check out the exercise to get some practice with arithmetic operators and variables!

<iframe frameborder="0" width="100%" height="600px" src="scientific notation"></iframe>
<iframe frameborder="0" width="100%" height="600px" src="scientific notation (negative) and integer division"></iframe>
<iframe frameborder="0" width="100%" height="600px" src="integer divided by a string and add two strings together"></iframe>
<iframe frameborder="0" width="100%" height="600px" src="True + 2"></iframe>

### Relational Operators

In addition to arithmetic operators, we have what are called relational operators. These operations also come from math, but they are used slightly differently in computer programming.

Let's take the most simple operator, the **Equality Operator**, as an example.

<div class="definition-section" markdown="1">

<span class="definition-title">Definition</span>
**Equality Operator** - This guy: `==`. It checks whether two values are the same. Note: this is NOT the same as the _assignment_ operator (`=`)! 

</div>

The equality operator, just like the arithmetic operators, must be put in between two values. 

```python
first_value == second_value
```

The entire statement above is what is called an _expression_. If an expression is correct, the entire thing is replaced by a `True` boolean, meaning that this expression...
```python
5 + 2 == 3 + 4
```
... is equal to this boolean value:
```python
True
```
In addition, if the expression is incorrect, the entire expression is replaced by a `False` boolean, meaning that this expression...
```python
4 == 7
```
... is equal to this boolean value:
```python
False
```
Remember that, with operators, can use variables and raw values togethers as well. This means that this piece of code...
```python
curitiba_population = 1765000

5 == curitiba_population
```
... is exactly the same as this piece of code:
```python
curitiba_population = 1765000

False
```
1. `==`, Equality Operator. Evaluates to `True` when the two values surrounding it are the same.
2. `!=`, Inequality Operator. Evaluates to `True` when the two values surrounding it are different. Equivalently, the Inequality Operator evaluates to `False` when the two values surrounding it are the same.
3. `>`, "Greater Than" Operator. Evaluates to `True` when the first value is greater than the second value.
4. `>=`, "Greater Than or Equal To" Operator. Evaluates to `True` when the first value is greater than the second value and when they are the same.
5. `<`, "Less Than" Operator. Evaluates to `True` when the first value is less than the second value.
6. `<=`, "Less Than or Equal To" Operator. Evaluates to `True` when the first value is less than the second value and when they are the same.



```Relational Operators and Conditional Statements

```python
count = 0

while count < 10:
    count = count + 1
```
