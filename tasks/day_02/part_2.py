logger = None

def looks_shady(shadyStr, partsCount):
    partLen = len(shadyStr) // partsCount
    firstPart = shadyStr[0:partLen]
    for i in range(1, partsCount):
        testedPart = shadyStr[i*partLen:(i+1)*partLen]
        if firstPart != testedPart:
            return False
    return True

def run(filename):
    sum = 0
    num1 = 0
    num2 = 0
    firstNumDone = False

    with open(filename, "r") as f:
        data = f.read(1)
        while data:
            if data == "-":
                firstNumDone = True   
            elif data == "," or data == "\n" or data == "\r":
                # check range here
                logger.debug(f"Got range {num1}-{num2}")
                for n in range(num1, num2+1):
                    numAsStr = str(n)
                    for d in range(2, len(numAsStr)+1):
                        if len(numAsStr) % d != 0: continue
                        if looks_shady(numAsStr, d):                    
                            logger.debug(f"\t\t{numAsStr} is invalid!")
                            sum += n
                            break
                # and clean up
                firstNumDone = False
                num1 = 0
                num2 = 0
            elif firstNumDone:
                num2 = num2*10 + int(data)
            else:
                num1 = num1*10 + int(data)
            data = f.read(1)

    return str(sum)