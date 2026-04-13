import pandas as pd

summary = """

In this lesson we will learn how to use drop_duplicates method of pandas 

Also as an example we will find the most expensive and cheaptest laptops of each brand

"""

df = pd.read_csv("../datas/laptop_price.csv", encoding_errors="ignore")


## Dropping duplicate rows
no_duplicate = df.drop_duplicates(["Company"])

## Example
sorted = df.sort_values(["Company", "Price_euros"])

cheapest_laptops = sorted.drop_duplicates(["Company"])

most_expensive_laptops = sorted.drop_duplicates(["Company"], keep="last")
