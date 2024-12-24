# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:22:52 2024

@author: tayta
"""

import pandas as pd

#1
def createDataFrame(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(data = student_data, columns = ['student_id','age'])
    
    return df

#2
def getDataFrameSize(df: pd.DataFrame) -> list[int]:
    
    return list[df.shape]
#3
def selectFirstRows(df: pd.DataFrame, n: int) -> pd.DataFrame:
    return df.iloc[0:n]
#4   
def createColumn(df: pd.DataFrame, title: str, data: list) -> pd.DataFrame:
    df[title] = data
    return df
#5
def removeDuplicates(df: pd.DataFrame, title: str) -> pd.DataFrame:
    df.drop_duplicates(title)
    return df

#6
def dropMissing(df: pd.DataFrame, title: str) -> pd.DataFrame:
    
    return df.dropna(subset= title) #the subset will looks at the specific columns for the missing values

#7
def modifyColumn(df: pd.DataFrame, title: str) -> pd.DataFrame:
    df[title] = df[title] * 2
    return df

#8
def renameColumns(df: pd.DataFrame, og: str, new: str) -> pd.DataFrame:
    df.rename(columns = {og : new})
    return df

#9
def changeDataType(df: pd.DataFrame, title: str, dtype: type) -> pd.DataFrame:
    df.convert_dtypes(convert_integer=title)
    df.astype({title: dtype})
    return df

#10
def fillMissingValues(df: pd.DataFrame, title: str,quan: int) -> pd.DataFrame:
    return df.fillna(value={title, quan})

#11 reshape data: concate. Puts two dataframes together
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat(objs = [df1,df2])

#12 reshape data: Pivot (not pivot table)
def pivotTable(df: pd.DataFrame) -> pd.DataFrame:
    #index: main row classification
    #column: splits the values in the named series and makes them into the columns
    #values: the data that is being shown based on the index and columns
    pd.pivot(df, index= 'month', columns = 'city', values= 'tempurature')
    
#13 reshape data: melt
def meltTable(df: pd.DataFrame) -> pd.DataFrame:
    #can be done using pandas or DataFrame. ie, pd.melt(df....) or df.melt(value_vars...)
    #id_vars: the column that will not change
    #value_vars: the columns that are to be 'melted'.
    #var_name: the name of the new column
    #value_name: the new column from melting
    return pd.melt(df,id_vars= 'product', 
                      value_vars= ['quarter_1','quarter_2','quarter_3','quarter_4'],
                      var_name= 'quarter',
                      value_name= 'sales')

#14 Chaining
def findHeavyAnimals(animals: pd.DataFrame)-> pd.DataFrame:
    
    heavy = animals[animals['weight'] > 100].sort_values(by= 'weight', ascending = False)
    names_only = heavy[['name']] #the [['names]] makes the data into a dataframe instead of a series
    return names_only
    
def main():
    student_data = [[1,15],[2,11],[3,11],[4,20]]
    
    df = createDataFrame(student_data)
    size = getDataFrameSize(df)
    print(f'size: {size}')

