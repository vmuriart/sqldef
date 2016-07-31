import grako
import glob
import os

if __name__ == '__main__':
    os.chdir("../")
    for file in glob.glob("*.grako"):
        print("Starting {file}".format(file=file))
        with open(file) as f:
            b = f.read()
        text = grako.gencode(grammar=b)

        with open("./parsers/" + file[:-5] + 'py', 'w') as f:
            f.write(text)

        print("Finished {file}".format(file=file))
