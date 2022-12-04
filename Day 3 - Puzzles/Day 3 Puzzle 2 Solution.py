from collections import Counter

#helper function to find priority
def priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

f = open('input.txt', 'r')
input = f.readlines()

#cleaning up our input a bit.
for i in range(len(input)):
    input[i] = input[i].replace('\n','')  

#to find our total priority
totalPriority = 0

##O(len(input)/3) complexity.
for i in range(0,len(input),3):
    #split the input into groups, bags a, b, and c.
    a = input[i]   
    b = input[i+1]
    c = input[i+2]
    
    #we hash bag a (first bag) into a dictionary
    ##O(a) complexity.

    #we hash bag b (second bag) into a dictionary
    ##O(b) complexity.
    
    d = Counter(a)
    e = Counter(b)
    
    #we iterate through bag c(third bag) to see if its items are
    #also in an item in a and b, if so this is the badge.

    ##O(c) complexity.
    for j in range(len(c)):
        
        ##O(1) complexity.
        if c[j] in d.keys():
            
            ##O(1) complexity.
            if c[j] in e.keys():
                #as soon as we find the item that is a badge and is in
                #both prior bags calculate priority add it to total and 
                totalPriority += priority(c[j])

                #we don't intend to count more than once in each group.
                #so we break.
                break

###Could likely be done with better time complexity but this feels clean.
##O(len(input/3)*O(a+b+c))
print(totalPriority)



