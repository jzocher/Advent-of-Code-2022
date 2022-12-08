# Majority of code for this day by /u/aaegic (reddit)
import re

infile = "AoC_day_7_input.txt"


def dirSize():
    path = list()
    tree = dict()
    with open(infile, 'r') as fin:
        for line in fin:
            line = line.replace('\n', '')
            if line == "$ cd ..":
                path.pop(-1)
                continue
            if line.startswith("$ cd"):
                path.append(line[5:])

                if ''.join(path) not in tree.keys():
                    tree.update({ ''.join(path): 0 })
                continue
            if re.search("^\d+ ", line):
                size, _ = line.split(' ')
                pwd = list()

                for d in path:
                    pwd.append(d)
                    tree.update({ ''.join(pwd): tree[''.join(pwd)] + int(size) })
                continue
    fin.close()
    #################
    # Part 1 Answer #
    #################
    #print(sum([i for i in tree.values() if i < 100000])) # Part 1

    #################
    # Part 2 Answer #
    #################
    # for i in sorted(list(tree.values())):
    #     if i > 30000000 - (70000000 - tree['/']):
    #         print(i)
    #         break


if __name__ == "__main__":
    dirSize()
