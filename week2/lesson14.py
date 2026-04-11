import pandas as pd
import numpy as np

summary = """ 

In this lesson we will learn create a conditional from more than 2 or more choices 

also we will use np.select() method

"""

df = pd.read_csv("../datas/train.csv")

conditions = [
    (df["Pclass"] == 1) & (df["Survived"] == 1),
    (df["Pclass"] == 1) & (df["Survived"] == 0),
    (df["Pclass"] == 3) & (df["Survived"] == 1),
    (df["Pclass"] == 3) & (df["Survived"] == 0),
]

values = [
    "Lucky Rich",
    "Unlucky Rich",
    "Lucy Poor",
    "Unlucky Poor",
]

selections = np.select(conditions, values, "No Evaluation")

df["Luck"] = selections
