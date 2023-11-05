import sys

# Get the command-line arguments
arguments = sys.argv

# The first element is the script name
script_name = arguments[0]

# The rest are the arguments
arguments = arguments[1:]

file = open('ecoli/union/1-2union.txt', 'r')

file1 = open('ecoli/union/1-3union.txt', 'r')

intListStart = []
intListEnd = []
lineNumber = 0
intListStart1 = []
intListEnd1 = []

for line in file:
    lineNumber = lineNumber + 1
    lineEdit = line.strip().strip("]").lstrip("[").split(", ")
    for i in lineEdit:
        if lineNumber == 1:
            intListStart.append(int(i))
        elif lineNumber == 2:
            intListEnd.append(int(i))

lineNumber = 0
for line in file1:
    lineNumber = lineNumber + 1
    lineEdit = line.strip().strip("]").lstrip("[").split(", ")
    for i in lineEdit:
        if lineNumber == 1:
            intListStart1.append(int(i))
        elif lineNumber == 2:
            intListEnd1.append(int(i))

# print(intListStart)
# print(intListEnd)
# print(" ")
# print(intListStart1)
# print(intListEnd1)

index = 0
index1 = 0
intersectComboStart = []
intersectComboEnd = []

while index<len(intListStart) and index1<len(intListStart1):
    if intListStart[index] > intListEnd1[index1]:
        index1 = index1 + 1
    elif intListStart1[index1] > intListEnd[index]:
        index = index + 1
    else:
        if intListStart[index] < intListStart1[index1] and intListEnd[index] < intListEnd1[index1]:
            intersectComboStart.append(intListStart1[index1])
            intersectComboEnd.append(intListEnd[index])
            index = index + 1
        elif intListStart[index] < intListStart1[index1] and intListEnd[index] >= intListEnd1[index1]:
            intersectComboStart.append(intListStart1[index1])
            intersectComboEnd.append(intListEnd1[index1])
            index1 = index1 + 1
        elif intListStart[index] >= intListStart1[index1] and intListEnd[index] < intListEnd1[index1]:
            intersectComboStart.append(intListStart[index])
            intersectComboEnd.append(intListEnd[index])
            index = index + 1
        else:
            intersectComboStart.append(intListStart[index])
            intersectComboEnd.append(intListEnd1[index1])
            index1 = index1 + 1

# print(intersectComboStart[0:10])
# print(" ")
# print(intersectComboEnd[0:10])

file = open(sys.argv[1], 'w')

file.write(str(intersectComboStart))
file.write("\n")
file.write(str(intersectComboEnd))

file.close()