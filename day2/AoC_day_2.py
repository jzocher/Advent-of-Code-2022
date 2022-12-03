# rock(A)(X = Lose)     = 1
# paper(B)(Y = draw)    = 2
# scissors(C)(Z = win)  = 3
# win                   = 6
# draw                  = 3
# lose                  = 0

infile = "AoC_day_2_input.txt"

def play():
    total = 0
    with open(f'{infile}', 'r') as fin:
        for line in fin:
            opp = line[0] # Opponent's choice
            me = line[2] # My choice

            # Uncomment one answer code block at a time to see the output
            #####################
            ### Part 1 answer ###
            #####################
            # # Add points for choice
            # if (me == 'X'):
            #     total += 1
            # elif (me == 'Y'):
            #     total += 2
            # elif (me == 'Z'):
            #     total += 3
            # # Add points for win/draw/loss
            # # Win
            # if(opp == 'A' and me == 'Y' or
            #     opp =='B' and me =='Z' or
            #     opp =='C' and me =='X'):
            #     total += 6
            # # Draw
            # elif(opp == 'A' and me == 'X' or
            #     opp == 'B' and me == 'Y' or
            #     opp == 'C' and me == 'Z'):
            #     total += 3
            # # Lose - don't need to check (0 score)
        
            #####################
            ### Part 2 answer ###
            #####################
            if (me == 'X'): # lose
                if (opp == 'A'):
                    total += 3 # 3(scissors) + 0(lose)
                if (opp == 'B'):
                    total += 1 # 1(rock) + 0(lose)
                if (opp == 'C'):
                    total += 2 # 2(paper) + 0(lose)
            if (me == 'Y'): # draw
                if (opp == 'A'):
                    total += 4 # 1(rock) + 3(draw)
                if (opp == 'B'):
                    total += 5 # 2(paper) + 3(draw)
                if (opp == 'C'):
                    total += 6 # 3(scissors) + 3(draw)
            if (me == 'Z'): # win
                if (opp == 'A'):
                    total += 8 # 2(paper) + 6(win)
                if (opp == 'B'):
                    total += 9 # 3(scissors) + 6(win)
                if (opp == 'C'):
                    total += 7 # 1(rock) + 6(win)
        print(total)
            

if __name__ == "__main__":
    play()