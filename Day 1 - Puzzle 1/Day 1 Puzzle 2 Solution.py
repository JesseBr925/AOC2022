elfAmt = 0
elfInd = 0

#this could be simplified to just use the value from each line read
#but I have elected to store it in an array for simplicity
f = open('input.txt', 'r')
meals = f.readlines()
calTotals = []

for i in range(len(meals)):
    #new elf begins, memoize if prior elf into the list.
    if meals[i] == '\n':
        calTotals.append((elfAmt, elfInd))
        elfAmt = 0
        elfInd += 1
    else:
        #Add meal to current elf's calorie count.
        elfAmt += int(meals[i])

#EOF so add last elf
calTotals.append((elfAmt, elfInd))

#Sort based on calories
sort = sorted(calTotals, key=lambda x: x[0])
sort.reverse()

total = int(sort[0][0]) + int(sort[1][0]) + int(sort[2][0])
print(total)

