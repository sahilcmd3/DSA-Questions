#HACKER RANK

def birds(arr):
    mydict = {} #Hashmap

    for i in arr:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1

    max_count = max(mydict.values())

    req_list = [key for key, value in mydict.items() if value == max_count]
    req_list.sort()

    return req_list[0]

ans=birds(arr=[1,1,2,2,3])
print(ans)