import math

logger = None

def run(filename):
    wire_count = 1000 if "data" in filename else 10
    points = []
    clusters = []
    distances = []
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip().split(",")
            points.append([int(x) for x in line] + [len(clusters)])
            clusters.append([len(clusters)])
            distances.append({})



    for i in range(len(points)):
        distances[i][i] = float("inf")
        for j in range(i + 1, len(points)):
            dist = (points[i][0] - points[j][0])**2  + (points[i][1] - points[j][1]) ** 2 + (points[i][2] - points[j][2])**2
            dist = dist **0.5
            distances[i][j] = dist
            distances[j][i] = dist

    cluster_count = len(clusters)

    while cluster_count > 1:
        logger.info(f"Remaining clusters: {cluster_count}")
        min_dist = float("inf")
        min_pair = (-1, -1) 

        for a in range(len(points)):
            for b in range(a + 1, len(points)):
                if distances[a][b] < min_dist and points[a][3] != points[b][3]:
                    min_dist = distances[a][b]
                    min_pair = (a, b)

        logger.info(f"{points[min_pair[0]][0:3]} {points[min_pair[1]][0:3]} {min_dist}")

        cluster_num = min(points[min_pair[0]][3], points[min_pair[1]][3])
        old_cluster_num = max(points[min_pair[0]][3], points[min_pair[1]][3])

        distances[min_pair[0]][min_pair[1]] = float("inf")
        distances[min_pair[1]][min_pair[0]] = float("inf")

        if cluster_num == old_cluster_num:
            continue
        
        for p in points:
            if p[3] == old_cluster_num:
                p[3] = cluster_num

        clusters[cluster_num].extend(clusters[old_cluster_num])
        clusters[old_cluster_num] = []
        for p in clusters[cluster_num]:
            for q in clusters[old_cluster_num]:
                distances[p][q] = float("inf")
                distances[q][p] = float("inf")

        cluster_count -= 1

    logger.info(f"{points[min_pair[0]][0]} {points[min_pair[1]][0]}")

    return str(points[min_pair[0]][0] * points[min_pair[1]][0])
