import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

pybank_path = os.path.join('Resources','budget_data.csv')

date = []
profits_losses = []
months = 0
total = 0
inc = ['',0]
dec = ['',1000000]
prev_rev = 867884
total_ch = 0



with open(pybank_path, "r", encoding="utf-8") as pybankfile:

    pybankreader = csv.reader(pybankfile, delimiter =',')

    next(pybankreader)

    for row in pybankreader:
        rev = int(row[1])
        months += 1
        total += rev

        change = rev - prev_rev
        total_ch += change
        prev_rev = rev

        if change > inc[1]:
            inc[0] = row[0]
            inc[1] = change

        if change < dec[1]:
            dec[0] = row[0]
            dec[1] = change

output = f'\nFinancial Analysis\n----------------------------\n\
  Total Months: {months}\n\
  Total: ${total:,}\n\
  Average  Change: ${total_ch/(months-1):,.2f}\n\
  Greatest Increase in Profits: {inc[0]} (${inc[1]:,})\n\
  Greatest Decrease in Profits:{dec[0]} (${dec[1]:,})\n'

print(output)

my_report = open('analysis/report.txt','w')
my_report.write(output)