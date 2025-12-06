logger = None
import math

def run(filename):
    data = []
    dataLen = None
    acc = 0
    with open(filename, "r") as f:
        input = f.read()
        for line in input.splitlines():
            line = line.strip()
            nums = [c for c in line.split(" ") if c]
            if not dataLen:
                dataLen = len(nums)
                for num in nums:
                    data.append([int(num)])
            elif not nums[0].isnumeric():
                # do computations
                for i in range(dataLen):
                    if nums[i] == '+':
                        acc += sum(data[i])
                    elif nums[i] == '*':   
                        acc += math.prod(data[i])
            else:
                for i in range(dataLen):
                    data[i].append(int(nums[i]))

    return str(acc)
