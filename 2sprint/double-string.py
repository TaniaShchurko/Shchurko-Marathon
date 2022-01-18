def double_string(data):
    count,start=0,0
    while start<len(data):
        check=0
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i]+data[j]==data[start] and check==0:
                    count+=1
                    check=1
        start+=1
    return count
