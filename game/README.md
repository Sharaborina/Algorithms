In this game a player sets balls of different colors in a line. 
When a continuous block of three or more balls of the same color is formed, it is removed from the line. 
In this case, all the balls are shifted to each other, and the situation may be repeated.

This function determines how many balls will be destroyed. 
There can be at most one continuous block of three or more same-colored balls at the initial moment.

**Input data:**

The function takes a list with initial balls disposition. Balls number is less or equals 1000, balls colors can be from 0 to 9, each color has its own integer.

**Output data:**

The function has to return one number - the number of the balls that will be destroyed.

**Example:**

Input: [2, 2, 1, 1, 1, 2, 1]

Output: 6
