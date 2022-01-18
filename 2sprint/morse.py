def morse_number(number):
    result=""
    for i in range(3):
        num=int(number[i])
        if num==0:
            result+="-----"
        elif num>0 and num<6:
            for i in range(num):
                result+="."
            while num<5:
                result+="-"
                num+=1
        elif num>=6:
            for i in range(5,num):
                result+="-"
            while num<10:
                result+="."
                num+=1
        result+=" "
    return result
print(morse_number("295"))