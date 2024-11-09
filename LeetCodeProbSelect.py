# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:24:01 2024

@author: tayta
"""

import LeetcodeSolutions as lcs
import os
import sys

terminal_size = os.get_terminal_size()

def get_problems(val = None):
    problems = {0: 'Exit Program', 
                88:'MergeSortedArray',
                1:'twoSum',
                2:'addTwoNumbers (IN PROGRESS)',
                3:'lengthOfLongestSubstring',
                4: 'findMedianOfSortedArray', 
                7: 'reverseInteger', 
                8: 'String to Integer (atoi)',
                1093: 'sampleStats',
                168: 'convertToTitle',
                1590: 'minSubarray',
                2463: 'minimumTotalDistance',
                26: 'removeDuplicates'
                }
    
    sort_probs = sorted(problems.items())
    
    if val == None:
        for key, value in sort_probs:
            print(key, ":", value, ' : ', get_description(key))
    else:
        print('Problem: ' + problems[val] + '\n'
              + 'Description: ' + get_description(val))
        
def get_description(val: int) -> str:
    desc = {0:'',
            88:'Merges two sorted arrays into one sorted array',
            1: 'Finds the earliest indecies which the elements sum to a targeted number',
            2: 'Adds two LinkedNode lists together reversed', 
            3: 'Finds the length of the longest substring in a larger string',
            4: 'Finds the median number of a sorted array',
            7: 'Takes in an integer and reverses the numbers (ie, 123 -> 321)',
            8: 'Takes in a string and will find the first set of numbers and its sign (+/-)',
            1093: 'Takes in an int list of 256 elements representing the number of times each index is seen in an original array and outputs the minimum, maximum, mean, median, and mode of the og list',
            30: 'Takes in a string and an array of strings that are to be found within the og array',
            168: 'Takes in an integer and returns the Excel Column Title. (ie, x = 27 returns AA)',
            1590: 'Takes in an list and an integer, then makes the sum of the list divisable by the integer by removing a subarray. Then returns the length of that removed array',
            2463: 'Takes in two lists corresponding to a robots and factory positions. Then returns an integer based on the minimum distance for robots to travel to the factories.',
            26: 'Takes in an array and removes duplicates, returning the number of elements in the sorted array'
            }
                
    return desc[val]

def get_Submission_Status():
    #Status format: problem #: ('Accepted/NotSubmitted', # of tries to get accepted)
    status = {1: ('Accepted',1),
              2: ('Unsub.', 0),
              3: ('Accepted', 1),
              4: ('Accepted', 1),
              7: ('Accepted', 4),
              88: ('Accepted', 5),
              168: ('Accepted', 1),
              1093: ('Accepted', 2),
              1590: ('Unsub.', 3),
              2463: ('Unsub.',0),
              26: ('Accepted',3)
              }
    
    return status

def run_Problem(prob: int):
    match prob:
        case '88':
            
            nums1 = [[1,2,3,0,0,0],[1],[0],[2,0],[4,5,6,0,0,0]]
            nums2 = [[2,5,6],[],[1],[1],[1,2,3]]
            m = [3,1,0,1,3]
            n = [3,0,1,1,3]
            for i in range(len(nums1)):
                print('Inputting:')
                print(f"nums1: {nums1[i]} -> m = {m[i]}, nums2: {nums2[i]} -> n = {n[i]}")
                print(f'Merged: {lcs.MergeSortedArray(nums1[i], m[i], nums2[i], n[i])}')
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
                
        case '1093':
            count = [0,1,2]
            count[0] = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0]
            count[1] = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,0]
            count[2] = [2725123,2529890,2612115,3807943,3002363,3107290,2767526,981092,
                      896521,2576757,2808163,3315813,2004022,2516900,607052,1203189,
                      2907162,1849193,1486120,743035,3621726,3366475,639843,3836904,
                      462733,2614577,1881392,85099,709390,3534613,360309,404975,715871,
                      2258745,1682843,3725079,564127,1893839,2793387,2236577,522108,
                      1183512,859756,3431566,907265,1272267,2261055,2234764,1901434,
                      3023329,863353,2140290,2221702,623198,955635,304443,282157,3133971,
                      1985993,1113476,2092502,2896781,1245030,2681380,2286852,3423914,
                      3549428,2720176,2832468,3608887,174642,1437770,1545228,650920,
                      2357584,3037465,3674038,2450617,578392,622803,3206006,3685232,
                      2687252,1001246,3865843,2755767,184888,2543886,2567950,1755006,
                      249516,3241670,1422728,809805,955992,415481,26094,2757283,995334,
                      3713918,2772540,2719728,1204666,1590541,2962447,779517,1322374,
                      1675147,3146304,2412486,902468,259007,3161334,1735554,2623893,
                      1863961,520352,167827,3654335,3492218,1449347,1460253,983079,
                      1135,208617,969433,2669769,284741,1002734,3694338,2567646,3042965,
                      3186843,906766,2755956,2075889,1241484,3790012,2037406,2776032,
                      1123633,2537866,3028339,3375304,1621954,2299012,1518828,1380554,
                      2083623,3521053,1291275,180303,1344232,2122185,2519290,832389,
                      1711223,2828198,2747583,789884,2116590,2294299,1038729,1996529,
                      600580,184130,3044375,261274,3041086,3473202,2318793,2967147,
                      2506188,127448,290011,3868450,1659949,3662189,1720152,25266,1126602,
                      1015878,2635566,619797,2898869,3470795,2226675,2348104,2914940,
                      1907109,604482,2574752,1841777,880254,616721,3786049,2278898,
                      3797514,1328854,1881493,1802018,3034791,3615171,400080,2277949,
                      221689,1021253,544372,3101480,1155691,3730276,1827138,3621214,
                      2348383,2305429,313820,36481,2581470,2794393,902504,2589859,740480,
                      2387513,2716342,1914543,3219912,1865333,2388350,3525289,3758988,
                      961406,1539328,448809,1326527,1339048,2924378,2715811,376047,
                      3642811,2973602,389167,1026011,3633833,2848596,3353421,1426817,
                      219995,1503946,2311246,2618861,1497325,3758762,2115273,3238053,
                      2419849,2545790]
            for i in range(len(count)):
                print(f'Inputting count[{i}]')
                stats = lcs.sampleStats(count[i])
                print(f'min: {stats[0]}, max: {stats[1]}, mean: {stats[2]}, median: {stats[3]}, mode: {stats[4]}')
        case '1590':
            nums = [[3,1,4,2],[6,3,5,2],[1,2,3]]
            p = [6,9,3]
            for i in range(len(nums)):
                print(f'Inputting nums = {nums[i]}  p = {p[i]}')
                print('The length')
                
        case '2463':
            robot = [[0,2,6],[0,2],[5,8]]
            factory = [[[2,2],[5,2]],[2,2],[4,10]]
            
        case '26':
            nums = [[1,1,2],[0,0,1,1,1,2,2,3,3,4]]
            for i in nums:
                print(f'Inputing: {i}')
                print(f'Array with duplicates removed is length: {lcs.removeDuplicates(i)}')
            
        case 0:
            print('Exiting Program')
            sys.exit()