
#Please Pass the Coded Messages
#==============================

#You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

#You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

#Languages
#=========

#To provide a Java solution, edit Solution.java
#To provide a Python solution, edit solution.py

#Test cases
#==========
#Your code should pass the following test cases.
#Note that it may also be run against hidden test cases not shown here.

#-- Java cases --
#Input:
#Solution.solution({3, 1, 4, 1})
#Output:
#    4311

#Input:
#Solution.solution({3, 1, 4, 1, 5, 9})
#Output:
#    94311

#-- Python cases --
#Input:
#solution.solution([3, 1, 4, 1])
#Output:
#    4311

#Input:
#solution.solution([3, 1, 4, 1, 5, 9])
#Output:
#    94311
def solution(l):
    modulus = []
    indices = []
    count = 0
    twoCount = 0
    oneArray = []
    twoArray = []
    returnedValue = ""
    valuesArray = []
    def hashkey(v):
        return (v[0]*10)+(9-l[v[1]])
    for i in range(0,len(l)):
        modulus.append((l[i]%3,i))

    modulus = sorted(modulus, key=hashkey)
    for x in range(0,len(modulus)):
        if modulus[x][0] == 0:
            indices.append(modulus[x][1])
        elif modulus[x][0] == 1:
            oneArray.append(modulus[x][1])
            count = count + 1
            if(count == 3): 
                indices.extend(oneArray)
                oneArray = []
                count=0
        elif modulus[x][0] == 2:
            twoArray.append(modulus[x][1])
            twoCount = twoCount + 1
            if(twoCount == 3): 
                indices.extend(twoArray)
                twoArray = []
                twoCount=0

    for x in range(0,min(len(oneArray), len(twoArray))):
        indices.append(oneArray[x])
        indices.append(twoArray[x])

    for x in range(0,len(indices)):
        valuesArray.append(l[indices[x]])

    valuesArray.sort(reverse = True)
    
    for x in range(0,len(valuesArray)):
        returnedValue = returnedValue + str(valuesArray[x])
    if(len(returnedValue) == 0):
        return 0
    return returnedValue

print(solution([3, 1, 4, 1, 5, 9]))