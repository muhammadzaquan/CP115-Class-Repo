scoreA = int(input())
scoreB = int(input())
pointA = 0
pointB = 0
if scoreA > scoreB:
    pointA = pointA + 3
    if scoreB < 1:
        pointA = pointA + 1
else:
    if scoreB > scoreA:
        pointB = pointB + 3
        if scoreA < 1:
            pointB = pointB + 1
    if scoreA == scoreB:
        pointB = 1
        pointA = 1
print(pointA)
print(pointB)