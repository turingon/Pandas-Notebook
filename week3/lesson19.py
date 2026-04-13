import pandas as pd

summary = """

In this lesson we will learn how to extract datas from a dataset with loc property of pandas and

We will learn how to extract single value

How to extract list of values from a dataset

How to extract slices of values also give attention to warning 

Finally extracting with conditions

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


## Extraction single values with loc property of pandas
leo = df.loc["L. Messi"]
ron = df.loc["Cristiano Ronaldo"]

leo_height = df.loc["L. Messi", "height_cm"]
ron_weight = df.loc["Cristiano Ronaldo", "weight_kg"]

height_of_players = df.loc[:, "height_cm"]

## Extractions list of values with loc property of pandas
leo_and_ron = df.loc[["L. Messi", "Cristiano Ronaldo"]]

height_of_leo_and_ron = df.loc[["L. Messi", "Cristiano Ronaldo"], "height_cm"]

height_and_weight_of_leo = df.loc["L. Messi", ["height_cm", "weight_kg"]]

height_and_weight_of_leo_and_ron = df.loc[
    ["L. Messi", "Cristiano Ronaldo"], ["height_cm", "weight_kg"]
]

## Extracting a range of values with loc property of pandas
## start:stop:step
## Warning contrary to python slices, both the start and stop are included at this
players = [
    "L. Messi",
    "Cristiano Ronaldo",
]

datas = df.loc[players, "age":"club"]


columns = [
    "age",
    "dob",
    "height_cm",
    "weight_kg",
]

top10 = df.loc["L. Messi":"M. Salah", columns]

## Extraction players according to conditions

tall_players = df.loc[df["height_cm"] > 182, columns]

tall_argentine_players = df.loc[
    (df["height_cm"] > 182) & (df["nationality"] == "Argentina"), :
]
