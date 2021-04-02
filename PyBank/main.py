import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

pybank_path = os.path.join('Resources','budget_data.csv')

date = []
profits_losses = []
total_months = []
total = []
average_change = []
greatest_increase_in_profits = []
greatest_decrease_in_profits = []


with open(pybank_path, "r", encoding="utf-8") as pybankfile:

    pybankreader = csv.reader(pybankfile, delimiter =',')

    for row in pybankreader:
        date.append(row[0])
        profits_losses.append(row[1])


        count = sum(row[0])
        total_months.append(count)
        print(total_months)