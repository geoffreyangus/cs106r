---
title: Course Notes 
---

# Control Flow 
We've learned how to instruct PyBot to take actions using functions like `move()`, `turn_right()`, and `pick_beeper()`. We've also learned how to combine these functions together to create our own functions – for example, we combined three `turn_right()` calls into one function called `turn_left()`. 

But up until now, we've only been giving PyBot a list of actions to take. Everytime we run a particular program, PyBot does the exact same thing. Things get interesting when PyBot starts acting differently depending on the siutation. 

# Conditional Statements 
Consider the following scenario: 
> You are about to go to the grocery store. You ask your friend if she needs anything from the store, to which she responds: "If they have any Maracuja, get me some, please." 

Notice how your friend used a conditional instruction: **if** they have Maracuja, then you should buy her some Maracuja. Otherwise, you should buy nothing for her. 

When programming, we sometimes need to give conditional instructions to PyBot. For example, we might want to tell her: "If there is an orange in your cell, pick the orange." Using a conditional instruction is important here, because PyBot will crash if she attempts to pick an orange in a cell where there is no orange. 

## `if` Statements 
In Python, we can program a conditional instruction using an `if` statement. Let's write the conditional instruction, "if there is an orange in your cell, pick the orange" in Python: 

_Python Code_
```python
if has_fruit(): 
    pick_fruit()
```

The code above will . Let's learn how to write `if` statements:
```python
if condition_function(): 
    action_function()
    action_function()
    ...
```

1. First, we start the word `if` followe by a space
2. Next, we call a PyBot condition function. Remember, using a PyBot conditions function is like asking a yes or no question to PyBot. 
3. Put a colon (i.e. `:`) after the condition.
4. Write the  are like  The condition should be some

In general, we write conditional instructi


## `else` and  `elif`
Let's return for a moment to the scenario from before:
> You are about to go to the grocery store. You ask your friend if she needs anything from the store, except this time she responds "If they have any Maracuja, get me some, otherwise get me some mango. 

you can nest

## Nesting Conditional Statements  

# Inverting Conditions 
`not` 

## Combining Conditions
`and`

`or` 



# Loops 

##

