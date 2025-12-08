import math

logger = None

def run(filename):
    wire_count = 1000 if "data" in filename else 10
    points = []
    clusters = []
    connections = []

    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip().split(",")
            points.append([int(x) for x in line] + [len(clusters)])
            clusters.append([len(clusters)])



    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = (points[i][0] - points[j][0])**2  + (points[i][1] - points[j][1]) ** 2 + (points[i][2] - points[j][2])**2
            connections.append((dist, i, j))

    connections.sort(key=lambda x: x[0])

    for i in range(wire_count):
        logger.info(f"Iteration {i}")
        
        _, a , b = connections[i]
        
        cluster_num = min(points[a][3], points[b][3])
        old_cluster_num = max(points[a][3], points[b][3])

        if cluster_num == old_cluster_num:
            continue
        
        for p in points:
            if p[3] == old_cluster_num:
                p[3] = cluster_num

        clusters[cluster_num].extend(clusters[old_cluster_num])
        clusters[old_cluster_num] = []

    sorted_clusters = sorted([c for c in clusters if len(c) > 0], key=lambda x: len(x), reverse=True)
    for i in range(0, 3):
       logger.debug([points[j] for j in sorted_clusters[i]])

    return str(math.prod(len(c) for c in sorted_clusters[0:3]))
