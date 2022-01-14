def isPalindrome(str):
    dictionary={}
    for i in range(len(str)):
        dictionary[str[i]]=str.count(str[i])
    checking=0
    for item in dictionary.values():
        if item%2==1:
            checking+=1
    if checking>1:
        return False
    else:
        return True
