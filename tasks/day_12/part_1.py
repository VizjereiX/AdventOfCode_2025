logger = None

def run(filename):
    shapes = {}
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    
    i = 0
    while True:
        shaped_id = lines[i].strip()
        if not shaped_id.endswith(":"): break
        shaped_id = int(shaped_id.strip(":"))
        shapes[shaped_id] = {"size": 0, "shape": [[],[],[]]}
        i += 1
        
        for j in range(3):
            line = lines[i].strip()
            shapes[shaped_id]["shape"][j] = [int(c == "#") for c in line]
            shapes[shaped_id]["size"] += line.count("#")
            i+=1
        i+=1

    acc = 0
    for j in range(i,len(lines)):
        dims, *gift_counts = lines[j].split(" ")
        print(gift_counts)
        x, y = dims[:-1].split("x")
        area_size = int(x) * int(y)
        area_needed = 0
        for idx, num in enumerate(gift_counts):
            area_needed += int(num) * shapes[idx]["size"]
            
        if 0.82 * area_size > area_needed:
            acc += 1
        print(f"Needed: {area_needed}, have: {area_size}")

    return str(acc)
