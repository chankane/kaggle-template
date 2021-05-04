# col.py
import pandas as pd


# 1


train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')
df = pd.concat([train, test])

print('\n')
print('In cols:')
print(df.columns.values)
print('\n')

# 2

print('Out cols:')
print(df.columns.values)

df.to_csv('./data/col-out.csv', index=False)
