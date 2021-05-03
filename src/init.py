with open('./data/train.csv', 'r') as f:
    cols = f.readline().strip().split(',')

with open('./src/col.py', 'r') as f:
    code = f.read()

# 1
a = []
for col in cols:
    s = "def " + col + "(df):\n"
    s += "    return df\n"
    a.append(s)
code = code.replace('# 1\n', '\n\n'.join(a))

# 2
s = ''
for col in cols:
    s += "df = " + col + "(df)\n"
code = code.replace('# 2\n', s)

with open('./src/col.py', 'w') as f:
    f.write(code)
