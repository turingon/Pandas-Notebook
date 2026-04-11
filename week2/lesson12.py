import pandas as pd
import numpy as np

summary = """

In this lesson we will learn how to create columns based on one condition

"""

df = pd.read_csv("../datas/train.csv")

lucky_ones = np.where(df["Survived"] == 1, "Lucky", "Unlucky")

df["Lucky Ones"] = lucky_ones
