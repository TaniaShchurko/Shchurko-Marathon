import cmath
def solve_quadric_equation(a, b, c):
    try:
       if a==0:
           raise ZeroDivisionError("Zero Division Error")
       elif type(a)==str or type(b)==str or type(c)==str:
           raise TypeError("Could not convert string to float")
       else:
           d=b**2-4*a*c
           x1=(-b-cmath.sqrt(d))/2*a
           x2=(-b+cmath.sqrt(d))/2*a
    except ZeroDivisionError as z:
        return z
    except TypeError as t:
        return t
    else:
        return f"The solution are x1={x1} and x2={x2}"