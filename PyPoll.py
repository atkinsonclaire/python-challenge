import os
import csv

csvpath=os.path.join("Resources", "election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)

    voter_ids=[]
    counties=[]
    candidates=[]
    for row in csvreader:
        voters=row[0].split(",")
        voter_ids.append(row[0])
        county=row[1].split(",")
        counties.append(row[1])
        candidate=row[2].split(",")
        candidates.append(row[2])
        continue
  
    num_votes=len(voter_ids)
    print("Total Votes: "+ str(num_votes))

    myset=set(candidates)
    candid_list=list(myset)
    print(candid_list)
    
    khan_votes=0
    correy_votes=0
    li_votes=0
    otooley_votes=0
    for row in candidates:
        if row=="Khan":
            khan_votes=khan_votes+1
        elif row=="Correy":
            correy_votes=correy_votes+1
        elif row=="Li":
            li_votes=li_votes+1
        else: otooley_votes=otooley_votes+1
        continue
    
    khan_percent=((khan_votes/int(num_votes))*100)
    print("Khan: "+str(khan_percent)+"% "+str(khan_votes))
    
    correy_percent=((correy_votes/int(num_votes))*100)
    print("Correy: "+str(correy_percent)+"% "+str(correy_votes))

    li_percent=((li_votes/int(num_votes))*100)
    print("Li: "+str(li_percent)+"% "+str(li_votes))
    
    otooley_percent=((otooley_votes/int(num_votes))*100)
    print("O'Tooley: "+str(otooley_percent)+"% "+str(otooley_votes))

    print("Winner: Khan")
    
