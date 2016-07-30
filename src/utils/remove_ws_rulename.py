import re

path = r'..\ebnf\sql1992.ebnf'
with open(path) as f:
    b = f.read()

regex = re.compile(r"<[\w ']+>")
found = regex.findall(b)
for old in found:
    new = old.replace(' ', '_')
    new = new.replace("'", '').lower()
    b = b.replace(old, new)
print(found)
print(b)

with open(path, 'w') as f:
    f.write(b)
