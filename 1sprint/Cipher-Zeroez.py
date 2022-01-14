def Cipher_Zeroes(N):
    marks = 0
    for i in N:
        if i == '0' or i == '6' or i == '9':
            marks+=1
        elif i == '8':
            marks+=2
    if marks > 0:
        if marks%2==0:
            marks-=1
        elif marks%2==1:
            marks+=1
    return bin(marks)[2:]