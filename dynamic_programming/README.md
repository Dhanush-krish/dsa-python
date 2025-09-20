#### Dynamic Programming
* overlapping subproblems
* optimal substructure
#### two ways to implement a DP algorithm:
* Bottom-up, also known as tabulation. implemented with a recursive function and hash map
* Top-down, also known as memoization.  bottom-up is implemented with nested for loops and an array.

#### The FrameworkTo solve a DP problem, we need to combine 3 things:

1. A function or data structure that will compute/contain the answer to the problem for every given state
2. A recurrence relation to transition between states.
3. Base cases, so that our recurrence relation doesn't go on infinitely.

#### When to Use DP
##### The first characteristic
* What is the minimum cost of doing...
* What is the maximum profit from...
* How many ways are there to do...
* What is the longest possible...
* Is it possible to reach a certain point...

##### The second characteristic
* future "decisions" depend on earlier decisions.

#### For any problem:

**Choices** → what moves/actions can I take?

**State** → what information uniquely defines a subproblem?

**Transition** → how do smaller states combine into the larger one?

**Base Case** → what’s the simplest answer I know immediately?

**Answer** → what state(s) give me the final solution?




### reference
*   https://leetcode.com/discuss/general-discussion/662866/Dynamic-Programming-for-Practice-Problems-Patterns-and-Sample-Solutions