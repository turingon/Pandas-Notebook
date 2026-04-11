import pandas as pd

summary = """ 

In this lesson we will learn filter with isin() method 

"""

df = pd.read_csv("../datas/train.csv")

rich_and_poor = df["Pclass"].isin([3, 1])

df = df[rich_and_poor]
