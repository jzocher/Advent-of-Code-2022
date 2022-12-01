infile = "AoC_day_1_input.txt"
answer = ""


def parse_elves():
    elves = []
    elf_num = 0
    tmp_arr = []
    escaped = "\n"
    with open(f'{infile}', 'r') as fin:
        for line in fin:
            # print(f"Parsing line {line}")
            # separate the elves
            if line == escaped:
                ("new line found")
                elves.append(tmp_arr)
                # tmp_arr.clear()
                elf_num += 1
            else:
                # print("Added to array")
                line = line.replace(escaped, '')
                int(line)
                tmp_arr.append(line)
        print("Completed parsing")
    fin.close()
    for elf in elves:
        print(elves[elf])


if __name__ == "__main__":
    parse_elves()
