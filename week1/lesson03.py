import pandas as pd

summary = "In this lecture we will learn how to select a single column from a dataset and for this we will use titanic dataset of kaggle specifically train.csv"

df = pd.read_csv("../data/train.csv")

fares = df["Fare"]
names = df.Name

names_data_type = type(names)
fares_data_type = type(fares)

names_count = names.count
