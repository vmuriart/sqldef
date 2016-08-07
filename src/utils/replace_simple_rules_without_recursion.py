import glob
import os
import re


def process(path):
    with open(path) as f:
        b = f.read()

    regex = re.compile(r'(.*) =\n')
    found = regex.findall(b)

    res = {}
    for def_ in found:
        regex = re.compile(r'\b' + def_ + r'\b')
        res[def_] = len(regex.findall(b))

    regex = re.compile(r'((.*) =\s+(\w+?)\s*;\n)')
    # regex = re.compile(r'((.*) =\s+(.*?\s+.*?)\s*;\n)')
    # regex = re.compile(r'((.*) =\s+(.*?\s+.*?\s+.*?)\s*;\n)')

    found = regex.findall(b)
    names = []
    news = []

    for def_, name, new in found:
        if name == 'start':
            continue
        names.append(name), news.append(new)

    to_do = []

    for key, value in res.items():
        if key == 'start':
            continue

        if value > 20 or key not in names:
            continue
        to_do.append(key)

    for def_, name, new in found:

        def needed():
            for x in news:
                if name in x:
                    return True

        if needed():
            continue

        if name == 'start':
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
