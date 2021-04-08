import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

pypoll_path = os.path.join('Resources','election_data.csv')

all_votes = []
all_candidates =[]
candidates = []
votes = 0

with open(pypoll_path, "r", encoding="utf-8") as pypollfile:

    pypollreader = csv.reader(pypollfile, delimiter =',')

    next(pypollreader)

     
    for row in pypollreader:
        all_votes.append(row[0])
        all_candidates.append(row[2])
        votes = len(all_votes)

       #candidates names 
    [candidates.append(x)for x in all_candidates if x not in candidates]   

        #candidates votes
    khan_total = all_candidates.count(candidates[0])
    correy_total = all_candidates.count(candidates[1])
    li_total = all_candidates.count(candidates[2])
    otooley_total = all_candidates.count(candidates[3])
    
    total = [khan_total, correy_total, li_total, otooley_total]
        
        #percentage
    khan_percent = round(((khan_total/votes) * 100),3)
    correy_percent = round(((correy_total/votes)*100),3)
    li_percent = round(((li_total/votes)*100),3)
    otooley_percent = round(((otooley_total/votes)*100),3)    

    percent = [khan_percent, correy_percent, li_percent, otooley_percent]

    output =f'\nElection Results\n-------------------------\n\
  Total Votes: {votes:,}\n\
  -------------------------\n\
  {candidates[0]}: {percent[0]}% ({total[0]:,})\n\
  {candidates[1]}: {percent[1]}% ({total[1]:,})\n\
  {candidates[2]}: {percent[2]}% ({total[2]:,})\n\
  {candidates[3]}: {percent[3]}% ({total[3]:,})\n\
  -------------------------\n\
  Winner: Khan\n\
  -------------------------\n'
print(output)