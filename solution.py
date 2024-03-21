
def solvepart1():
    #format data
    data = fileRead("input.txt")
    histories = []
    for row in data:
        rowInt = row.strip().split(" ")
        histories.append([int(i) for i in rowInt])

    #make predictions
    sum = 0
    for row in histories:
        sequences = [row]
        while not ( len(set(sequences[-1])) == 1 and sequences[-1][0] == 0):
            newSequence = []
            for i in range(len(sequences[-1])-1):
                newSequence.append(sequences[-1][i+1]-sequences[-1][i])
            sequences.append(newSequence)
        for i in reversed(range(len(sequences)-2)):
            sequences[i].append(sequences[i][-1]+sequences[i+1][-1])
        sum = sum + sequences[0][-1]
    print(sum)

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart1()