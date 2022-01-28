def check_number_group(num):
    try:
        if (type(num)==str and num.isdigit()) or type(num)!=str:
            if int(num)<=10:
                raise ValueError("We obtain error:Number of your group can't be less than 10")
        elif type(num)==str and num.isdigit() == False:
            raise TypeError("You entered incorrect data. Please try again.")
    except ValueError as v:
        return v
    except TypeError as t:
        return t
    else:
        return f"Number of your group {int(num)} is valid"