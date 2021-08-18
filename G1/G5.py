#Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for the LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in a bit of sabotage while you're at it -- so you took the job gladly. 

#Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

#The fuel control mechanisms have three operations: 

#1) Add one fuel pellet
#2) Remove one fuel pellet
#3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

#Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

#For example:
#solution(4) returns 2: 4 -> 2 -> 1
#solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
#Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 
def solution(l):
    lcopy = str(l)
    l = []
    l[:0] = lcopy
    binaryString = []
    def divideByTwo(t):
        carry = 0
        startIndex = 0
        if int(t[0])==1:            
            carry = 1
            startIndex = 1
        y = 0
        z = 0
        result = []
        for i in range(startIndex,len(t)):
            y = carry*10+int(t[i])
            z = int(y/2)
            result.append(str(z))
            carry = y%2
        return result
    while len(l)>1 or int(l[0])>1:
        binaryString.append(str(int(l[-1])%2))
        l[-1] = str(int(l[-1]) - int(l[-1]) %2 )
        l = divideByTwo(l)
    answer = 0
    
    binaryString.append("1")
    i = 0
    while i < len(binaryString):
        if(binaryString[i] == "0"):
            answer = answer + 1
        elif(binaryString[i] == "1"):
            consecutiveOnes = 1
            for j in range(i+1, len(binaryString)):
                if(binaryString[j] == "1"):
                    consecutiveOnes = consecutiveOnes + 1
                else:
                    break
            if consecutiveOnes == 1:
                if(i!=len(binaryString)-1):
                    answer = answer + 2
            else:
                answer = answer + 1 + consecutiveOnes
                i = i + consecutiveOnes - 1
                if(i+1 < len(binaryString)): 
                    binaryString[i+1] = "1"
            if consecutiveOnes == 2 and i >= len(binaryString)-1:
                answer = answer-1
        i = i+1
    return answer

print(solution("13"))

