import pandas as pd

summary = """

In this lesson we will learn how can we select rows according to conditions like only get rows matches with these conditions for this lesson we will titanic dataset of kaggle specifically train.csv

"""

df = pd.read_csv("../data/train.csv")

survivors = df[df["Survived"] > 0]

third_class_survivors = df[(df["Pclass"] == 3) & (df["Survived"] == 1)]

second_class_survivors = df[(df["Pclass"] == 2) & (df["Survived"] == 1)]

first_class_survivors = df[(df["Pclass"] == 1) & (df["Survived"] == 1)]
