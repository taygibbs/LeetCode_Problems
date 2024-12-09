# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 19:46:41 2024

@author: tayta
"""

import heapq

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



    
#binary Search tree practice
class Node:
    #setting up the nodes value and then assumes the branches under are none, until set later
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    
    # The searching function
def search(root,key):
    try:
        print(f'root: {root.key}  key: {key}')
    except AttributeError:
        print('No Root Found')
    #base case: root is null (end of tree) or the value we are looking for (key)
    if root is None or root.key == key:
        return root
    #if the key is larger than the current nodes value of key, then it will move to the larger side
    if root.key < key:
        return search(root.right,key)
    
    #if the key is smaller than the current nodes value of key, it will look at the lesser side
    return search(root.left, key)

#first level
root = Node(50) #start of the tree has value 50

#second level
root.left = Node(30) #first left branch
root.right = Node(70) #first right branch

#third level
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

#searching through the binary search tree
print('Found' if search(root,19) else 'Not Found')
print('Found' if search(root, 80) else 'Not Found')
    

#messing around with heap queue
l1 = [5,7,9,1,3]
heapq.heapify(l1)

print(f'Created heap is: {list(l1)}')

print(f'Using heappush() to push elements into the heap:')
heapq.heappush(l1, 4)
print(f'The modified heap after pushing is: {list(l1)}')
print('Popping the smallest element using heappop()')
k = heapq.heappop(l1)
print(f'Popped k: {k}')
