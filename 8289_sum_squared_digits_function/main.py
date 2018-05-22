'''

3 <-- number of data sets
1 10 1234 < -- index, base, value
2 3 98765
3 16 987654321



-> take the base number, and incrementally check each power to determine if it exceeds the integer
-> once it exceeds, then 

'''

def calculateIntegerInBase(base, integerVal):
    baseIndex = 0
    
    while(True):
        if (pow(base,baseIndex) > integerVal):
            pass # begin algorithm to check lesser powers
            print baseIndex
            break

        baseIndex+=1

    
            

        
input1 = (1, 10, 1234) 
input2 = (2, 3, 98765) 
input3 = (3, 10, 987654321) 
calculateIntegerInBase(10,1234)


