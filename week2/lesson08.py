import pandas as pd

summary = """
In this lesson see how to count rows and counts row categorically and we will use titanic dataset of kaggle specificaly train.cvs

Count rows to learn how many of them we have is very easy you can do this by two way one len() function other count() method 

To count categorically we are using value_counts() method and we can also find relative frequency of categories with this method 

For more details look at the lesson code
"""

df = pd.read_csv("../datas/train.csv")

length = len(df["Sex"])
count = df["Sex"].count()

gender_count = df["Sex"].value_counts()

gender_relative_frequency = df["Sex"].value_counts(normalize=True)
