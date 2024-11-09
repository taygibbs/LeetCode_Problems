# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 19:46:41 2024

@author: tayta
"""

#This is just a small set of code that I will be using to practice topics that I have not worked on before

#the collection type set() is a the equivalent to a hashset used in different 


for i in range(5,-1,-1):
    print(i)
    

#Puts a list into a list of tuples with the first number being the index and second being the actual value
arr = [5,6,8,2,3,4,6,10]
arr_list = list(enumerate(arr))
print(arr_list)
for i,num in arr_list:
    print(f'i = {i}    num = {num}')
    
    
    
#messing around with hash sets or dictionaries

#while this works for arrays that have the numbers necessary, it doesn't work for any list
# that does not contain the modulo/remainder
numMap = {}
length = 0
tot = 0
p = 7
for i, num in enumerate(arr):
    numMap[num] = i #this puts the index as the value and the element as the key
    tot += num

while tot % p != 0:
    if tot % p in numMap:
        del numMap[tot % p]
        tot -= tot % p
        length += 1
    
numMap.keys() #Displays the keys of the dictionary



    
def backward_check(path):
    
    for i in range(len(path)-1)

