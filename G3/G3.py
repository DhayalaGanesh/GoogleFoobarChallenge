

def solution(l):
    maxLen = [0,0,0]
    lenDictionary = dict()
    maxOfLen = 0
    for x in l:
        eachVersion = x.split(".")
        for i in range(0,len(eachVersion)):
            maxLen[i] = max(maxLen[i],len(eachVersion[i]))
        lenDictionary[x] = str(len(x))
        maxOfLen = max(maxOfLen, len(str(len(x))))
    for x in l:
        curLen = len(lenDictionary[x])
        while curLen < maxOfLen:
            lenDictionary[x] = "0" + lenDictionary[x]
            curLen = curLen + 1
    def hashkey(v):
        splittedArray = v.split(".")
        while len(splittedArray)<3:
            splittedArray.append("0")
        for i in range(0,3):
            while len(splittedArray[i]) < maxLen[i]:
                splittedArray[i] = "0" + splittedArray[i]
        hashVal = splittedArray[0]+ "."+  splittedArray[1] + "." + splittedArray[2]
        
        hashVal = hashVal + lenDictionary[v]
        return hashVal
    l = sorted(l, key=hashkey)
    return l

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
#print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))