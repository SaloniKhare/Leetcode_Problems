def countAndSay(n):
    res = "1"
    
    for _ in range(n - 1):
        temp = ""
        count = 1
        
        for i in range(1, len(res)):
            if res[i] == res[i - 1]:
                count += 1
            else:
                temp += str(count) + res[i - 1]
                count = 1
        
        temp += str(count) + res[-1]
        res = temp
    
    return res
