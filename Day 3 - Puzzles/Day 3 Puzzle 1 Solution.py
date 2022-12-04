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

for i in range(len(input)):
    #split the string input in halfs (first and second compartment, a and b)
    a = input[i][:len(input[i])//2]    
    b = input[i][len(input[i])//2:]
    
    #we hash string a (first compartment) into a dictionary
    d = Counter(a)
    
    #we iterate through string b (second compartment) to see if its also in a.
    for j in range(len(b)):        
        if b[j] in d.keys():
            #as soon as we find the item that is an error
            #calculate priority add it to total and 
            totalPriority += priority(b[j])

            #we don't intend to count more than once in each bag.
            #so we break.
            break
        
print(totalPriority)



