# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:18:42 2024

@author: tayta
"""
import LeetcodeSolutions as lcs
import LeetCodeProbSelect as lcps
import os


terminal_size = os.get_terminal_size()

def eq_print():
    print('=' * terminal_size.columns)
    


print('What problem would you like to see?\nI have:')

lcps.get_problems() #Prints the problem names and descriptions

eq_print()

#The number of the problem wanting to be seen
prob = input('\nInput the number of the problem you would like to see: ')

print('You Selected:\n')
problem = lcps.get_problems(int(prob)) #Displays the problem name and description again
lcps.run_Problem(prob)
eq_print()



