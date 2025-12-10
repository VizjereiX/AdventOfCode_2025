logger = None

"""
That part was very hard for me. Brute force was way too slow, even with itertools invloved.
I was trying to use scipy.linalg or numpy.linalg to solve a system of linear equations,
but failed.
Looked for hints on Reddit and found a suggestion to use milp fro scipy.optimize
Big thanks to https://www.reddit.com/user/johnpeters42/ for the idea!
"""

from scipy.optimize import milp 
import numpy as np
from scipy.optimize import LinearConstraint




def find_button_combination_len(joltage_target, buttons):
    
    buttons_matrix = []
    for i in range(len(joltage_target)):
        buttons_matrix.append([0] * len(buttons) )    
        for j, button in enumerate(buttons):
            if i in button:
                buttons_matrix[i][j] += 1

    A = np.matrix(buttons_matrix)
    b_u = np.array(joltage_target)
    b_l = b_u.copy()
    constraint = LinearConstraint(A, b_l, b_u)
    c = np.ones(len(buttons))

    x = milp(c, constraints=[constraint], integrality=np.ones_like(c))
    return int(x.fun)


def run(filename):
    acc = 0
    with open(filename, "r") as f:
        data = f.read()
        for line in data.splitlines():
            line = line.strip()
            _, *elems = line.split(" ")
            buttons = []
            joltage_specs = []
            for elem in elems:
                nums = [int(e) for e in elem[1:-1].split(",")]
                if elem.startswith("("):
                    buttons.append(nums)
                elif elem.startswith("{"):
                    joltage_specs = nums
            logger.debug(f"Buttons: {buttons}, Joltage specs: {joltage_specs}")
            l = find_button_combination_len(joltage_specs, buttons)
            acc += l
            
    return str(acc) 
