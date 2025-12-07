logger = None

def run(filename):
    data_grid = []
    splitters_activated = set()
    with open(filename, "r") as f:
        data = f.read()
        j = 0
        for line in data.splitlines():
            line = ["." ] + [c for c in line.strip()] + ["."]
            if j == 0:
                logger.debug("".join(line))
                data_grid.append(line)
                j+=1
                continue    

            new_line = line.copy()

            for i in range(1, len(line)-1):
                if line[i] == "." and data_grid[j-1][i] in "|S":
                    new_line[i] = "|"                

                if line[i] == "." and data_grid[j-1][i-1] == "^" and data_grid[j-2][i-1] in "|S":
                    new_line[i] = "|"
                    splitters_activated.add((j-1, i-1))

                if line[i] == "." and data_grid[j-1][i+1] == "^" and data_grid[j-2][i+1] in "|S":
                    new_line[i] = "|"
                    splitters_activated.add((j-1, i+1))

            data_grid.append(new_line)
            logger.debug("".join(new_line))
            j+=1

    for x, y in splitters_activated:
        data_grid[x][y] = "#"
    logger.debug("\n" + "\n".join("".join(row) for row in data_grid))
    return str(len(splitters_activated)) 
