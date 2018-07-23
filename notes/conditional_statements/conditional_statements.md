---
title: Conditional Statements 
---
We've learned how to instruct PyBot to take actions using functions like `move()`, `turn_right()`, and `pick_beeper()`. We've also learned how to combine these functions together to create our own functions – for example, we combined three `turn_right()` calls into one function called `turn_left()`. 

But up until now, we've only been giving PyBot a list of actions to take. Everytime we run a particular program, PyBot does the exact same thing. Things get interesting when PyBot starts acting differently depending on the siutation. 

--- 

Consider the following scenario: 
> You are about to go to the grocery store. You ask your friend if she needs anything from the store, to which she responds: "If they have any Maracuja, get me some, please." 

Notice how your friend used a conditional instruction: **if** they have Maracuja, then you should buy her some Maracuja. Otherwise, you should buy nothing for her. 

When programming, we sometimes need to give conditional instructions to PyBot. For example, we might want to tell her: "If there is an orange in your cell, pick the orange." Using a conditional instruction is important here, because PyBot will crash if she attempts to pick an orange in a cell where there is no orange. 

<a class="anchor-offset" id="if-statements" href="#if-statements"></a>

# `if` Statements 
In Python, we can program a conditional instruction using an `if` statement. As an example, let's write the conditional instruction, "if there is an orange in your cell, pick the orange" in Python: 

_Python Code_
```python
if has_fruit(): 
    pick_fruit()
```

The code above will instruct PyBot to check if there is an orange in her cell, and if there is, to pick that fruit.

Let's learn the steps for writing `if` statements:
<img class="fig_if" src="figures/fig_if_example.png">
1. First, we start with the word `if` followed by a space.
2. Next, we write a PyBot condition function. Remember, using a PyBot conditions function is like asking a yes or no question to PyBot. 
3. Put a colon (i.e. `:`) after the condition to mark the beginning of the `if` statement.
4. Lastly, we write the instructions that PyBot should follow if the answer to the condition function is `True`. These instructions should be written under the condition function and should be indented in **one tab** relative to the word `if`. These instructions can be a list of action functions or, as we'll see later, other conditional statements and loops. 

Here's another `if` statement example. It could be useful to program PyBot to move only if she is not on the edge of the field – that she won't crash. We can write this conditional instruction using an `if` statement. 

_Python Code_
```python
if not front_is_blocked():
    move()
```

_Result_

<a class="anchor-offset" id="inverting" href="#inverting"></a>

## `not` – Inverting Conditions 

_Python Code_
```python
if not front_is_blocked():
    move()
```

_Result_

<a class="anchor-offset" id="else-elif" href="#else-elif"></a>

## `else` and  `elif`
Let's return for a moment to the scenario from before:
> You are about to go to the grocery store. You ask your friend if she needs anything from the store, except this time she responds "If they have any Maracuja, get me some, otherwise get me some mango. 



<a class="anchor-offset" id="nesting" href="#nesting"></a>

## Nesting Conditional Statements  

<a class="anchor-offset" id="combining-conditions" href="#combining-conditions"></a>

## Logical Operators – Combining Conditions
`and`

`or` 
