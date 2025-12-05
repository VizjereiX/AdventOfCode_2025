logger = None

def in_range(value, ranges):
    for start, stop in ranges:
        if start <= value < stop:
            return True
    return False

def run(filename):
    ranges = []
    acc = 0

    with open(filename, "r") as f:
        while True:
            line = f.readline()
            line = line.strip()
            if not line:
                break

            start, stop = line.split("-")
            ranges.append((int(start), int(stop)+1))

        while True:
            line = f.readline()
            line = line.strip()
            if not line:
                break
            value = int(line)
            if not in_range(value, ranges):
                continue
            acc+=1

    return str(acc) 
