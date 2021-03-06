# Coconut-Math-Problem
A solution process for an extra-credit problem in college algebra written in python.

# Explaination
This Progam is designed to solve the following problem:

Five men and a monkey were shipwrecked on an island. They spent the first night gathering coconuts. During the night, one man woke up and decided to take his share of the coconuts. He divided them into five piles. One coconut was left over so he gave it to the monkey, then hid his share and went back to sleep.
Each of the five men did this over the course of the night. What is the smallest number of coconuts in the original pile?


This variation of the program is different from most, as the men do not divide the remaining pile in the morning. Because of this, we can determine that the smallest amount remaining in the morning can be 4 (The last man divides a pile of six into five groups of one, gives one to a monkey,and hides his own). In order for the process to repeat, each man ends with a remaining pile that is a multiple of 4. From this, we can assume that the remaining amount in the morning will always be a multiple of 4. This is used to improve program efficency by only trying multiples of 4 by using a base of 4 and increasing a multiplier for every iteration. The process is then solved in reverse order (Combining 5 piles, adding one from the monkey) five times, one for each man. To test if a solution is valid, the values are tested for remainders. If a remainder is found, the solution is considered invalid and the next multiple is tested.

Using this program, the solution can be found in 0.0006961822509765625 seconds

This method determines solutions at a rate of 580 solutions per second (5800 in 10 second)