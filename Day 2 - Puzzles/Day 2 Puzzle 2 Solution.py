f = open('input.txt', 'r')
input = f.readlines()

#cleaning up our input a bit.
for i in range(len(input)):
    input[i] = input[i].replace('\n','')
    input[i] = input[i].split(' ')    

total = 0
#now to iterate and calculate our total score.
for j in range(len(input)):
    val = set(input[j])
    print(val)
    #since there are only 12 possible outcomes to a "match"
    #i've decided to use a simple if tree, is also efficient.
    #we'll have to add a bit more logic in now with the update
    #of instructions.
    if val == {'A' , 'X'}:
        total += 3 + 0
    elif val == {'A' , 'Y'}:
        total += 1 + 3
    elif val == {'A' , 'Z'}:
        total += 2 + 6
    elif val == {'B' , 'X'}:
        total += 1 + 0
    elif val == {'B' , 'Y'}:
        total += 2 + 3
    elif val == {'B' , 'Z'}:
        total += 3 + 6
    elif val == {'C' , 'X'}:
        total += 2 + 0
    elif val == {'C' , 'Y'}:
        total += 3 + 3
    elif val == {'C' , 'Z'}:
        total += 1 + 6
            
print(total)
