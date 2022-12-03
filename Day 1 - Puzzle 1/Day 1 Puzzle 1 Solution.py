maxElfAmt = 0
maxElfInd = 0 
elfAmt = 0
elfInd = 0

#this could be simplified to just use the value from each line read
#but I have elected to store it in an array for simplicity
f = open('input.txt', 'r')
meals = f.readlines()

for i in range(len(meals)):
    #new elf begins, memoize if prior elf is the most caloric.
    if meals[i] == '\n':
        if elfAmt > maxElfAmt:
            maxElfAmt = elfAmt
            maxElfInd = elfInd
        elfAmt = 0
        elfInd += 1
    else:
        #Add meal to current elf's calorie count.
        elfAmt += int(meals[i])

#EOF so check one last time for the last elf.
if elfAmt > maxElfAmt:
    maxElfAmt = elfAmt
    maxElfInd = elfInd
    
print(maxElfAmt)
print(maxElfInd)
