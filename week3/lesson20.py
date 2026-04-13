import pandas as pd

summary = """

In this lesson we will learn same things as we learned in lesson19 but this time we are using iloc 

in iloc we use integers over strings in loc

We will learn extract single value, list of values, and slice of values

"""

df = pd.read_csv("../datas/players_20.csv")

## Preparing our dataset of data extractions
df = df.set_index("short_name")

df = df[
    [
        "long_name",
        "age",
        "dob",
        "height_cm",
        "weight_kg",
        "nationality",
        "club",
    ]
]


## Select single values
leo_height = df.iloc[0, 3]

ron_weight = df.iloc[1, 4]

heights = df.iloc[:, 3]

leo_stats = df.iloc[0, :]

## Select list of values
ron_leo_stats = df.iloc[[0, 1], :]

ron_leo_heights = df.iloc[[0, 1], 3]

leo_physics = df.iloc[0, [3, 4]]

ron_leo_physics = df.iloc[[0, 1], [3, 4]]

## Selecting a range of datas
## Warning in iloc property the start is included but the stop is excluded
## start:stop:step
players = [0, 1]
columns = [1, 2, 3, 4]

messi_ron_stats = df.iloc[players, 1 : 6 + 1]

top10 = df.iloc[0:10, columns]


## Selecting with conditions
columns = [0, 1, 2, 3, 4, 5, 6]

tall_players = df.iloc[list(df["height_cm"] > 182), columns]

tall_argentina_players = df.iloc[
    list((df["height_cm"] > 182) & (df["nationality"] == "Argentina")), 1 : 6 + 1
]
