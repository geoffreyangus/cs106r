---
title: Conditional Statements 
---
We've learned how to instruct PyBot to take actions using functions like `move()`, `turn_right()`, and `pick_beeper()`. We've also learned how to combine these functions together to create our own functions – for example, we combined three `turn_right()` calls into one function called `turn_left()`. 

But up until now, we've only been giving PyBot a list of actions to take. Everytime we run a particular program, PyBot does the exact same thing. Things get interesting when PyBot starts acting differently depending on the siutation. 

--- 

Consider the following scenario: 
> You are about to go to the grocery store. You ask your friend if she needs anything from the store, to which she responds: "If they have any Maracuja, get me some, please." 

Notice how your friend used a conditional instruction: **if** they have Maracuja, then you should buy her some Maracuja. Otherwise, you should buy nothing for her. 

When programming PyBot, we sometimes need to give her conditional instructions. For example, we might want to tell her: "If there is an orange in your cell, pick the orange." Using a conditional instruction is important here, because PyBot will crash if she attempts to pick an orange in a cell where there is no orange. How do we do this in Python? We can program the conditional instruction, "if your current cell has a fruit, pick the fruit", using an `if` statement like this: 

_Python Code_
```python
if has_fruit(): 
    pick_fruit()
```

The code above will instruct PyBot to check if there is an orange in her cell, and if there is, to pick that fruit. Let's explore `if` statements in more detail. 

<a class="anchor-offset" id="if-statements" href="#if-statements"></a>

# `if` Statements 
In Python, we program conditional instruction using `if` statements. 

> `if` **Statement** – A section of code that should only be executed if a condition is `True`. 

Every `if` statement consists of  a condition (i.e. a _True_ or _False_ question, like the ones we can ask PyBot with the condition functions) and code to be executed if the condition is satisfied (i.e. the answer to the question is _True_). 

Let's learn the steps for writing `if` statements with PyBot:
<img class="fig_if" src="figures/fig_if_example.png">
1. First, we start with the word `if` followed by a space .
2. Next, we write a PyBot condition function (e.g. `has_fruit()`, `front_is_blocked()`). Remember, using a PyBot conditions function is like asking a yes or no question to PyBot.
3. Put a colon (i.e. `:`) after the condition to mark the beginning of the `if` statement.
4. Lastly, we write the code that PyBot should follow if the answer to the condition function is `True`. These instructions should be written under the condition function and should be indented in **one tab** relative to the word `if`. These instructions can be a list of action functions or, as we'll see later, other conditional statements and loops. 

In a way, `if` statements grant your program _decision making power_. Your program can now decide what to do based off the condition. 

<a class="anchor-offset" id="inverting" href="#inverting"></a>

## `not` – Inverting Conditions 
Here's another `if` statement example with PyBot. We want to program PyBot to move if she is not on the edge of the field, so that she won't ever crash.

We need to program the conditional instruction: "`if` the front is clear, move." PyBot can answer the question "is the front blocked?" with the `front_is_blocked()` function, but she cannot directly answer "is the front clear?". How then can we program this conditional instruction if we only have the opposite of the condition we'd like to check? 

Luckily, Python provides the keyword `not` which inverts any condition. For example, `not front_is_blocked()` asks the question "Is the front not blocked?" (i.e. is the front clear). Let's write the `if` statement for the conditional instruction: 

_Conditional Instruction_
> `if` the front is clear, move

_Python Code_
```python
if not front_is_blocked():
    move()
```

_Result_
<img class="fig_not" src="figures/fig_not.png">

In summary, `not` allows us to write `if` statements where code is executed if a condition is **not** satisfied.


<a class="anchor-offset" id="else-elif" href="#else-elif"></a>

## `else`
Let's return for a moment to the scenario from before:
> You are going to the grocery store. You ask your friend if she needs anything, except this time she responds "If they have any maracuja, get me some, otherwise get me mango." 

In this example, your friend has given you a conditional instruction with **2** possible courses of action: `if` there is Maracuja then you should (1) get her maracuja, `else` you should (2) get her mango. 

In Python, we can program conditional instructions with **2** possible courses of action by extending the `if` statement with an `else` statement. 
 
```python
if condition_function():
    action_function()
    action_function()
    ...
else:
    action_function()
    action_function()
    ...
```

## `elif`
Let's go back to  to the grocery store example one last time:

> You are about to go to the grocery store. You ask your friend if she needs anything from the store, to which she responds: "If they have any Maracuja, get me a Maracuja. Else, if they have Kiwis, get some of those. Otherwise, just get me Mango". 

Here, your friend has given you a conditional instruction with **3** possible courses of action. In Python, we can program conditional instructions with any number of  courses of action by extending the `if` statement with an `elif` statement. 

```python
if condition_function():
    action_function()
    action_function()
    ...
elif condition_function():
    action_function()
    action_function()
    ...
elif condition_function():
    action_function()
    action_function()
    ...
else:
    action_function()
    action_function()
    ...
```

Let's take a look at a PyBot example that uses an `if-elif-else` statement. We want to turn PyBot to face south. We'll need PyBot to take a different course of action depending on the direction she is facing initially. Let's start by writing out the conditional instruction in English. 

_Conditional Instruction_ 
>`If` PyBot is facing east, she should turn right once,  `else if` she is facing north, she should turn right twice, `else if` she is facing west, she should turn right thrice, `else` she should do nothing, since she was already facing south. 

_Python Code_ 
```python
if is_facing_east():
    turn_right()

elif is_facing_north():
    turn_right()
    turn_right()

elif is_facing_west():
    turn_right()
    turn_right()
    turn_right()

```

<a class="anchor-offset" id="nesting" href="#nesting"></a>

## Nesting Conditional Statements  
move 
<a class="anchor-offset" id="combining-conditions" href="#combining-conditions"></a>

## Logical Operators – Combining Conditions
Check the top row
`and`

`or` 

