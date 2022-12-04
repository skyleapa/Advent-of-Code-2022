# Adventures of Coding with Michelle and Darryl 😎

## Day 1 - Calorie Counter
* `O(n)`
* This coding question was pretty fun; we struggled with getting Java to compile in VS Code, but decided to switch to Python and it instantly made life easier!
## Day 2 - Rock Paper Scissors
* `O(n)`
* Originally tried to do with brute force comparisons in if statements. The next day, refactored solution to use a dictionary which made it much cleaner.
## Day 3 - Rucksack Reorganization
* `O(n)`
* Immediately jumped to a hashmap/dict solution, learned about ord() in python and ASCII characters. Getting used to using key/values for solutions. Could have come up with a better way to discern between 3 lines rather than an accumulator.?
## Day 4
* `O(n)` *chef's kiss*
* Thinking of arithmetic connections with the ranges, evaluated based on 3 cases in which pairs would overlap. Adjusted conditions for part 2
* Part 1:
Let `a-b`,`c-d`
if `a == c` or `b == d`, `pairsContained++`
if `a < c`, then if `d < b`, `pairsContained++`
if `a > c`, then if `d > b`, `pairsContained++`
* Part 2:
If `a == c` or `b == d`, `pairsContained++`
If `a < c`, then if `c <= b`, `pairsContained++`
If `a>c`, then if `d <= a`, `pairsContained++`


