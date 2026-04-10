import pandas as pd
import numpy as np

summary = """

In this lesson we will learn how can we add a new column to a dataframe. For this task we are using titanic dataset of kaggle specifically train.csv

we will add scalar valued columns or n many random valued columns to our dataframe to make this possible we will use some methods from numpy

For more detail please check the lesson
"""

df = pd.read_csv("../data/train.csv")


df["new col"] = 50

elements = np.random.randint(1, 100, size=len(df))

df["new col"] = elements
