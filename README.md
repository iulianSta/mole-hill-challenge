# A mountain of a mole hill

## Problem

Moles have infested a 16x16 area.
The fences of your gardens are outlined on maps with |, + and - symbols.
The mole hills are represented by a lower-case o.
How many mole hills are in your gardens?

- Two parallel fences of the garden cannot touch (it wouldn't make sense).
- Garden space is filled with white space unless there is a mole hill. Other space is filled with dots unless there is a mole hill.
- Everything that touches the outside of the map and is not enclosed in fences is other space. A fence is always between garden space and other space.
- Mole hills cannot be on fences.

## Example

### Input
<pre>
................\
................\
..+----------+..\
..|          |..\
..|   o      |..\
..|      o   |..\
..|          |..\
..+----------+..\
................\
............o...\
.....o..........\
................\
.........o......\
................\
................\
................\
</pre>

### Output
2

## Explanation

The answer is in the answer.py file.

- The code starts by declaring a variable called S. It then declares an integer called answer and sets it to 0.
- Next, the code creates two strings: L and L0.
- The first string is created with the input() function and contains all of the spaces in the string "S".
- The second string is created with enumerate() and contains all of the characters in "L" except for any spaces or commas that may be present at either end of each character.

- The next line inside = False; this means that if there are no more loops left, then we're done looping through our list (the list being our string).
- Then, for j from 0 to len(L) - 1:

- If c == '|' or (c == '+' and L0[j] in '|+'): inside = not inside

- This means that if there's a space on either side of a + sign, then we check whether or not this character is part of another word like o-n-d-e-x-t-.
- If so, then we add one to answer because it's now true that there was an extra word before ondext.
–
- The code will print the answer to the user.
