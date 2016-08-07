# Conversion from BNF to EBNF - sql2003

1. Use `-{2,4}h3[\S\s]*?\n-{2,4}/h3\n` to remove `h3` headers
1. Use `-{2,4}p[\S\s]*?\n-{2,4}/p\n` to remove `p` paragraphs
1. Use `-{2,4}##.*$\n` to remove `html` code
1. Use `-{2,4}h2[\S\s]*?\n-{2,4}/h2\n` to remove `h2` headers. - Had manual fix, no close tag
1. Use `--.*$` to remove misc. comments headers. & manual cleanup
1. Replace `PL/I` with `PL_I`
1. Replace `(<.*):(.*>)` with `\1_\2` to remove colons
1. Replace `(<.*)-(.*>)` with `\1_\2` to remove hyphens- apply multiple times. note END-EXEC was mistakely changed. will fix later
1. use script from readme to remove all spaces from rule names
1. use `([^'<])\b(\w+)\b([^'>])` to quote with `\1'\2'\3` apply multiple times
1. manually quote symbols
1. add semicolong to defintions
1. add spaces between >< '< >'
1. remove <...> replace ::=
used `<(\w+)>` `\L$1` for lowercase and remove <>

# Convert from BNF to EBNF - sql2011

1. use `\d+.\d+.+\n\n+Function\n(.*\n)*?Format` to convert comments and headers
1. Replace `(<.*):(.*>)` with `\1_\2` to remove colons
1. Replace `(<.*)-(.*>)` with `\1_\2` to remove hyphens- apply multiple times. note END-EXEC was mistakely changed. will fix later
1. use `(^\d+ .*)` to format all headers
1. use to select words to put quotes around `(?<!['<])\b([A-Z_\-]+)\b(?!['>])`
1. `(?<!::=\s)`    continuetions
1. use `(^[^\n#].*)\n\n` to add ; to the end of defintnions with `\1\n    ;\n\n`
1. use `(<\w+>) *\.\.\.` to select ellipses after a rule. use `{\1}+` to replace it
1, use `<(\w+)>[\n\s]+\[[\n\s]+{[\n\s]+<comma>[\n\s]+<\1>[\n\s]+}[\n\s]+\.\.\.[\n\s]+\]` to replace list chains with `<comma>.{\1}`

1. use for more generic version of above `(.*)[\n\s]+\[[\n\s]+{[\n\s]+<comma>[\n\s]+\1[\n\s]+}[\n\s]+\.\.\.[\n\s]+\]`
1. but first format `\[\n\s+` with `[ `
1. use `(?<!\.){(.*?)}(?!\+)` to remove left over {}
`(?<!\.){([\w \|']+?)}(?!\+)`
1. remove rules that have no context anymomre (rules werent being used)


1. `        (.*)\n    \|   ` to `    |   \1\n    |   ` to add leading | to options
1. `(?<!=)\n    (?!;)` to `\n        ` to indent in continuation lines
1. use `(\S)  +` with `\1 ` to clean up multiple spaces
1. use `{(.*?)}([^+])` with `(\1)\2` to replace {} with ()
1. use `[)}\]'>][<({\[']` to find definitions touching that shouldnt be

# General Conversion

## Conversion Aids

```Python
# Regex for words within <>
'<([\w]+(( |-)\w+)*)>'
'<[\w]+(?: \w+)+>'
```


## Convert blank spaces to underscore

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

## Add semi-colon to previous definition
```python
import re

path = r'.\sql92.ebnf'
with open(path) as f:
    b = f.read()

regex = re.compile(r'.(\n+<[\w]+> ::=)')
found = regex.findall(b)
for old in found:
    b = b.replace(old, '\n        ;' + old)
print(found)
print(b)

with open(path, 'w') as f:
    f.write(b)

```


## Remove rules that aren't reference by anything
```python

import re

path = r'.\sql92.ebnf'

with open(path) as f:
    b = f.read()

regex = re.compile(r'(.*) =\n')
found = regex.findall(b)

res = {}
for def_ in found:
    regex = re.compile(r'\b' + def_ + r'\b')
    res[def_] = len(regex.findall(b))

for key, value in res.items():
    if key == 'start':
        continue
    if value == 1:
        print key
        b=re.sub('\n'+key + r' =\n[\s\S]*?;\n', '', b)

with open(path, 'w') as f:
    f.write(b)

```

## Update to standarize definitions
```
digit
/\d/

regular_identifier
@name
/[a-z]\w*/

space
/ /

delimited_identifier_body
/(""|[^"\n])+/

character_representation
/(''|[^'\n])+/

sql_language_identifier
regular_identifier

hexit
/[a-f\d]/
```

## Rename
`qualified_name` to `schema_qualified_name`

## Remove Duplicates within Rule
`  \| (\w+)\n  \| \1\n` and `  \| \1\n`

## Lists
`(\w+) \[{comma \1}\+\]` to `','.{$1}`

