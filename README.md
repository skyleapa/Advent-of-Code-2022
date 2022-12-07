# 2022 Advent of Code 😎

## Day 1 - Calorie Counter
* `O(n)`
* A simple and fun introduction to AoC. At first struggled with getting Java to compile in VS Code, ended up switching to use python
## Day 2 - Rock Paper Scissors
* `O(n)`
* Originally tried to do with brute force comparisons in if statements. The next day, refactored solution to use a dictionary which made it much cleaner.
## Day 3 - Rucksack Reorganization
* `O(n)`
* Immediately jumped to a hashmap/dict solution, learned about ord() in python and ASCII characters. Getting used to using key/values for solutions. Could have come up with a better way to discern between 3 lines rather than an accumulator.?
## Day 4 - Camp Cleanup
* `O(n)` *chef's kiss*
* Thinking of arithmetic connections with the ranges, evaluated based on 3 cases in which pairs would overlap. Adjusted conditions for part 2
Let `a-b`,`c-d`
* Part 1:
if `a == c` or `b == d`, `pairsContained++`
if `a < c`, then if `d < b`, `pairsContained++`
if `a > c`, then if `d > b`, `pairsContained++`
* Part 2:
If `a == c` or `b == d`, `pairsContained++`
If `a < c`, then if `c <= b`, `pairsContained++`
If `a > c`, then if `d <= a`, `pairsContained++`
## Day 5 - Supply Stacks
* `O(n)`
* The most challenging day yet! I'm especially proud to have completed this entirely on my own in an unfamiliar language :) The objective itself was simple, but coding was complicated in parsing the text file data and looping through the correct indexes
* Learned about python regex, manipulating arrays, using python for loops, thinking about how to access extracting necessary data from txt file. Manipulated stackHolder array to modify stacks.
* For part 2, modified stackMover to use a while loop that kept track of the index position and iterated upwards
## Day 6 - Tuning Trouble
* `O(n)`
* A more clean solution than I expected. Had an oversight on removing the first element rather than all elements leading to the duplicate index. Part 2 was a variation of part 1 where checks when the length of the array is equal to the filled values and dictates a correct solution


