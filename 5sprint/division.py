def divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError(f"Oops, {numerator}/{denominator}, division by zero is error!!!" )
        elif type(numerator)==str or type(denominator)==str:
            raise ValueError("Value Error! You did not enter a number!")
    except ZeroDivisionError as z:
        return z
    except ValueError as v:
        return v
    else:
        return f"Result is {numerator / denominator}"