# SqlParser - ebnf

## Links:

    https://github.com/daeken/PyTableGen/blob/ddc27ac53948e6bf7e273a634450793ef78e5b79/tblgen/grammar.ebnf
    https://github.com/lambdafu/smc.mw/blob/master/smc/mw/mw.ebnf
    
    https://raw.githubusercontent.com/xwb1989/sqlparser/master/sql.y
    http://www.antlr3.org/grammar/list.html
    http://savage.net.au/SQL/sql-92.bnf.html
    http://www.contrib.andrew.cmu.edu/~shadow/sql/sql1992.txt
    http://savage.net.au/SQL/sql-bnf-20160417.tgz

## Conversion Aids

```Python
# Regex for words within <>
'<([\w]+(( |-)\w+)*)>'
'<[\w]+(?: \w+)+>'
```


### Convert blank spaces to underscore

```python
import re

path = r'.\sql92.ebnf'
with open(path) as f:
    b = f.read()

regex = re.compile(r'<[\w]+(?: \w+)+>')
found = regex.findall(b)
for old in found:
    new = old.replace(' ', '_')
    b = b.replace(old, new)
print(found)
print(b)

with open(path, 'w') as f:
    f.write(b)
```

### Add semi-colon to previous definition
```python
import re

path = r'.\sql92.ebnf'
with open(path) as f:
    b = f.read()

regex = re.compile(r'.(\n+<[\w]+> =)')
found = regex.findall(b)
for old in found:
    b = b.replace(old, ';' + old)
print(found)
print(b)

with open(path, 'w') as f:
    f.write(b)

```
