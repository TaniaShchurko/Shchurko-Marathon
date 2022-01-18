from re import findall
from math import sqrt
def figure_perimetr(pattern):
    x1,y1,x2,y2,x4,y4,x3,y3 = map(int, findall(r'\d+', pattern))
    x,y=[x1,x2,x3,x4],[y1,y2,y3,y4]
    result=0
    for i in range(1,len(x)):
        result+=sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
    result += sqrt((x[3] - x[0]) ** 2 + (y[3] - y[0]) ** 2)
    return result