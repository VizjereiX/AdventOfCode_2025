logger = None
from functools import lru_cache
graph = {}

@lru_cache(maxsize=None)
def find_paths_to_stop(node, fft_visited = False, dac_visited = False):
    logger.debug(f"find_paths_to_stop: {node}")
    if node == 'out':
        ans = 1 if dac_visited and fft_visited else 0
        logger.debug(f"Reached 'out' node, returning {ans} ({fft_visited}, {dac_visited}).")
        return ans
    if node == 'fft':
        fft_visited = True
    if node == 'dac':
        dac_visited = True

    acc = 0
    for elem in graph.get(node, []):
        acc += find_paths_to_stop(elem, fft_visited, dac_visited)

    return acc

def run(filename):
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            start, *elems = line.strip().split()
            start = start.strip(":")
            graph[start] = [elem.strip(",") for elem in elems]

    acc = find_paths_to_stop("svr")
    return str(acc) 