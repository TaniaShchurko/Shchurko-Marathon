import re
def max_population(data):
    result={}
    for i in range(len(data)):
        name=re.findall(r'[a-z]{2}_[a-z]*',data[i])
        temp=re.findall(r'\d+,[yn]',data[i])
        if temp:
            temp=temp[0].split(',')
            result[int(temp[0])]=name[0]
    max_num=max(result.keys())
    return  (result[max_num],max_num)
