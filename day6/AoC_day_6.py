infile = "AoC_day_6_input.txt"

def packetMarker():
    total_char = 0
    with open(infile, 'r') as fin:
        data_stream = fin.read()
    fin.close()
    rolling_data = []
    for c in data_stream:
        if (len(rolling_data) < 4):
            rolling_data.append(c)
            total_char += 1
        else:
            for i in rolling_data:
                if rolling_data.count(i) > 1:
                    rolling_data.pop(0)
                    rolling_data.append(c)
                    total_char += 1
                    break
    print(total_char)

def messageMarker():
    total_char = 0
    with open(infile, 'r') as fin:
        data_stream = fin.read()
    fin.close()
    rolling_data = []
    for c in data_stream:
        if (len(rolling_data) < 14):
            rolling_data.append(c)
            total_char += 1
        else:
            for i in rolling_data:
                if rolling_data.count(i) > 1:
                    rolling_data.pop(0)
                    rolling_data.append(c)
                    total_char += 1
                    break
    print(total_char)
                

            

if __name__ == "__main__":
    packetMarker()
    messageMarker()