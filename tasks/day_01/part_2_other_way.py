logger = None

def run(filename):
    dial = 50
    cnt = 0
    dir = {'L': -1, 'R': 1}
    logger.debug(f"The dial starts by pointing at {dial}.")
    i = 0
  
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()
            
            step = dir[line[0]]
            num = int(line[1:])
            
            values = range(dial + step, dial + step*num + step, step)
            cnt += sum(1 for v in values if v%100 == 0)
            
            dial = (dial + step*num) % 100
            logger.debug(f"The dial is rotated {line} to point at {dial}; \t{cnt}")
            
    return str(cnt)