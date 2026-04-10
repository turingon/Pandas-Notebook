import numpy as np
import pandas as pd


summary = "In this lesson we learned the creation of dataframes and ways to create them"

fruits = [
    "Banana",
    "Oranoe",
    "Peach",
    "Kiwi",
]
prices = [
    2,
    3,
    10,
    0,
]

data = np.array(
    [
        [1, 4, 5],
        [1, 22, 5],
        [6, 7, 6],
    ]
)
data1 = {
    "Fruits": fruits,
    "Prices": prices,
}

df0 = pd.DataFrame(
    data, index=["row1", "row2", "row3"], columns=["col1", "col2", "col3"]
)

df1 = pd.DataFrame(data1)

titanicdf = pd.read_csv("../data/train.csv")
