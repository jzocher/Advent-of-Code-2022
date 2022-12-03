infile = "AoC_day_3_input.txt"

def organize():
    values = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M',
                'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    total = 0
    group = []
    match_found = False
    matching = ''
    with open(f'{infile}', 'r') as fin:
        for line in fin:
            line = line.replace('\n', '') # Remove escape character
            # Uncomment one answer code block at a time to see the output
            #####################
            ### Part 1 answer ###
            #####################
            # s1 = slice(int(len(line)/2))
            # s2 = slice(int(len(line)/2),int(len(line)))
            # item_one = line[s1] # Get first half of string
            # item_two = line[s2] # Get second half of string

            # # Find the matching character
            # for i in item_one:
            #     for j in item_two:
            #         if i is j:
            #             matching = j
            # total += values.index(matching) + 1

            #####################
            ### Part 2 answer ###
            #####################
            # group.append(line)
            # if (len(group) == 3):
            #     done = False
            #     for i in group[0]:
            #         for j in group[1]:
            #             if done:
            #                 break
            #             elif i is j:
            #                 matching = j
            #                 match_found = True
            #             if (match_found == True):
            #                 for k in group[2]:
            #                     if matching is k:
            #                         total += values.index(matching) + 1
            #                         group = []
            #                         match_found = False
            #                         done = True
            #                         break
            #         if done:
            #             break
    fin.close() 
    print(total)


if __name__ == "__main__":
    organize()