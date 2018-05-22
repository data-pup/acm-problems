'''

3 <-- number of data sets
1 10 1234 < -- index, base, value
2 3 98765
3 16 987654321



-> take the base number, and incrementally check each power to determine if it exceeds the integer
-> once it exceeds, then

'''

def squareSum(digitList):
    runningSum = 0
    for i in digitList:
        runningSum+=pow(i,2)
    return runningSum


def calculateIntegerInBase(base, integerVal):
    baseIndex = 0
    while(True):
        if (pow(base,baseIndex) > integerVal):
            pass # begin algorithm to check lesser powers
            break
        baseIndex+=1
    baseIndex-=1

    remaining = integerVal
    digits = []
    
    while baseIndex >= 0:
        nextDigit = base - 1
        nextAmount = nextDigit * pow(base, baseIndex)
        while nextAmount > remaining:
            nextDigit -= 1
            nextAmount = nextDigit * pow(base, baseIndex)
        digits.append(nextDigit)
        remaining -= nextAmount
        baseIndex-=1
    return digits

if __name__ == '__main__':
    input1 = (1, 10, 1234)
    input2 = (2, 3, 98765)
    input3 = (3, 10, 987654321)

    digitlist = calculateIntegerInBase(16,987654321)
    print (squareSum(digitlist))
