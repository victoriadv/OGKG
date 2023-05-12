from math import ceil
from random import uniform
from point import *
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np


def preprocess():
    points = []
    n = int(input("Enter number - amount of vertexes of the polygon: "))
    print("Enter vertexes of the polygon (x and y per line). Warning those points MUST create convex hull.")
    for i in range(0, n):
        x, y = map(float, input().split())
        points.append(Point(x, y))
    return points


def yourInput():
    tests = []
    n = int(input("Enter number - amount of points to be tested: "))
    print("Enter point(x and y per line).")
    for i in range(0, n):
        x, y = map(float, input().split())
        tests.append([x, y])
    return tests


def randomInput(min_x, max_x, min_y, max_y):
    tests = []
    n = int(input("Enter number - amount of points to be tested: "))

    for i in range(0, n):
        x = uniform(min_x, max_x)
        y = uniform(min_y, max_y)
        tests.append([x, y])
    return tests


def testPoints(tri):
    min_x = ceil(np.min(tri.points[:, 0]))
    max_x = ceil(np.max(tri.points[:, 0]))
    min_y = ceil(np.min(tri.points[:, 1]))
    max_y = ceil(np.max(tri.points[:, 1]))
    x_avg = (min_x + max_x) / 2
    y_avg = (min_y + max_y) / 2

    if x_avg > 0:
        min_x -= x_avg
        max_x += x_avg
    else:
        min_x += x_avg
        max_x -= x_avg

    if y_avg > 0:
        min_y -= y_avg
        max_y += y_avg
    else:
        min_y += y_avg
        max_y -= y_avg

    how = input("Enter 0 if you want to add points yourself or something else if you want random generated points: ")
    try:
        if int(how) == 0:
            return yourInput()
        else:
            return randomInput(min_x, max_x, min_y, max_y)
    except ValueError:
        return randomInput(min_x, max_x, min_y, max_y)


def locatePoints(tri, list):
    inside = []
    outside = []
    for p in list:
        res = tri.find_simplex(p) >= 0
        print(f"{p} inside: {res}")
        if res:
            inside.append(p)
        else:
            outside.append(p)
    drawPoints(inside, 'blue')
    drawPoints(outside, 'black')


def drawPoints(points, color):
    x, y = zip(*points)
    plt.scatter(x, y, c=color)


points = getSorted(preprocess())

pointsList = []
for p in points:
    pointsList.append([p.x, p.y])
pointsList = np.array(pointsList)

tri = Delaunay(pointsList)

flag = True

while flag:
    plt.triplot(pointsList[:, 0], pointsList[:, 1], tri.simplices)
    plt.plot(pointsList[:, 0], pointsList[:, 1], 'o', color='red')

    locatePoints(tri, testPoints(tri))

    plt.show()
    print()
    how = input("Enter 0 if you want to test points again or something else to end program: ")
    try:
        if int(how) != 0:
            flag = False
    except ValueError:
        flag = False