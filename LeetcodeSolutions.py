# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:31:27 2024

@author: Taylor


This is a set of code that I am writing to work with the LeetCode problems.
"""
#Imports
#import collections
import os





#Problem 88:
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
""" Some examples:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""

def MergeSortedArray(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
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
    m_index = m - 1 #the last element index of nums1 that will be merged
    n_index = n - 1 #the last element index of nums2 that will be merged
    end = m + n - 1
    
    while n_index >= 0: #Starting from the end of the list and going to the beginning. This will loop until we are before the beginning
        #print('inside while loop')
        
        if m_index >= 0 and nums1[m_index] > nums2[n_index]:
            #print(f"nums1[m_index] = {nums1[m_index]} > {nums2[n_index]} = nums2[n_index]")
            nums1[end] = nums1[m_index]
            m_index -= 1
            
        elif m_index >= 0 and nums1[m_index] <= nums2[n_index]:
            #print(f"nums1[m_index] = {nums1[m_index]} < {nums2[n_index]} = nums2[n_index]")
            nums1[end] = nums2[n_index]
            n_index -= 1
            
        # elif m_index >= 0 and nums1[m_index] == nums2[n_index]:
        #     nums1[end] = nums2[n_index]
            
        else:
            print('Failure to merge the sorted arrays :(')
            break
        
        end -= 1
                    
    print(f"Merged nums1: {nums1}")


#Problem 1
def twoSum(nums: list[int], target: int) -> list[int]:
   """
   Submitted/Accepted with 3977 ms runtime (beating 5%) with 17.22mb of memory (beating 90.42%)

   """
    #inputs a list, we have to find the solution to which two of the elements of the list
    #will add up to the target
    
    #index = 0 #the currently looked at index
   soln = [] #will be two elements long
   for i in range(len(nums)):
        #print(i)
        for k in range(len(nums)):
            if i == k:
                continue
            
            if nums[i] + nums[k] == target:
                soln.append(i)
                soln.append(k)
                break
        if len(soln) ==  2:
           break     
   return soln

#Problem 2:
#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
            
def addTwoNumbers(l1: list, l2: list) -> list:
    l1.reverse()
    l2.reverse()
    print(f"l1 Reversed: {l1} \nl2 Reversed: {l2}")
    l1_num = int(''.join([str(i) for i in l1]))
    l2_num = int(''.join([str(i) for i in l2]))
    l3 = l1_num + l2_num
    l3 = [int(i) for i in str(l3)]
    l3.reverse()
    return l3


#Main code:
    
#Whenever a problem is added, I will add it as part of the dictionary and call it using a match case system.
problems = {0: 'Exit Program', 88:'MergeSortedArray',1:'twoSum',2:'addTwoNumbers'}
problems = sorted(problems.items())
print('What problem would you like to see?\n I have:')
print(problems)
prob = input('\nInput the number of the problem you would like to see: ')
terminal_size = os.get_terminal_size()
print('=' * terminal_size.columns)
match prob:
    case '88':
        print('You Selected the MergeSortedArrays Problem:')
        nums1 = [[1,2,3,0,0,0],[1],[0]]
        nums2 = [[2,5,6],[],[1]]
        m = [3,1,0]
        n = [3,0,1]
        for i in range(len(nums1)):
            print('Inputting:')
            print(f"nums1: {nums1[i]} -> m = {m[i]}, nums2: {nums2[i]} -> n = {n[i]}")
            print(MergeSortedArray(nums1[i], m[i], nums2[i], n[i]))
            print('=' * terminal_size.columns)
    case '1':
        print('You Selected the sumTwo Problem:')
        nums = [[2,7,11,15],[3,2,4],[3,3]] 
        target = [9,6,6]

        for i in range(len(nums)):
            print('inputting:')
            print(f"nums: {nums[i]},target = {target[i]}")
            print(f"The indexes of the solution are: {twoSum(nums[i],target[i])}")
            print('=' * terminal_size.columns)
            
    case '2':
        print('You Selected the addTwoNumbers Problem:')
        l1 = [[2,4,3],[0],[9,9,9,9,9,9,9]]
        l2 = [[5,6,4],[0],[9,9,9,9]]
        
        for i in range(len(l1)):
            print('Inputting:')
            print(f'l1: {l1[i]}, l2: {l2[i]}')
            print(f'The resulting added list: {addTwoNumbers(l1[i],l2[i])}')
            print('=' * terminal_size.columns)
    case 0:
        print('Exiting Program')
        exit()