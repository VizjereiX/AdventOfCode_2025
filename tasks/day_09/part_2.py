from typing import DefaultDict


logger = None

def is_inside(x1, y1, x2, y2, points):
    for i in range(len(points)):
        a = points[i]
        b = points[(i + 1) % len(points)]
        if max(a[0], b[0]) <= x1 or x2 <= min(a[0], b[0]) or max(a[1], b[1]) <= y1 or y2 <= min(a[1], b[1]):
            continue
        return False
    return True

def run(filename):
    points = list()
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            x, y = line.strip().split(",")
            points.append((int(x), int(y)))

    max_area = 0
    for i in range(len(points) - 1):
        for j in range(i, len(points)):
            x1 = min(points[i][0], points[j][0])
            y1 = min(points[i][1], points[j][1])
            x2 = max(points[i][0], points[j][0])
            y2 = max(points[i][1], points[j][1])
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > max_area:
                logger.debug(f"Bigger area: {area} with points {points[i]} and {points[j]}")
                if is_inside(x1, y1, x2, y2, points):
                    logger.debug(f"  It is inside!")
                    max_area = area
        
    return str(max_area)
