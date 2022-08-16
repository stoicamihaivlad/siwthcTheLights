
def toggle(led):
    led = 1 - led
    return led


# mL = [{
#         'id': (0,0),
#         'val': 0
#     }]

#where mL is matrixLightning
#mL is a list containing first an index(row,column) 
# and immediately after that
#                              a dictionary {id: (row, column}, val: 0)}

mL=[]

for i in range(0,1000):
    for j in range(0,1000):
        mL.append(f'({i},{j})')
        mL.append(
            {
                'id' : (i,j),
                'val': 0
            }
        )

def findLightAtIndex(l,r,c):
    """
    
    This is a simple function that receives as arguments the list, row and column of the light you are interested in

    Returns a dictionary with the 'id' (row, column) and with the 'value' indicating light is on (1) or off (0)

    Example: If you want to turn on light at (500,499)

    indx = findLightAtIndex(mL, 500, 499)
    mL[indx]['val'] = 1

    """
    return (l[l.index(f'({r},{c})') + 1])

def countLightsOn(l):
    """
    Takes the matrix(list) as arguments and returns the number of lights that are on
    """
    counter = 0
    for i in range(len(l)):
        try:
            if l[i]['val'] == 1:
                counter += 1
        except TypeError:
            pass
    return counter

def testing():
# print(countLightsOn(mL))
# for i in range(1,15,2):
#     mL[i]['val'] = 1
# print(countLightsOn(mL))

# print(mL.index('(999,999)'))
# print(mL[mL.index('(999,999)') +1])
# print(mL[499]['val'])
# mL[499]['val'] = 1 - mL[499]['val']
# print(mL[499]['val'])
    pass


def turnOn(l,r1,c1,r2,c2):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            l[l.index(f'({i},{j})') + 1]['val'] = 1 #check

def turnOff(l,r1,c1,r2,c2):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            l[l.index(f'({i},{j})') + 1]['val'] = 0 #check

def toggle(l,r1,c1,r2,c2):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            l[l.index(f'({i},{j})') + 1]['val'] = 1 - l[l.index(f'({i},{j})') + 1]['val'] #check


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
                # print(indexes)
                turnOn(mL,indexes[0],indexes[1],indexes[2],indexes[3])
                print(f'Now are {countLightsOn(mL)} lights On')
            elif 'turn off' in line:
                indexes = getRowsAndColumns(line)
                print(f'Turning the lights off and assign 0 from {indexes[0]},{indexes[1]} through {indexes[2]},{indexes[3]}')
                print(indexes)
            elif 'toggle' in line:
                print(f'Switch the lights from {indexes[0]},{indexes[1]} through {indexes[2]},{indexes[3]}')
                indexes = getRowsAndColumns(line)
                print(indexes)
        
        except:
            print("Please double check if the input.txt was defined accordingly to the examples provided")

    inputFile.close()
