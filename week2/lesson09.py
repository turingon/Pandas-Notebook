import pandas as pd

summary = """

In this lesson we will how to sort dataframes with one or multiple columns with sort_values() methods and it is some properties 

For more detail please look at the lesson's code

"""

df = pd.read_csv("../datas/train.csv")

sorted_fare = df.sort_values("Fare", ascending=True)

sorted_fare_age = df.sort_values(["Fare", "Age"], ascending=False)

## BTW sort_values method does not update the df defaulty but if you will set inplace True the method will update the df automatically without
# manually stores it to a variable
