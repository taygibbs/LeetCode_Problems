# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 00:46:25 2024

@author: Taylor Gibbons

This is a set of code that will take basically check the code that I have submitted into leetcode and create some statistics about it
"""

import LeetCodeProbSelect as lcps
import pandas as pd
import numpy as np
import os


filepath_name = os.getcwd() + '/LeetCodeStats.xlsx'


def stats_Main():
    stats = lcps.get_Submission_Status()
    column_names = {0:'Status', 1:'Attempts'}
    
    df_stats = pd.DataFrame.from_dict(stats,).transpose()
    df_stats = df_stats.rename(columns = column_names)
    
    df_acc = df_stats[df_stats.Attempts == 'Accepted']
    df_rej = df_stats[df_stats.Status == 'Unsub']
    
    tot_attempts = df_stats['Attempts'].sum() #total number of attempts for all problems
    avg_attempts = df_stats.Attempts.mean() #Average number of attempts per problem
    max_attempts = df_stats.index[df_stats.Attempts.max()] #Index of the highest attempts
    
    print(f'LeetCode Stats (So Far):\nTotal Number of Attempts: {tot_attempts} Attempts\n' +
          f'Avg. Number of Attempts: {avg_attempts} Attempts Per Problems')
    
    df_stats.to_excel(filepath_name)