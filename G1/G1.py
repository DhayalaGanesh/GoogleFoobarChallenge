
data = [5, 10, 15, 10, 7]
n = 1
returnedValue = []
def solution(data, n):
    if n==0:
        return []
    countDictionary = dict()
    for x in data:
        if x in countDictionary:
            countDictionary[x] = countDictionary[x] + 1
        else:
            countDictionary[x] = 1

    for x in range(0,len(data)):
        if countDictionary[data[x]]<=n:
            returnedValue.append(data[x])
    print returnedValue
    return returnedValue
    
solution(data,1)