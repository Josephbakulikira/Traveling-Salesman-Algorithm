from math import sqrt

def Distance(a, b):
    return sqrt( (b.x-a.x)*(b.x-a.x) + (b.y-a.y)*(b.y-a.y) )

def SumDistance(points):
    s = 0
    for i in range(len(points)-1):
        dist = Distance(points[i], points[i+1])
        s += dist
    return s

def LexicalOrder(orderList):
    x = -1
    y = -1

    # Step 1 : Find the largest x such that Order[x]<Order[x+1]
    # (If there is no such x, Order is the last permutation.)
    for i in range(len(orderList)-1):
        if orderList[i] < orderList[i+1]:
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
    print(orderList)

    return orderList

def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)
