def run(input_file):
    with open(input_file, 'r') as f:
        data = f.read().strip()

    total = 1
    for num in data.split(" "):
        total *= int(num)

    return str(total)