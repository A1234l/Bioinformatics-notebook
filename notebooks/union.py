import sys

# Get the command-line arguments
arguments = sys.argv

# The first element is the script name
script_name = arguments[0]

# The rest are the arguments
arguments = arguments[1:]

# Print the script name and arguments
print(f"Script name: {script_name}")
print(f"Arguments: {arguments}")

file = open(arguments[0], 'r')

start = []
end = []
while True:
    line = file.readline()
    if not line:
        break  # Exit the loop when there are no more lines to read
    if line[0] != "#":
        fields = line.split("\t")
        if len(fields)>7 and float(fields[2]) > 97.000:
            start.append(int(fields[6]))
            end.append(int(fields[7]))

# Create a mapping between start and end
mapping = list(zip(start, end))

# Sort the start list
start.sort()

# Update the end list based on the sorted start list
end = [value for key, value in sorted(mapping)]

mergedStart = [start[0]]
mergedEnd = [end[0]]
for i in range(len(start)):
    if i>0:
        if start[i] <= mergedEnd[-1]:
            if end[i] > mergedEnd[-1]:
                mergedEnd[-1] = end[i]
        else:
            mergedStart.append(start[i])
            mergedEnd.append(end[i])

print(mergedStart)  # Sorted start list
print(mergedEnd)    # Updated end list

if len(mergedStart) <= len(start):
    print("code works")
if len(mergedStart) == len(mergedEnd):
    print("code works 2")

file.close()

file = open(arguments[1], 'w')

file.write(str(mergedStart))
file.write("\n")
file.write(str(mergedEnd))

file.close()