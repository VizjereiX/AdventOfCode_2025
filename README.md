# Advent Of Code 2025 write-ups and runner
Hello! This is small repo that I will be using to work with AoC in 2025. This year I chose to use python only.
This repo consists of multiple parts:

## run.py
Main script used to run test and get final response from the code
```
usage: run.py [-h] {test,run} {day_1/part_1, day_1/part_2, ...}

Test runner for Advent of Code solutions

positional arguments:
  {test, run}          Choose execution mode
  {day_1/part_1, ...}  Which day's solution to execute

optional arguments:
  -h, --help       show this help message and exit
```

First parameter is called "mode". On "test" it is running your solution or all test inputs and test them against test outputs. Each inpout/output pair has to be placed in the same directory. Input file has to start with "input" and corresponding output has to same the same name, with "input" replaced to "output".

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