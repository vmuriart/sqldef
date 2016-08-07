import grako
import glob
import os

if __name__ == '__main__':
    os.chdir("../")
    for file in glob.glob("*.grako"):
        print("Starting {file}".format(file=file))

        with open(file) as f:
            b = f.read()

        try:
            text = grako.gencode(grammar=b)

        except Exception as e:
            print("Error {file}".format(file=file))
            print(e)

        else:
            with open("./parsers/" + file[:-5] + 'py', 'w') as f:
                f.write(text)
            print("Finished {file}".format(file=file))
