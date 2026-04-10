import pandas as pd

summary = "We will learn some attributes, methods, and functions of pandas via using titanic dataset of kaggle especially the train.csv"

df = pd.read_csv("../data/train.csv")

## Attributes
shape = df.shape
index = df.index
columns = df.columns
data_types = df.dtypes

## Methods
head = df.head(10)
info = df.info()
describe = df.describe()

## Functions
length = len(df)
maximum = max(df.index)
minimum = min(df.index)
data_type = type(df)
rounded = round(df, 2)
