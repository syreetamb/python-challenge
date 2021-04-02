import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
os.chdir(dir_path)

pybank_path = os.path.join('Resources','budget_data.csv')
#print(pybank_path)

with open(pybank_path, "r", encoding="utf-8") as pybankfile:

    pybankreader = csv.reader(pybankfile, delimiter =',')

    for row in pybankreader:
        print(row)