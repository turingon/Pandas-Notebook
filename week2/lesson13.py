import pandas as pd

summary = """

In this lesson we will learn selecting columns with multiple conditions 

We will learn & | operators to use multiple conditionals

"""

df = pd.read_csv("../data/train.csv")

third_class_survivors = df[(df["Pclass"] == 3) & (df["Survived"] == 1)]


third_class_or_first_class_survivors = df[
    ((df["Pclass"] == 3) | (df["Pclass"] == 1)) & (df["Survived"] == 1)
]
