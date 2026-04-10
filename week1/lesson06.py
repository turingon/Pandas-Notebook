import pandas as pd
import numpy as np

summary = """

In this lesson we will learn other ways to add columns to dataframes for this task we are using titanic dataset of kaggle specifically train.csv

There are two more ways to add columns to dataframes assign() and insert()

assing()

When to use assign

- Add multiple columsn in a single line of code 
- When you need to overwrite the values of an exisitng columns (best practice)

insert()

When to use insert 

- Inserts a new column at a specific position of index

"""

df = pd.read_csv("../data/train.csv")

new_fares = np.random.rand(len(df)) * 75

series1 = pd.Series(new_fares, index=np.arange(0, len(df)))

new_df = df.assign(fares=series1)


new_ages = np.random.randint(10, 80, size=len(df))

series2 = pd.Series(new_ages, index=np.arange(0, len(df)))

df.insert(1, "new_ages", series2)
