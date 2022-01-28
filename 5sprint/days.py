def day_of_week(day):
    days={1:"Monday",2:"Tuesday",3:"Wedday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
    try:
        if (type(day)==int and day not in days.keys())or(type(day)!=int and day.isdigit()==True and int(day) not in days.keys()):
            raise ValueError("There is no such day of the week! Please try again.")
        elif type(day)!=int and day.isdigit()==False:
            raise TypeError("You did not enter a number! Please try again.")
    except ValueError as v:
        return v
    except  TypeError as t:
         return t
    else:
        return days[int(day)]