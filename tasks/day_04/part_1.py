logger = None

def run(filename):
    acc = 0
    prev = []
    act = []
    nxt = []
    prev_data = ""
    with open(filename, "r") as f:
        for data in f.read().splitlines():
            data = data.strip()
            data_len = len(data)
            data = "_" + data + "_"
            prev = act or [0] * (data_len+2)
            act = nxt or [0] * (data_len+2)
            nxt = [0] * (data_len+2)
            for i in range(1, data_len+1):
                if data[i] != "@": continue
                for j in range(i-1, i+2):
                    prev[j]+= 1
                    act[j] += 1 if i != j else 0
                    nxt[j] +=1
            if prev_data:
                cnt = sum(1 for i in range(1, data_len+1) if prev[i] < 4 and prev_data[i] == "@")
                debug_str = ""
                for i in range(1, data_len+1):
                    if prev_data[i] == ".": debug_str += "."
                    elif prev[i] < 4: debug_str += "x"
                    else: debug_str += "@"
                debug_str += f"\t{cnt}"
                logger.debug(debug_str)
                acc+=cnt
            prev_data = data
        cnt = sum(1 for i in range(1, data_len+1) if act[i] < 4 and prev_data[i] == "@")
        
        debug_str = ""
        for i in range(1, data_len+1):
            if prev_data[i] == ".": debug_str += "."
            elif prev[i] < 4: debug_str += "x"
            else: debug_str += "@"
        debug_str += f"\t{cnt}"
        logger.debug(debug_str)
        acc+=cnt
    return str(acc) 
