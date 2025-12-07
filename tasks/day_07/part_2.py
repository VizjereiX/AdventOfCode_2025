logger = None

def run(filename):
    data_grid = []
    with open(filename, "r") as f:
        data = f.read()
        j = 0
        for line in data.splitlines():
            line = ["." ] + [c for c in line.strip()] + ["."]
            data_grid.append(line)
        data_grid.append(["." ] * len(line))
            
    memory = {}
        
    def count_timelines(x, y):
        if (x, y) in memory:
            return memory[(x, y)]
        for j in range(y+1, len(data_grid)):
            if data_grid[j][x] == "^":
                memory[(x, y)] = count_timelines(x-1, j) + count_timelines(x+1, j)
                return memory[(x, y)]
        return 1

    cnt = count_timelines(data_grid[0].index("S"), 0)

    return str(cnt)
