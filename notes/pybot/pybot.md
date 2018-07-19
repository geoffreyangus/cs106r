---
title: Course Notes 
---

## Introducing PyBot and PyCountry
<img class="bio-pic" align="right" width="75" height="75" src="figures/fig_pybot.png">
For the first week of the course, we're going to be working with a virtual robot name `PyBot`. We'll teach you some important Python concepts, and you will use those concepts to program PyBot. (PyBot is based very closely on Karel the Robot, a virtual robot that students work with in Stanford's introductory computer science course.)

This is PyBot on the right. She is a simple robot that lives in PyCountry, a land renown for its oranges (it said that an orange from PyCountry is easier to peel than any orange in the world). 

## PyCountry Fields 
The oranges in PyCountry grow in rectangular fields, like the ones shown below. 

TODO: Insert fields

Each field has 25 **cells** arranged in a 5x5 grid. In each cell there is:
1. An **orange plant**  where an orange can grow. If there is an orange hanging from the plant then you'll see an orange: 🍊. Otherwise, if there is no orange, you'll just see the seedling: 🌱
2. A **path** where PyBot can stand. Path's are just a black square: ◾️.

The four sides of a PyCountry field are labeled with the cardinal directions: _north, east, south_ and _west_. 

## PyBot

PyBot spends all of her time hanging out in PyCountry's orange fields. At all times:
1. PyBot is standing in one **cell** on the field
2. PyBot is facing the **direction** indicated by her arrow.

PyBot was built to perform only a small set of actions: she can move in the direction she is facing, turn herself 90 degrees to the right, and pick the orange in her cell if there is one. To get PyBot to do more complicated tasks, we'll need to program her in Python using PyBot functions. 

## PyBot Functions
### Commands
**Commands**   We can program PyBot to perform a few simple actions by calling the following Python functions:
<img class="bio-pic" src="figures/fig_pick_fruit.png" width="750">

1. `move()` - PyBot takes one step in the direction she is facing.
2. `turn_right()` - PyBot turns herself 90 degrees to the right
3. `pick_fruit()` - PyBot picks the fruit in its current cell.



**Conditions  
1. `front_is_blocked()` - PyBot takes one step in the direction she is facing.
2. `has_fruit()` -
3. `is_facing_east()`, `is_facing_north()`, `is_facing_west()`, `is_facing_south()` - 

## PyBot Conditions


### PyBot Functions 

`move()` Move PyBot one cell in the direction she is facing. 
Example: 
    