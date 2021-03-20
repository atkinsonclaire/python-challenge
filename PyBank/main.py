import os
import csv

date=[]
amount=[]


csvpath=os.path.join('..', 'Resources', 'budget_data.csv')
with open(budget_data.csv, newline='') as csvfile
  csvreader=csv.reader(csvfile, delimiter=",")

  
  tot_amount=0
  change=0
  greatest=0
  smallest=0

  for row in csvreader:
    date.append(row[0])
    amount.append(row[1])

    months=len(date)
    tot_months=int(months)

    x=int(amount[0])
    tot_amount=tot_amount+x

    change=change-x

    if change>greatest then
      greatest=change
    else if change<smallest then
      smallest=change
    else continue

  next

  print(tot_months)
  print(pro_loss)
  avg_change=change/tot_months
  print(avg_change)
  print(gre
  print(smallest)

