# Activity 04: Expressions and Datatypes
![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=main) ![Points badge](../../blob/badges/.github/badges/points.svg)


Solve the following problems.

See https://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/2021/01/28/04_Python_1/ for help.

## Temperature conversion

Create a program `tempconverter.py` that asks the user to input a
temperature in degree Fahrenheit (θ) and prints the temperature in
Kelvin (T), according to the equation

          5
      T = - (θ - 32) + 273.15
          9

Your program should assign the temperature in Kelvin to a variable `T`.


## List indexing and slicing

Given the lists

     letters = ['A', 'B', 'C', 'D', 'E', 'F']
     temperatures = [60.1, 78.3, 98.8, 97.1, 101.3, 110.0] 

create a program `slices.py` that assigns to variables `a`, `b`, ... the following:

* a: extract the letter 'E' from `letters`
* b: extract the letters 'C', 'D' from `letters`
* c: extract the letters 'D', 'E' from `letters` (hint: use negative indices)
* d: find the length of `temperatures`
* e: extract the second-but last value from temperatures
* f: extract the last two values from `temperatures`
* g: reverse the order of `temperatures` (note the `step` argument of slicing!)

## List construction

Given an empty list `stuff` in a file `stuff.py`, perform the
following steps and print `stuff`.

1. append "dog"
2. append "mouse"
3. replace element 1 with 42
4. extend with list `[-1.234, "cat", [3, 2, 1]]`

Now

1. **copy** `stuff` to a list `more_stuff`
2. replace elements 1 and 2 with the list `['python', 'swallow']`
3. remove the last element and extend with the list `['Hund', 'Python', 'Schwalbe', 'Katze']`
4. insert at position 2 the list `['parrot', 'llama']`


