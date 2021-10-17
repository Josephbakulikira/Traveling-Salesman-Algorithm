from math import sqrt
from random import randint, uniform

def Distance(a, b):
    return sqrt( (b.x-a.x)*(b.x-a.x) + (b.y-a.y)*(b.y-a.y) )

def SumDistance(points):
    s = 0
    for i in range(len(points)):
        dist = Distance(points[i], points[(i+1) % len(points)])
        s += dist
    return s

def PickSelection(myList, probabilities):
    i = 0
    r = uniform(0, 1)

    while r > 0:
        r -= probabilities[i]
        i += 1
    i -= 1
    return myList[i].copy()

def LexicalOrder(orderList):
    x = -1
    y = -1

    # Step 1 : Find the largest x such that Order[x]<Order[x+1]
    # (If there is no such x, Order is the last permutation.)
    for i in range(len(orderList)):
        if orderList[i] < orderList[(i+1)%len(orderList)]:
            x = i
    if x == -1:
        return orderList

    # Step 2 : Find the largest y such that Order[x]<Order[y].
    for i in range(len(orderList)):
        if orderList[x] < orderList[i]:
            y = i
    # Step 3 : Swap Order[x] and Order[y].
    orderList[x], orderList[y] = orderList[y], orderList[x]

    # Step 4 : Reverse Order[x+1 .. n].
    RightSidereversed = orderList[x+1:][::-1]
    orderList = orderList[:x+1]
    orderList.extend(RightSidereversed)
    # print(orderList)

    return orderList

def translateValue(value, min1, max1, min2, max2):
    return min2 + (max2 - min2)* ((value-min1)/(max1-min1))

def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)
