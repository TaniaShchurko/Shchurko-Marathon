class MyError(Exception):
    def __init__(self, number):
        self.message = f"You input negative number: {number}. Try again."
        super().__init__(self.message)

    def __str__(self):
        return self.message


def check_positive(number):
    try:
        if type(number) == str and number.isdigit() == False and '-' not in number:
            raise ValueError("Error type: ValueError!")
        elif float(number) < 0:
            raise MyError(float(number))
    except ValueError as v:
        return v
    except MyError as m:
        return m
    else:
        return f"You input positive number: {float(number)}"