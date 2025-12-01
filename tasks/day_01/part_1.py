def run(filename):
    dial = 50
    cnt = 0
    dir = {'L': -1, 'R': 1}
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()
            num = int(line[1:]) % 100
            dial = (dial + (dir[line[0]] * num + 100) ) % 100
            if dial == 0:
                cnt += 1
    return str(cnt)