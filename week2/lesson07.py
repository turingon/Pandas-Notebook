import pandas as pd

summary = """

In this lesson we will learn math operations on columns and rows with titanic dataset of kaggle specifically train.csv

We can calculate separately count, standard deviation, max, min, and mean in columns operations or you can just use describe method to calculate all and write them

We can also make some mathemetical operation in rows such as calculatin averge of something but in our example we will calculate total passengers in titanic

"""

df = pd.read_csv("../data/train.csv")

count = df.count()
std = df["Fare"].std()
max = df.max()
min = df.min()
mean = df["Fare"].mean()

describe = df.describe()


total_passengers = df["Parch"] + df["SibSp"] + 1

df["Human Count in Family"] = total_passengers
