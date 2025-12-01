logger = None

def run(filename):
    dial = 50
    cnt = 0
    dir = {'L': -1, 'R': 1}
    logger.info(f"The dial starts by pointing at {dial}.")
    i = 0
    print(filename)
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            old_dial = dial

            line = line.strip()
            num =dir[line[0]] * int(line[1:])
            full_dial =  dial + num
            add_cnt, dial = divmod(full_dial, 100)
            if add_cnt <= 0:
                add_cnt *= -1
                if old_dial == 0 and dial != 0:
                    add_cnt -= 1
                if dial == 0:
                    add_cnt += 1

            logger.info(f"The dial is rotated {line} to point at {dial}; \t\t{add_cnt if add_cnt > 0 else ""} [{cnt + add_cnt}]")

            if add_cnt > 0:
                cnt += add_cnt
            
    return str(cnt)