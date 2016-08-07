import glob
import os
import re


def process(text, start=None):
    # Full Definition
    # ((.*) =\s+([\s\S]*?)\s*;\n)
    # Group1 is the full rule definition
    # Group2 is only the name of the rule
    # Group3 is the definition of the rule

    # Definitions within this definition
    # (?<!')\b\w+\b(?!')
    # Excludes keywords/terminals

    # List of rule paths to check and leave. Any not needed will be removed
    if start is None:
        start = ['cursor_specification']

    rules_required = set(start)

    rule_definition = re.compile(r"((.*) =\s+([\s\S]*?)\s*;\n)")
    rules_in_definition = re.compile(r"(?<!')\b\w+\b(?!')")
    rules_directory = {}

    found = rule_definition.findall(text)

    for _, name, definition in found:
        rules_directory[name] = rules_in_definition.findall(definition)

    found_new = True
    while found_new:
        found_new = False
        for rule_name in list(rules_required):
            if rules_directory.get(rule_name) is None:
                continue

            new = set(rules_directory.get(rule_name)) - rules_required
            rules_required = rules_required | set(rules_directory[rule_name])
            if new:
                found_new = True

    for full, name, _ in found:
        # Exclude rules starting with underscore
        if name.startswith('start'):
            continue

        if name not in rules_required:
            print name
            text = text.replace('\n' + full + '\n', '\n')

    return text

if __name__ == '__main__':
    os.chdir("../")
    for file in glob.glob("*.grako"):
        print("Starting {file}".format(file=file))

        with open(file) as f:
            text = f.read()

        text = process(text)

        with open(file, 'w') as f:
            f.write(text)

        print("Finished {file}".format(file=file))
