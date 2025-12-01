from argparse import ArgumentParser 
import os
from importlib import import_module
import logging

logger = logging.getLogger("[AoC]")
logging.basicConfig(level=logging.DEBUG) 


COLOR_ERROR = '\033[91m'
COLOR_WARNING = '\033[93m'
COLOR_END = '\033[0m'

def get_available_days():
    for dirpath, _, filenames in os.walk("tasks"):
        dir = os.path.basename(dirpath)
        for filename in filenames:
            if filename.endswith(".py"):
                yield f"{dir}/{filename[:-3]}"
def main():
    parser = ArgumentParser(
        prog="run.py",
        description="Test runner for Advent of Code solutions",
        epilog="Enjoy the challenge!"
    )

    parser.add_argument("mode", choices=["test", "run"], help="Test solution on examples or run command on samples")
    parser.add_argument("task", type=str, choices=list(get_available_days()), help="Which day's solution to execute")
    args = parser.parse_args()

    module_path = f"tasks.{args.task}".replace("/", ".")
    print(args.task, module_path)
    module = import_module(module_path)
    module.logger = logger

    data_dir = f"tasks/{args.task}"

    if args.mode == "test":
        test_count, errors = 0, 0
        for file in os.listdir(data_dir):
            if file.startswith("input"):
                output_file = file.replace("input", "output")
                if not os.path.isfile(f"{data_dir}/{output_file}"):
                    print(f"{COLOR_WARNING}No output file found for {file}{COLOR_END}")
                    continue

                print(f"Testing {file} against {output_file}", end=" ... ")
                with open(f"{data_dir}/{output_file}", "r") as f:
                    expected_output = f.read().strip()
                
                output =  module.run(f"{data_dir}/{file}")
                if output != expected_output:
                    print(f"{COLOR_ERROR} failed!")
                    print(f"Expected: {expected_output}, Got: {output}{COLOR_END}")
                    errors += 1
                else:
                    print(" passed!")
                test_count += 1
        print(f"Tests run: {test_count}, \tErrors: {errors}")
    else:
        datapath = f"{data_dir}/data"
        if os.path.isfile(datapath) == False:
            print(f"{COLOR_ERROR}No data file found at {datapath}{COLOR_END}")
            return
        output =  module.run(datapath)
        print(output)

if __name__ == "__main__":
    main() 