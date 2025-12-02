logger = None

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
                    firstpart, secondpart = numAsStr[:len(numAsStr)//2], numAsStr[len(numAsStr)//2:]
                    logger.debug(f"Checking for {numAsStr} if {firstpart}=={secondpart}")
                    if (firstpart == secondpart):
                        logger.debug("{numAsStr is invalid!}")
                        sum += n
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