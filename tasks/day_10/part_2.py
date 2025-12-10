logger = None

def run(filename):
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()

    return "" 
