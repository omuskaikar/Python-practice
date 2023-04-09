import pandas as pd
import numpy as np

exam_data = {
    "name": [
        "Anastasia",
        "Dima",
        "Katherine",
        "James",
        "Emily",
        "Michael",
        "Matthew",
        "Laura",
        "Kevin",
        "Jonas",
    ],
    "score": [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


df = pd.DataFrame(exam_data, index=labels)


df.head(3)


df1 = df[["name", "score"]]
df1


df1 = df.loc["a":"e", ["name", "score"]]


df.iloc[:7, [1, 3]]


df[df["attempts"] > 2]


print("no. of coulmns is:", len(df.columns))
print("no. of rows are:", len(df))


df1 = df[df["score"] > 15]
df1 = df1[df1["score"] <= 20]
df1


df1 = df[df["attempts"] < 2]
df2 = df1[df1["score"] > 15]
df2


df.loc["k"] = ["om", 20.0, 2, "yes"]


df


df.drop("k", inplace=True)
df


df.sort_values(by=["name", "score"], ascending=[False, True])


a = df.head(10)
a


df["qualify"] = df["qualify"].map({"yes": True, "no": False})


df


df.at["d", "score"] = 10.2


df


df.isnull()
df.dropna()


df.duplicated()


l1 = [0, 10, 20, 40, 60, 80]
l2 = [10, 30, 40, 50, 70]
l3 = []
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)
