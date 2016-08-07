import glob
import os
import re

RULE_DEFINITION = re.compile(r"((\w+) =[\s\S]*?\s*;\n)")


def process(text):
    # Group1 is the full rule definition
    # Group2 is only the name of the rule

    rules_directory = {}

    found = RULE_DEFINITION.findall(text)

    for full, name in found:
        rules_directory[name] = full

    for name in order:
        full = rules_directory.pop(name, '\n')
        text = text.replace('\n' + full + '\n', '\n') + full

    return text

os.chdir("../")
with open('sql2003_grammar.grako') as f:
    sql2003 = f.read()

order = [name for _, name in RULE_DEFINITION.findall(sql2003)]

for file in glob.glob("*.grako"):
    print("Starting {file}".format(file=file))

    with open(file) as f:
        text = f.read()

    text = process(text)

    with open('_' + file, 'w') as f:
        f.write(text)

    print("Finished {file}".format(file=file))
