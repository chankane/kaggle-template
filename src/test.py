# col.py
import pandas as pd


# 1


train = pd.read_csv('./data/train.csv', keep_default_na=False)
test = pd.read_csv('./data/test.csv')
df = pd.concat([train, test])

print('')
print('######## col.py ########')
print('In cols:')
print(df.columns.values)
print('')

# 2

print('Out cols:')
print(df.columns.values)

df.to_csv('./data/col-out.csv', index=False)

print(train['Age'])
print(test['Age'])
print(type(pd.NA))
print(type(train['Age'][0]))
print(type(test['Age'][0]))
print(train)
print(test)
