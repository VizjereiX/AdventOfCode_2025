from typing import DefaultDict


logger = None

def run(filename):
    points_by_x = DefaultDict(list)
    points_by_y = DefaultDict(list)
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            x, y = line.strip().split(",")
            points_by_x[int(x)].append(int(y))
            points_by_y[int(y)].append(int(x))


    bounding_points = set()

    for x, ys in points_by_x.items():
        ys.sort()
        bounding_points.add((x, ys[0]))
        bounding_points.add((x, ys[-1]))

    for y, xs in points_by_y.items():
        xs.sort()
        bounding_points.add((xs[0], y))
        bounding_points.add((xs[-1], y))

    max_area = 0

    bounding_points = list(bounding_points)


    for i in range(len(bounding_points)-1):
        p1 = bounding_points[i]
        for j in range(i+1, len(bounding_points)):
            p2 = bounding_points[j]
            area = (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)
            if area > max_area:
                max_area = area


    return str(max_area)
