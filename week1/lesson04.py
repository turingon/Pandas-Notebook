import pandas as pd

summary = """

In this lecture we will learn how to select 2 or more columns from a dataset and the dataset we will use for this task is the titanic dataset of kaggle specifically train.csv 
for this we will use [[]] 

"""

df = pd.read_csv("../data/train.csv")

passengers_with_fares = df[["Name", "Fare"]]
