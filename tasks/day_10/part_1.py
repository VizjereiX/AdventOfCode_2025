logger = None
import itertools

def find_button_combination(lights_target, buttons):
    for i in range(1, len(buttons) + 1):
        for combo in itertools.combinations(buttons, i):
            combined = [0] * len(lights_target)
            for button in combo:
                for idx in button:
                    combined[idx] ^= 1
            if combined == lights_target:
                return combo


def run(filename):
    acc = 0
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()
            lights_spec, *elems = line.split(" ")
            lights = []
            for c in lights_spec[1:-1]:
                if c == "#":
                    lights.append(1)
                else:  
                    lights.append(0)
            buttons = []
            joltage_specs = []
            for elem in elems:
                nums = [int(e) for e in elem[1:-1].split(",")]
                if elem.startswith("("):
                    buttons.append(nums)
                elif elem.startswith("{"):
                    joltage_specs.append(nums)
            combo = find_button_combination(lights, buttons)
            logger.info(f"Found combination: {combo}")
            acc += len(combo)
            
    return str(acc) 
