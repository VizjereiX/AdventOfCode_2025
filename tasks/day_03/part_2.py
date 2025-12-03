logger = None

"168193674087539 <-- too low"
"168193674087539"
"169782750711259"
"169935154100102"

def my_min(v):
    idx = 0
    for i in range(1, len(v)):
        if v[i] < v[idx]:
            idx = i
    return idx

def my_max(v):
    idx = 0
    for i in range(1, len(v)):
        if v[i] > v[idx]:
            idx = i
    return idx


from itertools import combinations

def arr_to_int(v):
    if not v:
        return ""
    return int("".join([str(e) for e in v]))


def run(filename):
    acc = 0
    with open(filename, "r") as f:
        for data in f.read().splitlines():
            v = [int(c) for c in data.strip()]
            reconstructed = []

            while len(reconstructed) < 12:
                idx = my_max(v[0: len(v) - 11 + len(reconstructed)])
                reconstructed.append(v[idx])
                if idx < len(v):
                    v = v[idx+1::]
                else:
                    v = []
                logger.debug(f"{reconstructed}\t{v}")


            m = int("".join([str(e) for e in reconstructed]))
            logger.info(f"{data} -> {m}")
            acc+=m

    return str(acc)
