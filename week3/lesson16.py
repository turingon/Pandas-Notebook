import pandas as pd

summary = """ 

In this lesson we will learn how to detect duplicates 

for this we will use duplicated method of pandas

and in the lesson we will check are there any duplicates for the name column of dataframe as an example

"""

df = pd.read_csv("../datas/train.csv")

name_duplicate = df.duplicated("Name")

duplicate_names = df[name_duplicate]
