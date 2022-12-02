infile = "AoC_day_1_input.txt" # File contining the challenge input


def parse_elves():
    # Initialize variables
    elves = []
    tmp = []
    escaped = "\n"
    totals = {}
    elf_num = 0
    # Open the text file contining the challenge inputs
    with open(f'{infile}', 'r') as fin:
        for line in fin: # Parse the file line by line
            if line == escaped: # If the line is blank (\n)
                elves.append(tmp) # Add the list of the previous elf's calories to the full list
                tmp = [] # Reset the temp list by creating a new one
                # If a new list is not initialized, then the previous list(s) added to the full list will be modified by new values as well
            else:
                line = line.replace(escaped, '') # remove new line characters for int convertion
                tmp.append(int(line)) # Add the item, convert to int, to the temp list
    fin.close() # Close the file
    for elf in elves: # Parse through the full list of elves
        total = 0
        for i in range (0, len(elf)): # Loop through the items for each elf and add them up
            total += elf[i]
        totals[elf_num] = total # Add the total calories of each elf to a dict with their corresponding number
        elf_num += 1

    # Uncomment one answer code block at a time to see the output
    #####################
    ### Part 1 answer ###
    #####################
    # most_cal = max(totals.items(), key=lambda x: x[1]) # Finds the highest calorie value in the dict
    # # [print(key,':',value) for key, value in totals.items()] # Prints all dict keys and values
    # print(f'\n{most_cal}') # Prints out the elf with the most calories and the amount of calories
    
    #####################
    ### Part 2 Answer ###
    #####################
    # x=list(totals.values())
    # x.sort(reverse=True)
    # x=x[:3]
    # top_3_total = 0
    # for i in x:
    #     top_3_total += i
    # print(top_3_total)

if __name__ == "__main__":
    parse_elves()
