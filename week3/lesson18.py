import pandas as pd

summary = """ 

In this lesson we will learn how to get unique values from a column with unique() method furthermore we will learn how to get total number of unique values with two ways 

First way to get the size of unique values is using len() function

Second way to get the size of unique values is using nunique() method of pandas

"""

df = pd.read_csv("../datas/laptop_price.csv", encoding_errors="ignore")

## unique() method
unique_brands = df["Company"].unique()

unique_sizes = df["Inches"].unique()

## len() function
size_of_unique_brands = len(unique_brands)

## nunique() method
total_number_of_unique_sizes = df["Inches"].nunique()
