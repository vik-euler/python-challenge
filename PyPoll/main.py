import os
import csv
import operator
candidate_votes={}
candidate_county={}
candidate_stats=[]
total_votes=0
index=0
csvpath = os.path.join('..','PyPoll/Resources','election_data.csv')
with open(csvpath) as csvfile:
    cvsreader = csv.reader(csvfile, delimiter=',')
#    print(cvsreader)
    csv_header = next(cvsreader)
    #print(csv_header)
   

    for row in cvsreader:
        total_votes= total_votes+1
        if row[2] not in candidate_votes:
            candidate_votes[row[2]]=1
            candidate_county[row[2]]=row[1]
        else:
            candidate_votes[row[2]]=int(candidate_votes[row[2]])+1



    print("Election Results")
    line="---------------------------"

    print(line)
    # Write the second row
    print(f"Total Votes: {total_votes}")
    print(line)
    for i,v in candidate_votes.items():
        round_percent=round(v/total_votes*100)
        percentage="{:.3%}".format(round_percent/100)
        candidate_stats.append(str(i)+ " "+ str(percentage)+" "+ str(v))
    for candidate_stat in candidate_stats:
        print(candidate_stat)

    print(line)
    winner="Winner: "+max(candidate_votes.items(),key=operator.itemgetter(1))[0]
    print(winner)
    print(line)


# Specify the file to write to
output_path = os.path.join("..", "PyPoll/analysis", "election_stats.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow([line])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow([line])
    for candidate_stat in candidate_stats:
        #print(candidate_stat, file=csvfile)
        csvwriter.writerow([candidate_stat])
    csvwriter.writerow([line])
    csvwriter.writerow([winner])
    csvwriter.writerow([line])

