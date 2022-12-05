infile = "AoC_day_5_input.txt"


def stackCrates():
    top_crates = ''
    crates = {
        1: ['B','G','S','C'],
        2: ['T','M','W','H','J','N','V','G'],
        3: ['M','Q','S'],
        4: ['B','S','L','T','W','N','M'],
        5: ['J','Z','F','T','V','G','W','P'],
        6: ['C','T','B','G','Q','H','S'],
        7: ['T','J','P','B','W'],
        8: ['G','D','C','Z','F','T','Q','M'],
        9: ['N','S','H','B','P','F']
    }
    with open(f'{infile}', 'r') as fin:
        for line in fin:
            line = line.replace('\n','')
            split_raw = line.split(' ')
            num_of_crates = int(split_raw[1])
            stack_from = int(split_raw[3])
            stack_to = int(split_raw[5])
            # Uncomment one answer code block at a time to see the output
            #####################
            ### Part 1 answer ###
            #####################
            # for c in range(num_of_crates):
            #     c = crates[stack_from].pop()
            #     crates[stack_to].append(c)
            #####################
            ### Part 2 answer ###
            #####################
            # if num_of_crates == len(crates[stack_from]):
            #     moving = crates[stack_from]
            #     for i in moving:
            #         crates[stack_to].append(i)
            #     crates[stack_from].clear()
            # else:
            #     moving = crates[stack_from][:len(crates[stack_from])-num_of_crates-1:-1]
            #     del crates[stack_from][:len(crates[stack_from])-num_of_crates-1:-1]
            #     for i in moving[::-1]:
            #         crates[stack_to].append(i)

        for key,value in crates.items():
            top_crates += str(value[len(value)-1])
    fin.close()
    print(top_crates)


if __name__ == "__main__":
    stackCrates()