# LeetCode Problem Solution Notes/Thoughts
 Wrote by Taylor Gibbons with the intent to practice coding concepts

# Problems in numerical order:
## 1. twoSum Problem:
**[TASK]** In this problem, the task is to find the indices of a list that will sum to a target number. For example:  `nums = [2,7,11,15]` and `target = 9`. The resulting output will be `soln = [0,1]` because those correspond to the numbers 2 and 7, which sum up to 9.

**[PROCESS]** The first thing that came to mind when dealing with this problem is how I would go along solving it as a math problem. Intuitively, I would go from the first element, add it with the second, see if it is equal to the target, and if not, then move to the next element, where the first element is now added with the third, then checked and repeated. Then if the first and last elements do not match, it moves to checking if the second value added with any of the other values equals target, and thus continues. To put this into code, I made two `for` loops where the first loop is the initial value that will be added to the others, and the inner loop is the loop running through the rest of the values. Then it would check to see if the sum is equal to the target. If it were equal, it would break the loops and return the indices; if not equal, it would run the loop again with the initial value moved over one. 

## 2. addTwoNumbers Problem:
**[TASK]** In this problem, the task is to take two linked lists (that are backward), add the numbers (as integers) to each other, and then separate back into a list of numbers. For example: `l1 = [2,4,3], l2 = [5,6,4]` and the output would be `soln = [7,0,8]` because the integer reversed is `342 + 465 = 807`, then reversed again. 

**[PROCESS]** This problem didn't seem to difficult to me due to some of the list operations that could be used. The first thing that I thought of was using the `.reverse()` function to reverse the lists, then use `''.join()` to combine the integers in the list together. However, using just the join function did not work and I had to figure out a way to fix this. This was done by looking into the join function and finding out that since the elements in the list are integers, they will not be joined together since it looks for strings. To get around this, I found a way to go through each index of the list, turning it into a string, combining it, then returning the combined string into an integer; `int(''.join([str(i) for i in l1]))`. This resulted in the list elements being a combined integer, which then could be added to the other list's integer. From there, the newly made list is separated into a list and reversed.

This is about the time that I ended up realizing that I messed up and was thinking that the problem was dealing with lists, not ListNodes. So the original code that I had made does not work for the actual problem. This made it a bit more difficult since I am not used to linked lists and this would be a bit of a learning curve for me. Thus I took this as a sign to work on a linked list tutorial and eventually try to figure out the problem. Thus, this problem is still being worked on while I am working on other problems.

## 3. lengthOfLongestSubstring Problem:
**[TASK]** In this problem, the task is to find the length of the longest substring, of a larger string, without having any repeated letters. For example: `s = "abcabcbb"` will result with `num = 3` since the longest substring without a repeat is `"abc"`.

**[PROCESS]** When planning out how I was going to tackle this problem, I decided to try to think of it logically. If I had the function start with the first letter of the string, then check to make sure that the next letter in the string, has not been already added. If it has been added, it will take note of the length of the temp string, then restart by adding the next string letter and checking. To better show my thinking about this problem, I made a simple flowchart: 
![alt Text]([https://github.com/](https://github.com/taygibbs/LeetCode_Problems/edit/main/Flowcharts/Porblem3FC.png))



## 88. mergeSortedArrays Problem
