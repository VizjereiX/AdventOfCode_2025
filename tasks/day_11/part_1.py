logger = None

def find_paths_to_stop(graph, node):
    logger.debug(f"find_path_to_stop: {node}")
    if node == 'out':
        logger.debug("Reached 'out' node, returning path.")
        return [["out"]]
    if graph.get(node, None) is None:
        logger.debug(f"Node {node} has no connections, returning empty list.")
        return []
    paths = []
    for elem in graph[node]:
        new_paths = find_paths_to_stop(graph, elem)
        logger.debug(f"New paths from {elem}: {len(new_paths)}")
        for path in new_paths:
            paths.append([node] + path)
    return paths if paths else []

def run(filename):
    graph = {}
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            start, *elems = line.strip().split()
            start = start.strip(":")
            graph[start] = [elem.strip(",") for elem in elems]

    paths = find_paths_to_stop(graph, "you")
    return str(len(paths)) 
