logger = None


def run(filename):
    acc = 0
    ranges = []

    with open(filename, "r") as f:
        while True:
            line = f.readline()
            line = line.strip()
            
            if not line:
                break

            start, stop = line.split("-")
            ranges.append((int(start), int(stop)))
    
    # sorting so we need to check only start of the range
    ranges = sorted(ranges)
    fixed_ranges = []
    for begin, end in ranges:
        if fixed_ranges and fixed_ranges[-1][1] >= begin - 1:
            fixed_ranges[-1][1] = max(fixed_ranges[-1][1], end)
        else:
            fixed_ranges.append([begin, end])
    

    for start, stop in fixed_ranges:
        acc += stop-start + 1

    return str(acc)