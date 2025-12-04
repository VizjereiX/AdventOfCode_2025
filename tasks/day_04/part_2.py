logger = None

def run(filename):
    acc = 0
    datalines = []
    data_len = 0

    # load all lines to store them in array
    with open(filename, "r") as f:
        for data in f.read().splitlines():
            data = data.strip()
            data_len = len(data)
            # make area bigger 1 col each side to prevent checking index out of bounds
            data = "_" + data + "_"           
            datalines.append(data)

    while True:
        # we are doing sliding window and annylizng previous line
        prev = []
        act = []
        nxt = []
        prev_data = ""
        # we need to know if ne moved anything IN THIS RUN
        run_acc = 0        

        for d in range(0, len(datalines)):
            data = datalines[d]
            # prep arrays for counting rolls
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
                    if prev_data[i] == "." or prev_data[i] == "x": debug_str += "."
                    elif prev[i] < 4: debug_str += "x"
                    else: debug_str += "@"
                logger.debug(debug_str + f"\t{cnt}")
                run_acc+=cnt
                datalines[d-1] = "_" + debug_str + "_"
            prev_data = data
        run_acc += sum(1 for i in range(1, data_len+1) if act[i] < 4 and prev_data[i] == "@")
        
        debug_str = ""
        for i in range(1, data_len+1):
            if prev_data[i] == "." or prev_data[i] == "x": debug_str += "."
            elif act[i] < 4: debug_str += "x"
            else: debug_str += "@"
        logger.debug(debug_str + f"\t{cnt}")

        datalines[len(datalines)-1] = "_" + debug_str + "_"
        if (run_acc > 0):
            acc+=run_acc
        else:
            return str(acc) 
