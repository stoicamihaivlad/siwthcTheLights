matrix ={}

for i in range(1000):
    for j in range(1000):
        matrix[f'{i},{j}'] = 0


def countLightsOn(dic):
    counter = 0
    for val in dic.values():
        if val == 1:
            counter += 1
    return counter


def turnOn(dic,r1,c1,r2,c2):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            dic[f'{i},{j}'] = 1

def turnOff(dic,r1,c1,r2,c2):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            dic[f'{i},{j}'] = 0

def toggle(dic,r1,c1,r2,c2):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            dic[f'{i},{j}'] = 1 - dic[f'{i},{j}']


# def turnOnV2(dic,r1,c1,r2,c2):
#     for i in range(r1,r2+1):
#         for j in range(c1,c2+1):
#             dic[f'{i},{j}'] += 1

# def turnOffV2(dic,r1,c1,r2,c2):
#     for i in range(r1,r2+1):
#         for j in range(c1,c2+1):
#             if (dic[f'{i},{j}']):
#                 dic[f'{i},{j}'] -=1

# def toggleV2(dic,r1,c1,r2,c2):
#     for i in range(r1,r2+1):
#         for j in range(c1,c2+1):
#             dic[f'{i},{j}'] += 2


def getRowsAndColumns(ss): #where ss is a string
    rowColumns = []
    newString = ''
    for ch in range(len(ss)):

        if ss[ch].isnumeric():
            newString += ss[ch]
            
        if newString and ss[ch] == ",":
            rowColumns.append(int(newString))
            newString = ''
        if newString and (ss[ch].isspace()) == True:
            rowColumns.append(int(newString))
            newString = ''
        if newString and ch == len(ss)-1:
            rowColumns.append(int(newString))
            newString = ''
    return rowColumns

with open('input.txt', 'r',encoding='ISO-8859-1') as inputFile:
    for line in inputFile:
        rowColumns = []
        try:
            if 'turn on' in line:
                indexes = getRowsAndColumns(line)
                print(f'Turning the lights on and assign 1 from {indexes[0]},{indexes[1]} through {indexes[2]},{indexes[3]}')
                turnOn(matrix,indexes[0],indexes[1],indexes[2],indexes[3])
                print(f'Now are {countLightsOn(matrix)} lights On')
            elif 'turn off' in line:
                indexes = getRowsAndColumns(line)
                print(f'Turning the lights off and assign 0 from {indexes[0]},{indexes[1]} through {indexes[2]},{indexes[3]}')
                print(indexes)
                turnOff(matrix,indexes[0],indexes[1],indexes[2],indexes[3])
                print(f'Now are {countLightsOn(matrix)} lights On')
            elif 'toggle' in line:
                print(f'Switch the lights from {indexes[0]},{indexes[1]} through {indexes[2]},{indexes[3]}')
                indexes = getRowsAndColumns(line)
                toggle(matrix,indexes[0],indexes[1],indexes[2],indexes[3])
                print(f'Now are {countLightsOn(matrix)} lights On')
        except:
            print("Please double check if the input.txt was defined accordingly to the examples provided")

    inputFile.close()
