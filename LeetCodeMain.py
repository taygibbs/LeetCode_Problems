# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:18:42 2024

@author: tayta
"""
import LeetcodeSolutions as lcs
import os
import sys


terminal_size = os.get_terminal_size()
#Whenever a problem is added, I will add it as part of the dictionary in the LeetcodeSolutions code and call it in main.


print('What problem would you like to see?\nI have:')

lcs.get_problems()

prob = input('\nInput the number of the problem you would like to see: ')


print('=' * terminal_size.columns)

print('You Selected:')
problem = lcs.get_problems(int(prob))

match prob:
    case '88':
        
        nums1 = [[1,2,3,0,0,0],[1],[0]]
        nums2 = [[2,5,6],[],[1]]
        m = [3,1,0]
        n = [3,0,1]
        for i in range(len(nums1)):
            print('Inputting:')
            print(f"nums1: {nums1[i]} -> m = {m[i]}, nums2: {nums2[i]} -> n = {n[i]}")
            print(lcs.MergeSortedArray(nums1[i], m[i], nums2[i], n[i]))
            print('=' * terminal_size.columns)
    case '1':
        
        nums = [[2,7,11,15],[3,2,4],[3,3]] 
        target = [9,6,6]

        for i in range(len(nums)):
            print('inputting:')
            print(f"nums: {nums[i]},target = {target[i]}")
            print(f"The indexes of the solution are: {lcs.twoSum(nums[i],target[i])}")
            print('=' * terminal_size.columns)
            
    case '2':
        
        l1 = [[2,4,3],[0],[9,9,9,9,9,9,9]]
        l2 = [[5,6,4],[0],[9,9,9,9]]
        
        #l1 = ListNode(2)
        
        for i in range(len(l1)):
            print('Inputting:')
            print(f'l1: {l1[i]}, l2: {l2[i]}')
            print(f'The resulting added list: {lcs.addTwoNumbers(l1[i],l2[i])}')
            print('=' * terminal_size.columns)
            
    case '3':
        
        s = ['abcabcbb','bbbbb','pwwkew']
        
        for i in s:
            print(f'Inputting: s = {i}')
            print(f'Longest Substring has length: {lcs.lengthOfLongestSubstring(i)}')
            print('=' * terminal_size.columns)
            
        own_string = input('Would you like to try putting in your own string? (y/n) ')
        if own_string == 'y':
            print('Great! Type in your own string, without spaces of course!')
            new_s = input()
            print(f'The string "{new_s}" has a longest substring of length {lcs.lengthOfLongestSubstring(new_s)}')
        elif own_string == 'n' or own_string == None:
            print('Exiting...')
            sys.exit()
            
    case '4':
        
        nums1 = [[1,3],[1,3]]
        nums2 = [[2],[2,4]]
        
        for i in range(len(nums1)):
            print(f'Inputting nums1 = {nums1[i]}  nums2 = {nums2[i]}')
            print(f'Median is: {lcs.findMedianSortedArrays(nums1[i],nums2[i])}')
            
    case '7':
        
        x = [123,-123,120]
        for i in x:
            print(f'Inputting x = {i}')
            
            print(f'Reversed: {lcs.reverse(i)}')
        own_int = input('Would you like to try putting in your own integer? (y/n) ')
        if own_int == 'y':
            print('Great! Type in your own integer, without spaces of course!')
            new_s = input()
            print(f'The integer {new_s} has the reversed integer {lcs.reverse(new_s)}')
        elif own_string == 'n' or own_string == None:
            print('Exiting...')
            sys.exit()
    case '8':
        s = ['42','   -042','1337c0d3','0-1','words and 987']
        
        for i in s:
            print(f'Inputting: "{i}"')
            print(f'Number Found: {lcs.myAtoi(i)}')
        
    case 0:
        print('Exiting Program')
        sys.exit()