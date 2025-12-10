# Advent of Code 2025

Giving myself a crash course refresher on Python through Advent of code!

| Days | Part A | Part B |
| ---- | ------ | ------ |
|Day 1 |   ★ 	|    ★  |
|Day 2 |   ★ 	|    ★  |
|Day 3 |   ★ 	|    ★  |
|Day 4 |   ★ 	|    ★  |
|Day 5 |   ★ 	|    ★  |
|Day 6 |   ★ 	|    ★  |
|Day 7 |   ★ 	|    ★  |
|Day 8 |   ★ 	|    ★  |
|Day 9 |   ☆ 	|    ☆  |
|Day 10 |   ☆ 	|    ☆  |
|Day 11 |   ☆ 	|    ☆  |
|Day 12 |   ☆ 	|    ☆  |

## Setup
Each solution is contained within its own folders, and are writting assuming that everything is run from the root directory AdventOfCode2025.

## Logs

### Day 1
I'm really having a blast getting back in to Python! Some not too bad puzzles to start today off! The second solution was being slightly annoying to solve elegantly so I just ended up simulating an actual lock to deal with the edge cases where we go left but start on 0.

### Day 2
Today's was a really easy one for me! My solution isn't super efficient but python really makes things easy with everything that you can do with strings. I accidentally made a solution that solved part 2 before part 1 this time. I also figured out a more efficient solution for part 1 while bored at way the day after, so I'll probably go back and implement that when I have time.

### Day 3
The second part of this one was pretty tricky. I was mulling on the algorithm for a while at work until I realized I could implement a stack, and pop digits on or off as I went through the string left to right.

### Day 4
This was actually the easiest one for me yet, as I just employed a very similar method to one I used when I made a Conway's Game of Life simulation in Java a few years ago. I just read the input into a 2d array, and surrounded it with a "moat" of empty spaces so that I could check *all* the given inputs for adjacent rolls without having to do any error checking. I can definitely rewrite part 2 as a recursive function so I'll probably get around to that sometime when I get bored.

### Day 5
This one was a gentle reminder of the importance of not reading a billion things into memory if I don't need to. Once I realized that, part one was trivial. Part two took me a little longer to figure out, but once I realized I could just absorb overlapping ranges it wasn't too bad. This is one that I also want to come back and rewrite as a recursive algorithm.

### Day 6
Cephalod math was interesting to wrap my head around. Puzzle one was pretty easy once I learned the wonders of Python's zip function, but the second one had me stumped for a bit trying to figure out how to preserve the necessary whitespace, until I realized that the operator for each column directly followed the spacing column. That let me cleanly get indices to split on. I also realized that I had my old school email saved to my git credentials so none of the solutions I had been committing before today were being shown on my profile.

### Day 7
This one was really fun! The first part was really simple and fun to visualize. The second part gave me a rough dose of reality, and I went through 3 solutions before finally writing one that didn't take the life of the universe to finish. I got too caught up in writing a clever recursive function that I didn't realize how long that function would take to finish. In the end though, I went with a pretty clever (at least I'd like to think so) solution that runs in O(n) time.

### Day 8
I got off work today so I got to spend extra time working on my solutions, and boy did I need it. I had to basically relearn Union Find / Disjoint Set as I don't think I'd used it since my data structures class. I also got too excited about writing a custom class for my first solution that I built out a whole class and dictionary system before realizing that it didn't really help me. At least the second solution was relatively easy!
