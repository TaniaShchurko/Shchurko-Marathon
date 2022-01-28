def check_odd_even(num):
    try:
        if type(num)==str and num.isdigit()==False:
            raise TypeError("You entered not a number.")
    except TypeError as t:
        return t
    else:
        if int(num)%2==0:
            return "Entered number is even"
        elif int(num)%2==1:
            return "Entered number is odd"