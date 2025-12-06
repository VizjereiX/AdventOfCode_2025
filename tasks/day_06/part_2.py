logger = None
import math


def run(filename):
    data = []
    acc = 0
    with open(filename, "r") as f:
        input = f.read()
        for line in input.splitlines():
            line = line.strip("\n\r")
            if line[0] == '+' or line[0] == '*':
                nums = []
                num = ""
                for i in range(len(data[0])-1, -1, -1):
                    for j in range(len(data)):
                        num = num + data[j][i]
                    if num.strip() != "":
                        nums.append(int(num))
                    num = ""
                    if (line[i] == '+'):
                        acc += sum(nums) 
                        nums = []
                    elif (line[i] == '*'):
                        acc += math.prod(nums)
                        nums = []     
            else:
                data.append(line)


    return str(acc)
