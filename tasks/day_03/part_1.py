logger = None

def run(filename):
    acc = 0
    with open(filename, "r") as f:
        for data in f.read().splitlines():
            v = [int(c) for c in data.strip()]
            n1 = max(v[0:-1])
            pos = data.index(str(n1))
            
            n2 = max(v[pos+1::])
            m= n1*10 + n2  
            logger.info(f"{data}\t{m}")
            acc+=m

    return str(acc)
