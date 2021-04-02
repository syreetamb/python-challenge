import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
os.chdir(dir_path)

pypoll_path = os.path.join('Resources','election_data.csv')
#print(pypoll_path)

with open(pypoll_path, "r", encoding="utf-8") as pypollfile:

    pypollreader = csv.reader(pypollfile, delimiter =',')

    for row in pypollreader:
        print(row)