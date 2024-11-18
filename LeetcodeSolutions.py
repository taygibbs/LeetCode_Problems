# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:31:27 2024

@author: Taylor


This is a set of code that I am writing to work with the LeetCode problems.
"""
import numpy as np
import functools as ft
from collections import defaultdict

class ListNode: #for use in problem 2
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


#Start of the functions that I have made to help with selecting a problem or getting stats


#Problem 88:
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

def MergeSortedArray(nums1: list[int], m: int, nums2: list[int], n: int):
    """
    Does not retrun anything, modify nums1 instead. 
    """
    '''
    
    Everything below this is code that I had made originally, but did not work with the cases
    where n = 0 or m = 0, so I removed and changed the rest of the code to work without worrying about it. 
    
    #nums1 & 2 are both sorted ascending
    #m is the number of elements that should be merged
    #n is the length of nums1 input
    #First attempt
    # if n == 0:
    #     print('Case where n = 0:')
    #     nums1 = nums1[:m-1]
    # elif m == 0:
    #     print('Case where m = 0:')
    #     nums1 = nums2[:n-1]
    
    #else: 
      '''  
    mdx = m - 1 #Last index of nums1 that will be sorted
    ndx = n - 1 #Last index of nums2 that will be sorted
    end = m + n - 1 #The last index of the list that will be merged/sorted
    
    
    #In the leetcode problem, there was some sort of bug or reason that it would always return the wrong list if m = 0, so this is how I fixed that:
    if m == 0:
        for i in range(len(nums2)):
            nums1[i] = nums2[i]
    if n == 0:
        return nums1
    
    else:    
        while ndx >= 0 and end >= 0: #Making sure that if there is 0's in either m or n, then it will prevent infinite looping
        
            # print(f'mdx = {mdx}     nums1[mdx] = {nums1[mdx]}')
            # print(f'ndx = {ndx}     nums2[ndx] = {nums2[ndx]}')
            # print('---------------------------------------------')
        
        
            if mdx >= 0 and nums1[mdx] > nums2[ndx]: #While the 
                
                nums1[end] = nums1[mdx]
                nums1[mdx] = 0
                mdx -= 1 
            
            elif mdx >= 0 and nums1[mdx] <= nums2[ndx]:
                
                nums1[end] = nums2[ndx]
                ndx -= 1
                
            elif mdx < 0 and ndx >= 0:
                
                 nums1[end] = nums2[ndx]
                 ndx -= 1
            
            end -= 1            
             
    return nums1
                    
    #print(f"Merged nums1: {nums1}")


#Problem 1
""" CAN BE REDONE USING THE TWO POINTER PATTERN
"""
def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Submitted/Accepted with 3977 ms runtime (beating 5%) with 17.22mb of memory (beating 90.42%)
 
    
     inputs a list, we have to find the solution to which two of the elements of the list
     will add up to the target
     
     index = 0 #the currently looked at index
     soln = [] #will be two elements long
     for i in range(len(nums)):
          #print(i)
          for k in range(len(nums)):
              if i <= k:
                  continue
             
              if nums[i] + nums[k] == target:
                  soln.append(i)
                  soln.append(k)
                  break
          if len(soln) ==  2:
             break     
    
      #Retrying this problem by using the hashmap pattern
     """
    numMap = {} #creates a dictionary that will hold the elements and the index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in numMap:
            return [numMap[diff],i]
        numMap[num] = i
    return []
        

    
#Problem 2:
#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
            
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """ The code below is my first attempt at the problem. However, while running the code in the leetcode editor and running it, I realized that
        this code would not work due to my using of list, and not listNode (because for some reason my IDE doesn't like it...')
    l1.reverse()
    l2.reverse()
    print(f"l1 Reversed: {l1} \nl2 Reversed: {l2}")
    l1_num = int(''.join([str(i) for i in l1]))
    l2_num = int(''.join([str(i) for i in l2]))
    l3 = l1_num + l2_num
    l3 = [int(i) for i in str(l3)]
    l3.reverse()
    return l3
    """
    dummy = ListNode()
    result = dummy
    
    total = carry = 0
    
    while l1 != None or l2 != None or carry != None: #Only continues if the lists are nonempty
        
        total = carry 
        
        if l1:
            total += l1.val
            l1 = l1.next
            
        if l2:
            total += l2.val
            l2 = l2.next
            
        num = total % 10
        carry = total
        dummy.next = ListNode(num)
        dummy = dummy.next
            
    return result.next


#Problem 3: Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s: str) -> int:
    #Find the longest substring without repeating characters
    """   
    #First Attempt is a bit of a brute force. I got some examples to work, but not many. maybe 1/3
    
    m = len(s)
    
    temp = ''
    soln = ''
    repeat = True #the way to check if the string needs to restart
    
    for i in range(m):
        print(f'Running i = {i}')
        if i == 0 or repeat == True: #
            print('Initial/Restart')
            temp += s[i]
            
            repeat = False
            continue
        
        for k in temp: #Checking to see if the currently looked at letter has been seen in the current temp string
            print('Checking if there is a repeat')
            if k == s[i] or i == m: #If one of the letters is the currently looked at letter, or at the end of the og string
                print(f'k = {k}    s[i] = {s[i]}')
                repeat = True #The letter has been repeated
                break
           
        
        if i > 0 and repeat == True:
            if len(temp) > len(soln) and len(temp) > 1:
                soln = temp
                temp = '' + s[i]
        elif repeat == False:
            temp += s[i]
            
    #print(soln)
    return len(soln)
    """
    
    
    #The second attempt of this problem was more researched and was decided to work on a solution called the 
    #sliding window 
    
    start = 0 # Windows starting index
    end = 0 #windows ending index
    temp = {}
    longest = 0
    
    for end in range(len(s)):
        current = s[end] #Using the end index because itll be the newest letter to be checked.
        start = max(start, temp.get(current,0)) #This will keep start at the same index if the letter has not been seen, but move to the 
                                            # start index to the end in order to start a new window
        longest = max(longest, end - start + 1) #checks the lengths of the window
        
        temp[current] = end + 1
    
    return longest

#Problem #4: Median of Two Sorted Arrays
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    
    if len(nums1) > len(nums2):
        for i in nums2:
            nums1.append(i)
            
        merged = nums1
    else:
        for i in nums1:
           nums2.append(i)
    
        merged = nums2
    merged.sort()    
    size = len(merged)
    if size % 2 == 0: #even number of elements, thus median is the middle two elements added and divided by 2
        mid_ind = size // 2 
        soln = (merged[mid_ind - 1] + merged[mid_ind])/2
    else:
        soln = float(merged[size //2]) #odd number of elements, thus median is the very middle element

    return soln

#Problem #5: Longest Palindromic Substring
def longestPalindrome(s: str) -> str:
    
    #checking to see if string is a palindrome
    reverse = s
    reverse.reverse()
    
    if reverse == s:
        print('Palindrome')
        
#6 ZigZag Conversion
def convertZigZag(s: str, numRows: int)-> str:
    def addingListString(nums: list) -> str:
        new = ''
        for i in nums:
            for j in i:
                new += j
            return new
        
    if numRows == 1:
        return s    
    new_s = [[] for _ in range(numRows)]
    print(new_s)
    direction = 1
    index :int = 0
    
    for i in s:
        print(f'Index: {index}')
        new_s[index].append(i)
        print(f'new_s: {new_s}')
        
        
        
        if index == 0:
            direction = 1 
        elif index == numRows - 1: #the final list
            direction = -1
            
        index += direction
    return addingListString(new_s)        
        
#Problem #7 ReverseInteger
def reverse(x:int) -> int:
    
        negative = False
        temp = [str(i) for i in str(x)]

        if temp[0] == '-':
            negative = True
            temp = temp[1:]
        
        temp.reverse()
        soln = int(''.join([str(i) for i in temp]))

        if negative == True:
            soln = -1 * soln
        
        
        if -2 ** 31 >= soln or (2 ** 31) -1 <= soln:
            soln = 0
        

        return soln

#Problem 8: StringToInteger(atoi)
def myAtoi(s: str) -> int:
    
    temp = ''
    neg = False
    num = 0
    for end in range(len(s)):
        current = s[end]

        match current:
            case ' ' | '+' :
                if len(temp) == 0:
                    continue
                else:
                    break
            case '-':
                if len(temp) == 0:
                    neg = True
                    continue
                else:
                    break
        if end > 0 and current == ('-' or  '+') and s[end - 1] == ('+' or '-'):
            break
        
        try:
            int(current)
        except:
            break
        else:
            temp += current

    if len(temp) > 0:
        num = int(temp)
        if neg == True:
            num = -1 * num

    if num < -2**31:
        num = -2**31
    elif num > 2**31 - 1:
        num = 2**31 - 1
    return num
            
#26
def removeDuplicates(nums: list[int]) -> int: #Using a two pointer system
    n = 1 #starting with 2nd element to look at the previous element
    for i in range(1,len(nums)): 
        if nums[i] != nums[i-1]: #checks for unique values
            nums[n] = nums[i] #Overwrites duplicated values based on the value of n
            n += 1
    return n, nums[:n]

#Determines if a number is a palindrome 
def isPalindrome(x: int) -> bool:
    num = str(x)
    m, n = 0, len(num) - 1
    for i in range(len(num)//2):
        if num[m] != num[n]:
            return False
        else:
            m += 1
            n -= 1
    return True

#Problem 1093. Statistics From a Large Sample

def sampleStats(count: list[int]) -> list[float]:
    '''This set of code is WAY to expensive to run on lists with a LARGE amount of numbers. Ie, all the memory will be used up due to the list getting WAY TOO LARGE
    #Count is the amount of times the number corresponding with the index is found in the larger array/list:
        #ie: count = [0,1,2,3] means og_list = [1,22,333]
    
    temp = [] #temp list for finding the original list
    soln = [] #list corresponding to the soln[0] = min, soln[1] = max, soln[2] = mean, soln[3] = median, soln[4] = mode
    list_sum = 0
    max_ind = count.index(max(count))
    #filling temp list with the og data, though, this method is going to be pretty slow for large lists
    for i in range(len(count)):
        if count[i] > 0:
            for k in range(count[i]):
                temp.append(i)
                list_sum += i
    #Finished filling temp list
    
    
    soln.append(float(min(temp)))
    soln.append(float(max(temp)))
    soln.append(float(list_sum / len(temp)))
    soln.append(findMedianSortedArrays(temp, []))
    soln.append(count[max_ind] - 1)
    
    return soln '''

    non_zero = [i for i, val in enumerate(count) if val != 0]    #gives a list of indexes of non-zero elements
    
    min_val = non_zero[0]
    max_val = non_zero[-1]
    
    mode_ind = count.index(max(count)) #Mode value

    mean = 0
    for i in range(len(count)):
        
        mean += (i * count[i])
        
    mean = mean / sum(count)
    
    #Found a way to work with medians of count representing an og list through the solutions of the leetcode problem: https://leetcode.com/problems/statistics-from-a-large-sample/solutions/5683672/python-solution
    median = 0
    total = sum(count)
    if total % 2 == 1: #odd number of elements
        mid = (total + 1) // 2 #the number halfway of count + 1
        for i in range(len(count)):
            if mid > count[i]: 
                mid -= count[i]
            else:
                median = i
                break
        
        
    else: #Even case
        mid1 = 0
        mid2 = 0
        mid = total // 2 + 1
        
        for i in range(len(count)):
            if mid > count[i]:
                mid -= count[i]
            else:
                mid1 = i
                break
        
        mid = total // 2
        
        for i in range(len(count)):
            if mid > count[i]:
                mid -= count[i]
            else:
                mid2 = i
                break
        median = ( mid1 + mid2 ) / 2
    
    return [min_val, max_val, mean, median, mode_ind]

#problem 30. Substring with Concatenation of all words.I am using this problem to start getting used to Sets and how they work
def findSubstring(s: str, words = list[str]) -> list[int]:
    #This function 
    print('Work in Progress')

#problem 55. Jump Game
def canJump(nums: list[int]) -> int:
    """
    The best explanation for this problem was making an analogy to having to drive a certain distance with only a limited amount of gas (represented by the value in each element of the list).
    The basic idea was that to get to the goal, the car needs a certain amount of gas, so the car will start with the first index's amount of gas, move to the next index, if its value is larger than the current number in the gas, then it would replace
    and continue moving until the goal has been reached (if it can)
    """
    curr_jumps = 0
    
    for i in nums:
        if curr_jumps < 0: # the case in which there are no more available jumps
            return False #cannot make it to the end
        elif i > curr_jumps:
            curr_jumps = i
        curr_jumps -= 1
    return True
#Problem 59
def generateMatrix(n: int) -> list[list[int]]:
    #The idea behind this one is to go through the 4 different 'directions' that we have to fill the matrix up with. 
    #So, the first thing is set the outer edges of the matrix then move the edges inwards when the row/column has been filled. 
    #We start with the top row, fill in with the first n numbers, then move the top row index down (+1), then have the right side filled and moved left one (-1), then bottom filled and moved up one (-1)
    #   then left side filed, and moved over one (+1). Then this repeats until the n**2 has been hit.
    
    
    matrix = [[0] * n for _ in range(n)] #two dimensional list 
    
    top = 0 #top row index
    bottom = n - 1 #bottom row index
    
    left = 0 #left column index
    right = n - 1 #right column index
    
    
    curr = 1 #number being put into the matrix
    

    while curr <= n ** 2: #while the current number being put into the matrix is less than the square
            
        for i in range(left, right + 1): #filling in the top row, left to right
            matrix[top][i] = curr
            curr += 1
        top += 1
        
        for j in range(top, bottom +1): #filling the far right column, top to bottom
            matrix[j][right] = curr
            curr += 1
        right -= 1
        
        for i in range(right, left -1, -1): #Filling the bottom row, right to left (decrimenting by one)
            matrix[bottom][i] = curr
            curr += 1
        bottom -= 1
        
        for j in range(bottom, top - 1, -1): #fillin in the far left row, bottom to top
            matrix[j][left] = curr
            curr += 1
        left += 1
            
    return matrix
    
#Problem 168: Excel Sheet Column Title based on a column number 
def convertToTitle(columnNumber: int) -> str:
    title = '' #solution String
    while columnNumber > 0: #As long as column number is not 0
        remainder = (columnNumber-1) % 26 #finds the remainder of columnNum /26 to see how many in the second letter place. Takes into account the use of array index syntax
        title += chr(ord('A') + remainder) #Finds the letter based on the starting 'A' and how many is in the remainder. Ie, if remainder = 3, then title adds ('A' + 3) = 'D'
        columnNumber = (columnNumber - 1) // 26 #resets the column number to find the first letter place. So itll end up with a title put first place first, then second
        
    return title[::-1]
        
#Problem 1590. Make Sum Divisible by P
def minSubarray(nums: list[int],p: int) -> int:
    """
    Takes in a list of integers and an integer. The task is to make the sum of the array divisable by the number p.
    """
    remMap = {} #defines a dictionary for remembering the remainders
    tot = sum(nums)
    length = len(nums)
    pre_sum = 0
    target_remainder = tot % p
    if target_remainder == 0:
        return 0
    
    for i, num in enumerate(nums):
        pre_sum = (pre_sum + num) % p
        current_remainder = (pre_sum - target_remainder) % p
        
        if current_remainder in remMap:
            length = min(length, i - remMap[current_remainder])
        
        remMap[pre_sum] = i

    return length

#2463
def minimumTotalDistance(robot: list[int], factory: list[list[int]]) -> int:
    
    """
    This is the submission I made, however was not working completely
    """
    '''
    print(f'Input: Robot: {robot}  Factory: {factory}')
    
    fact_pos = []    
    #[[limit],[number of robots in factory]]. 
    #Index within each list is the corresponding factory. ie position lim[0][0] corresponds to # of robots in fact lim[1][0]
    
    fact = {}
    
    
    #separates the factory positions with the limits into a dictionary with all information including current robots in factory
    for f in factory:
        fact[f[0]] = [f[1],0]
        
        
    fact_pos = list(fact.keys()) #Postion values
    fact_lim = list(fact.values()) #Limit values and number of robots in a factory 
    
    print(f'Robot Positions: {robot}')
    print(f'Factory Positions: {fact_pos}')
    print(f'Factory Limits: {fact_lim}')
    
    dist = []
    curr_dist = 0
    for r in robot: #going through each robot position
        print(f'Starting Robot In Position {r}')
        #print(f'Running Distance Total: {curr_dist}')
        
        if r in fact.keys(): #The case of the robot already being on top of a factory
            print(f'Same Position found: Position {r}')
            dist.append(0)
            fact[r][1] += 1
            
        else: #Robot is not on top of a factory
            print(f'Robot {r} is NOT on a factory position')

            for f in fact.values(): #Going through each factory positions
                print(f'fact.values: {f}')
                f_pos = f[0]
                
            
                print(f'current distance: {curr_dist}')                
                
                if np.abs(r - f[0]) < curr_dist:
                    curr_dist = np.abs(r-f)
                else:
                    if fact[abs(curr_dist) + r][1] < fact[abs(curr_dist) + r][0]: #if the factory is not filled
                        dist.append(abs(curr_dist)) #adds the current distance to be added
                        fact[abs(curr_dist) + r][1] += 1
                        
    print(f'Final Factory stats: {fact}')
    '''
    #Redone with help
    robot.sort()
    factory.sort()
    
    
    
    #r: robot index, f: factory index, cap: number of robots in factory
    @ft.lru_cache(None)
    def helper(r,f, cap):
        if r == len(robot):
            return 0
        if f == len(factory):
            return float('inf')
        
        #Robot is skipping factory f (no helper)
        #
        skip = helper(r, f+1, 0)
        
        #robot (r) is assigned to factory (f) if the limit has not been reached
        if cap + 1 <= factory[f][1]:
            #since a robot has been assigned, the code moves to the next robot, looks at the same factory, increases limit
            assign = helper(r+1, f, cap + 1) + abs(robot[r] - factory[f][0])
            return min(skip, assign)
        
        return skip
    





        
    
