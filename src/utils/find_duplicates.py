import glob
import os
import re

os.chdir("../")
for file in glob.glob("*.grako"):
    print(file)

    with open(file) as f:
        b = f.read()

    regex = re.compile(r'(.*) =\n')
    found = regex.findall(b)

    res = {}
    for name in found:
        if name not in res:
            res[name] = None
        else:
            print name

    print ''
