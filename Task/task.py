from sys import argv
from sys import path
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'test.txt')
type = argv[1]
nov = argv[2]
fo = list(open(filename, 'r'))
if "t" != argv[1] or ("f" != argv[2] and "d" != argv[2]):
    raise Exception("You have to give arguments first t, second d or f !")
if type == "t":
    if nov == "f":
        for each_line in fo:
            if each_line.startswith("-"):
                each_line = each_line.split(";")
                print(";".join(each_line[1:3]))
    elif nov == "d":
        for each_line in fo:
            if each_line.startswith("d"):
                each_line = each_line.split(";")
                print(";".join(each_line[1:3]))