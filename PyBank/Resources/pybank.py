import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

pybank_path = os.path.join('Resources','budget_data.csv')

with open(pybank_path, "r", encoding="utf-8") as pybankfile:

    pybankreader = csv.reader(pybankfile, delimiter =',')

    next(pybankreader)

    for row in pybankreader:
        print(row)