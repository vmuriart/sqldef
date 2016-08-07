import glob
import os
import re

os.chdir("../ebnf/")
for file in glob.glob("*.ebnf"):
    print(file)

    with open(file) as f:
        b = f.read()

    regex = re.compile(r"<[\w ']+>")
    found = regex.findall(b)
    for old in found:
        new = old.replace(' ', '_')
        new = new.replace("'", '').lower()
        b = b.replace(old, new)
    print(found)
    print(b)

    with open(file, 'w') as f:
        f.write(b)
