import glob
import os
import re


def process(path):
    with open(path) as f:
        b = f.read()

    regex = re.compile(r"((\w+) =\s+('\w+')\s+;\n)")
    found = regex.findall(b)

    for def_, name, new in found:
        if name == 'underscore':
            continue
        print name

        b = b.replace('\n' + def_ + '\n', '\n')
        b = b.replace(' ' + name + ' ', ' ' + new + ' ')
        b = b.replace(' ' + name + '\n', ' ' + new + '\n')
        b = b.replace('[' + name + ']', '[' + new + ']')
        b = b.replace(' ' + name + ']', ' ' + new + ']')
        b = b.replace('[' + name + ' ', '[' + new + ' ')
        b = b.replace('{' + name + '}', '{' + new + '}')
        b = b.replace('{' + name + ' ', '{' + new + ' ')
        b = b.replace(' ' + name + '}', ' ' + new + '}')
        b = b.replace('(' + name + ')', '(' + new + ')')
        b = b.replace(' ' + name + ')', ' ' + new + ')')
        b = b.replace('(' + name + ' ', '(' + new + ' ')

    with open(path, 'w') as f:
        f.write(b)


if __name__ == '__main__':
    os.chdir("../")
    for file in glob.glob("*.grako"):
        print("Starting {file}".format(file=file))

        process(file)

        print("Finished {file}".format(file=file))
