import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

pypoll_path = os.path.join('Resources','election_data.csv')

all_votes = []
all_candidates =[]
candidates = {}
votes = 0

with open(pypoll_path, "r", encoding="utf-8") as pypollfile:

    pypollreader = csv.reader(pypollfile, delimiter =',')

    next(pypollreader)

     
    for row in pypollreader:
        all_votes.append(row[0])
        all_candidates.append(row[2])
        votes = len(all_votes)
        
        candidates["name"] = all_candidates

print(f'{candidates["name"]}')