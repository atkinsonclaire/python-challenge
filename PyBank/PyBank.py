import os
import csv

csvpath=os.path.join("Resources", "budget_data.csv")
with open(csvpath, newline='') as csvfile:
  csvreader=csv.reader(csvfile, delimiter=",")
  csv_header=next(csvfile)
  
  dates=[]
  amounts=[]
  for row in csvreader:
    date=row[0].split(",")
    dates.append(row[0])
    amount=row[1].split(",")
    amounts.append(row[1])
    continue
  
  months=len(dates)
  tot_months=int(months)
  print(tot_months)
  
  net_change=0
  i=0
  for row in amounts:
    x=int(amounts[i])
    net_change=net_change+x
    i=i+1
    continue
  print(net_change)

  n=0
  changes=[]
  for row in amounts:
    a=int(amounts[n])
    n=n+1
    b=int(amounts[n])
    diff=b-a
    changes.append(diff)
    if n==85:
      break
    continue
  c=0
  sum_diff=0
  for row in changes:
      d=int(changes[c])
      sum_diff=sum_diff+d
      c=c+1
      continue
  avg=sum_diff/tot_months
  print(avg)

  combo=dict(zip(dates, changes))
  
  greatest=max(combo, key=combo.get)
  print(greatest, combo[greatest])
  smallest=min(combo, key=combo.get)
  print(smallest, combo[smallest])



