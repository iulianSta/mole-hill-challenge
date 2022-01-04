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

# Example

# Input
................ /
................ /
..+----------+..
..|          |..
..|   o      |..
..|      o   |..
..|          |..
..+----------+..
................
............o...
.....o..........
................
.........o......
................
................
................

# Output
2
