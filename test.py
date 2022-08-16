ss = 'toggle 0,499 through 999,500'
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
print(rowColumns)