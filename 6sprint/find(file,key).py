import json
def find_unique(data, key):
    res=[]
    if key in data:
        if type(data[key])==list:
            res+=data[key]
        else:
            res.append(data[key])
    else:
        if type(data)==dict:
            for j in data.keys():
                if type(data[j])==dict:
                    res+=find_unique(data[j], key)
                elif type(data[j])==list:
                    for z in range(len(data[j])):
                        res += find_unique(data[j][z], key)
    return res
def find(file, key):
    with open(file) as json_file:
        data = json.load(json_file)
        result,uniq=[],[]
        if data:
            if type(data)==dict:
                for k in data.keys():
                    if k==key:
                        result += find_unique(data, key)
                    elif type(data[k])==list:
                        for i in range(len(data[k])):
                            result += find_unique(data[k][i], key)
            else:
                for i in range(len(data)):
                    result+=find_unique(data[i],key)
        res_set=set(result)
        for i in res_set:
            uniq.append(i)
        return uniq[::-1]






print(find("1.json", "username"))#['Nick', 'Tom1', 'Tom', 'OneMore']