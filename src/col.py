# col.py
import pandas as pd


# 1


train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")
df = pd.concat([train, test])

print('Input col:')
print(df.columns)

# 2

print('Output col:')
print(df.columns)
print("\n")

df.to_csv("./data/col-out.csv", index=False)
