from math import sqrt

def Distance(a, b):
    return sqrt( (b.x-a.x)*(b.x-a.x) + (b.y-a.y)*(b.y-a.y) )

def SumDistance(points):
    s = 0
    for i in range(len(points)-1):
        dist = Distance(points[i], points[i+1])
        s += dist
    return s
