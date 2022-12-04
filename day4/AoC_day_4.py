import re

infile = "AoC_day_4_input.txt"


def contains():
    total = 0
    with open(f'{infile}', 'r') as fin:
        for line in fin:
            line = line.replace('\n', '')
            split_line = re.split(',|-', line) # splits line at both ',' and '-' using regex
            values = [eval(i) for i in split_line] # Converts list of string to list of int
            e1 = values[:2] # get the first 2 values
            e2 = values[2:] # get the last two values
            # Uncomment one answer code block at a time to see the output
            #####################
            ### Part 1 answer ###
            #####################
            # if (e1[0] <= e2[0] and e1[1] >= e2[1] or # check for lower first value and 
            #     e1[0] >= e2[0] and e1[1] <= e2[1]):  # check if corresponding second value is higher 
            #     total += 1

            #####################
            ### Part 2 answer ###
            #####################
            # if (e1[0] <= e2[0] and e1[1] >= e2[0] or # check for lower first value and  check if corresponding
            #     e2[0] <= e1[0] and e2[1] >= e1[0]):  # second value is higher than higher first value
            #     total += 1
    fin.close()
    print(total)


if __name__ == "__main__":
    contains()