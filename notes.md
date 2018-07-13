---
title: Course Notes 
---
Hiya! Welcome to the course notes for CS 106R. On this page, you'll find all of the material we'll cover in the class. We designed these course notes to be as lightweight as possible – that is, they will cover all the essentials but won't dive into material too deeply. Throughout you will find links to external resources we've found helpful in understanding concepts. 

---
## What is Computer Science? 
When you hear the words "computer science", what comes to mind? Do you think of computer programming – neon text on a black screen? Do you think of algorithms and equations scribbled on a whiteboard? Perhaps, when you hear "computer science", you think of computer and phone applications, websites and video games: WhatsApp, FIFA 18, PhotoShop. Maybe you think of computers that [drive](https://www.technologyreview.com/s/609450/autonomous-vehicles-are-you-ready-for-the-new-ride/), [beat us at board games](https://www.nytimes.com/2017/05/23/business/google-deepmind-alphago-go-champion-defeat.html) and [make sense of language](https://www.washingtonpost.com/business/economy/ais-ability-to-read-hailed-as-historical-milestone-but-computers-arent-quite-there/2018/01/16/04638f2e-faf6-11e7-a46b-a3614530bd87_story.html?noredirect=on&utm_term=.285b937ed479). Maybe you've seen the power of [molecular dynamics simulation](https://www.youtube.com/watch?v=5JcFgj2gHx8) and you think of biology or chemistry. Or when you hear computer science you think of art – personally, I often think of [this Pixar short](https://www.youtube.com/watch?v=lkQTe0Wdo2k) and marvel at the unbelieavable computer rendering of the ocean – or [music](https://vimeo.com/100624271) made by instruments that could only be forged with code. Maybe you think of [goal line technology](https://football-technology.fifa.com/en/standards/goal-line-technology/), applications that track your fitness, or [statistical models](https://projects.fivethirtyeight.com/2018-world-cup-predictions/) that predict the outcomes of football tournaments. Perhaps you're concerned about all the personal information that you hand over to Facebook and you think of the recent [Facebook-Cambridge Analytica fiasco](https://www.nytimes.com/2018/03/19/technology/facebook-cambridge-analytica-explained.html). When you hear computer science you might think of the [economic implications of automation](https://economics.stanford.edu/sites/default/files/april11.pdf) and its impact on inequality. Or maybe, when someone says computer science you don't really think of anything at all. The thing is, computer science is not one of these things more than any another – it is all of them and much more. 

Simply put, computer science is **the art of using computers to solve problems**. Computers can be used to solve a remarkably diverse set of problems, and that is why the visions of computer science listed above are so varied. The bottom line is: if we are getting a computer to solve a problem that it couldn't before, then we are practicing computer science – it doesn't matter what that problem is. So, as you begin this course, we'd recommend that you don't dwell too much on preconceived notions of what you think computer science is or isnt. Rather, come with an open mind and along the way consider: what problems would I like a computer to solve? 

## What is a Computer and what is Computer Programming? 
Computers come in many forms. If you're reading these notes on a laptop, you are, of course, using a computer. If you're reading on a smartphone, you are using a computer as well. Computers can be large and powerful, like [IBM's Summit supercomputer](https://techcrunch.com/2018/06/08/ibms-new-summit-supercomputer-for-the-doe-delivers-200-petaflops/), or very small and specialized, like the computer in a [pacemaker](https://www.nhlbi.nih.gov/node/3465). Computers can be old: [Ada Lovelace](https://www.nytimes.com/interactive/2018/obituaries/overlooked-ada-lovelace.html) was the first to program a – she did so in 1837. Computers show up in places you might not expect them: microwave ovens, digital watches, traffic lights, microscopes, and MRI machines all have computers embedded inside them. So what ties all of these machines together? What makes them **computers**? 

Computers are **programmable** machines – without changing their physical design, they can perform new tasks by following written instructions. A **computer program** is a set of instructions for a computer. Computers consist of a few basic physical components that allow them to do four simple things:
1. Accept information as input

   We input information into our computers through our keyboard. We can also input information with a camera or microphone. With an internet connection, a computer can receive input from other computers. 
   
2. Store information (in memory)
   


3. Process information (

4. Output information
   A computer shows us information through the computer screen or speakers. Computers also output information to other computers via the internet. 
   
   
Furthermore, computers store, process and output information according to the written instructions they are given.  A machine is **programmable** if it can follow written instructions. 

computer program is a set of written instructions for a computer are called a computer program  very   programmed to process information   historian of Computer programming is an important part of computer science, **but**, computer programming is only part of the work of a computer scientist more computer science than writing is  

## Introduction to Python 

<iframe frameborder="0" width="100%" height="600px" src="https://repl.it/student_embed/assignment/1211151/65629c184c91c55555e68086ece937d5"></iframe>

## Simple Functions
How do we get Python to If we want to print something we can call print(). 

## Basic Types 
Learning Objectives
1. Show them the python interpreter
2. Get them comfortable with the interpreter
    a. Show them `control + C` and `control  + D`
3. Get them comfortable with floats, integers, booleans, and strings

### Variables

The fundamental building block of all programming languages is the *variable*. **A _variable_ is a word that stores a value.** Here are some examples of some variables and how they are used:

```python
x = 5
y = 4

z = x + y
```

Here, `x`, `y`, and `z` are all examples of variables.

### Types
There are four fundamental variable types in Python:

1. Integer
2. Float
3. String
4. Boolean

We will get into the definitions of these words below.

##### Integers

An _integer_ is a whole number...

```python
numPatients = 5
count = 0
```

##### Floats

A float a number that has decimal values...

They are initialized like integers, except with the addition of the decimal point and numbers that follow.

```python
volumeLevel = 0.93
totalScore = 100.0
```

##### Strings

Strings are _strings_ of characters of any kind. Look at the following examples:

```python
sentence1 = 'CS106R is awesome!'
emailDomain = '@gmail.com'
jerseyNumber = '9'
```

Here, `sentence1`, `emailDomain`, and `jerseyNumber` are all examples of Strings. Notice that a number can be a string.

##### Boolean

Booleans are variables that represent True or False values.

_Why not use strings that say "True" or "False" instead?_

We use booleans because they take up less space in the computer. Instead of storing a string of characters, we can store a 0 for a False value, and a 1 for a True value.

```python
isGirl = True
isBoy = False
```

Now that we have gone through the different variables, let us talk about the operators...

### Operators

##### Arithmetic Operators

1. `**`
2. `*` or `/`
3. `+` or `-`

##### Boolean Operators

- `==`
- `!=`
- `>`
- `>=`
- `<`
- `<=`
