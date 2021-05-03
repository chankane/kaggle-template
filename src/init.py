with open('./data/train.csv', 'r') as f:
    cols = f.readline().strip().split(',')

# col.py
with open('./src/col.py', 'r') as f:
    code = f.read()

with open('./old/col.def.py', 'w') as f:
    f.write(code)

a = []
for col in cols:
    s = "def " + col + "(df):\n"
    s += "    # any codes here...\n"
    s += "    return df\n"
    a.append(s)
code = code.replace('# 1\n', '\n\n'.join(a))

s = ''
for col in cols:
    s += "df = " + col + "(df)\n"
code = code.replace('# 2\n', s)

with open('./src/col.py', 'w') as f:
    f.write(code)
