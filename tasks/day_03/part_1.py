logger = None

def my_max(v):
    idx = 0
    for i in range(1, len(v)):
        if v[i] > v[idx]:
            idx = i
    return idx

def get_batt_joltage(filename, batt_cnt, logger):
    acc = 0
    with open(filename, "r") as f:
        for data in f.read().splitlines():
            v = [int(c) for c in data.strip()]
            reconstructed = []

            while len(reconstructed) < batt_cnt:
                idx = my_max(v[0: len(v) - batt_cnt + 1 + len(reconstructed)])
                reconstructed.append(v[idx])
                if idx < len(v):
                    v = v[idx+1::]
                else:
                    v = []
                logger.debug(f"{reconstructed}\t{v}")


            m = int("".join([str(e) for e in reconstructed]))
            logger.info(f"{data} -> {m}")
            acc+=m
    return acc

def run(filename):
    return str(get_batt_joltage(filename, 2), logger)
