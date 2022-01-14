def toPostFixExpression(e):
    result=[]
    temp=[]
    for i in range(len(e)):
        if e[i].isdigit():
            result.append(e[i])
        if e[i]=="(":
            temp.append(e[i])
        if e[i]==")":
            s=len(temp)-1
            while(temp[s]!="(") and s>0:
                result+=temp.pop()
                s-=1
            while "(" in temp:
                temp.remove("(")
            while bool(temp) == True:
                result.append(temp.pop())
        if e[i] in "-+*/%":
            temp.append(e[i])
    while bool(temp) == True:
        if "(" in temp:
            temp.remove("(")
        result.append(temp.pop())
    return result