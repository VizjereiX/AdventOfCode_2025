import tasks.day_03.part_1 as part_1
global logger

def run(filename):
    return str(part_1.get_batt_joltage(filename, 12, logger))
