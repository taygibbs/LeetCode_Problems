# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:31:27 2024

@author: Taylor


This is a set of code that I am writing to work with the LeetCode problems.
"""
#Imports
#import collections
import os


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


#Problem 88:
"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
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
            if i <= k:
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


#Main code:
    
#Whenever a problem is added, I will add it as part of the dictionary and call it using a match case system.
problems = {0: 'Exit Program', 88:'MergeSortedArray',1:'twoSum',2:'addTwoNumbers (IN PROGRESS',3:'lengthOfLongestSubstring'}
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
        
        #l1 = ListNode(2)
        
        for i in range(len(l1)):
            print('Inputting:')
            print(f'l1: {l1[i]}, l2: {l2[i]}')
            print(f'The resulting added list: {addTwoNumbers(l1[i],l2[i])}')
            print('=' * terminal_size.columns)
            
    case '3':
        print('You Selected the lengthOfLongestSubstring problem:')
        s = ['abcabcbb','bbbbb','pwwkew']
        
        for i in s:
            print(f'Inputting: s = {i}')
            print(f'Longest Substring has length: {lengthOfLongestSubstring(i)}')
            print('=' * terminal_size.columns)
            
        own_string = input('Would you like to try putting in your own string? (y/n) ')
        if own_string == 'y':
            print('Great! Type in your own string, without spaces of course!')
            new_s = input()
            print(f'The string "{new_s}" has a longest substring of length {lengthOfLongestSubstring(new_s)}')
        elif own_string == 'n' or own_string == None:
            print('Exiting...')
            exit()
    case 0:
        print('Exiting Program')
        exit()