import sys

# Get the command-line arguments
arguments = sys.argv

# The first element is the script name
script_name = arguments[0]

# The rest are the arguments
arguments = arguments[1:]

file = open(arguments[0], 'r')

file1 = open(arguments[1], 'r')

intListStartC = []
intListEndC = []
lineNumber = 0
intListStartA = []
intListEndA = []

for line in file:
    lineNumber = lineNumber + 1
    lineEdit = line.strip().strip("]").lstrip("[").split(", ")
    for i in lineEdit:
        if lineNumber == 1:
            intListStartC.append(int(i))
        elif lineNumber == 2:
            intListEndC.append(int(i))

lineNumber = 0
for line in file1:
    lineNumber = lineNumber + 1
    lineEdit = line.strip().strip("]").lstrip("[").split(", ")
    for i in lineEdit:
        if lineNumber == 1:
            intListStartA.append(int(i))
        elif lineNumber == 2:
            intListEndA.append(int(i))

# print(intListStart)
# print(intListEnd)
# print(" ")
# print(intListStart1)
# print(intListEnd1)

indexC = 0
indexA = 0
subtractComboStart = []
subtractComboEnd = []

while indexC<len(intListStartC) and indexA<len(intListStartA):
    if intListStartC[indexC] > intListEndA[indexA]: # and :
        # subtractComboStart.append(intListStartA[indexA])
        # subtractComboEnd.append(intListEndA[indexA])
        indexA = indexA + 1
    else:
        if intListStartA[indexA] < intListStartC[indexC]-1:
            subtractComboStart.append(intListStartA[indexA])
            subtractComboEnd.append(intListStartC[indexC]-1)
        indexC = indexC + 1

while indexA<len(intListStartA):
    subtractComboStart.append(intListStartA[indexA])
    subtractComboEnd.append(intListEndA[indexA])
    indexA = indexA + 1

print(subtractComboStart[0:10])
print(" ")
print(subtractComboEnd[0:10])

file = open(arguments[2], 'w')

file.write(str(subtractComboStart))
file.write("\n")
file.write(str(subtractComboEnd))

file.close()