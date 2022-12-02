# rock(A)(X)        = 1
# paper(B)(Y)       = 2
# scissors(C)(Z)    = 3
# win               = 6
# draw              = 3
# lose              = 0

# Iterate through all pairs in the input 
# 'Play' each round and record the score 
# Add the total score
infile = "AoC_day_2_input.txt"

def play():
    total = 0
    with open(f'{infile}', 'r') as fin:
        for line in fin:
            opp = line[0] # Opponent's choice
            me = line[2] # My choice

            # Add points for choice
            if (me == 'X'):
                total += 1
            elif (me == 'Y'):
                total += 2
            elif (me == 'Z'):
                total += 3
            
            # Uncomment one answer code block at a time to see the output
            #####################
            ### Part 1 answer ###
            #####################
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
        # print(total)
        
            #####################
            ### Part 2 answer ###
            #####################
            

        print(total)
            

if __name__ == "__main__":
    play()