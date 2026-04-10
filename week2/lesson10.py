import pandas as pd

summary = """ 

In this lesson we will learn how to rename columnsand indexes with rename() method

"""

df = pd.read_csv("../data/train.csv")

df.rename(columns={"Sex": "Gender"}, inplace=True)

df.rename(index={0: "A", 1: "B", 2: "C"}, inplace=True)
