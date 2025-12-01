# Advent Of Code 2025 write-ups and runner
Hello! This is small repo that I will be using to work with AoC in 2025. This year I chose to use python only.
This repo consists of multiple parts:

## run.py
Main script used to run test and get final response from the code
```
usage: run.py [-h] [-v] {test,run, full} {day_1/part_1, day_1/part_2, ...}

Test runner for Advent of Code solutions

positional arguments:
  {test, run, full}          Choose execution mode
  {day_1/part_1, ...}  Which day's solution to execute

optional arguments:
  -h, --help       show this help message and exit
  -v, --verbosity  Increase output verbosity
```

First parameter is called "mode". On "test" it is running your solution or all test inputs and test them against test outputs. Each inpout/output pair has to be placed in the same directory. Input file has to start with "input" and corresponding output has to same the same name, with "input" replaced to "output".
On "run" it is feeding the tested script with full data (file literally called `data`).
You can use "full mode" to do all test and then run script on full data if and only if all tests are OK.


## tasks
Each task/day should be placed in its directory in "tasks" directory and be a python module in single .py file. The name of the file should be the same as a directory with inputs and outputs, for example:
```
tasks
 |--sample
   |--part_1 (directory)
   |--part_1.py
   |--part_2 (directory)
   |--part_2.py
```

`run.py test sample/part_1` will execute function `run` placed in `part_1.py` against all inputs from `part_1` directory. 

Each solution's module have to implement `run` function with single input parameter (path to input file)

## Logging
Main runner is setting `logger` inside the tested module, so you can use the same stream for all tests. Default verosbity level is ERROR, you can increase it by setting `-v` flag to up it one time per flag (f.e. `-vvv` for DEBUG).