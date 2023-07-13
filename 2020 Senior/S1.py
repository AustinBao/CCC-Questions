# Get inputs
checks = int(input())
whole = []
for i in range(checks):
    whole.append(input())

# Make dict with time in order along with its respective position
alldict = {}
for i in whole:
    for k in i:
        if k.isspace():
            position = i[i.index(k)::]
            time = i[:i.index(k):]

            alldict[int(time)] = int(position)

alldict = dict(sorted(alldict.items()))

# Make a list from dict to iterate through later
dictlist = []
for key, value in alldict.items():
    temp = [key, value]
    dictlist.append(temp)

# Iterate through list to check fastest speed using physics.
# Find slope of distance-time graph to calculate speed.
# y2-y1 / x2-x1
max_speed = 0
for i in range(len(dictlist)):
    for j in range(i, len(dictlist)):
        if dictlist[j][0] - dictlist[i][0] == 0:
            continue
        else:
            if max_speed < abs((dictlist[j][1] - dictlist[i][1]) / (dictlist[j][0] - dictlist[i][0])):
                max_speed = abs((dictlist[j][1] - dictlist[i][1]) / (dictlist[j][0] - dictlist[i][0]))

print(max_speed)

