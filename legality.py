#import os
#import pandas as pd
import csv

#data_1 = pd.read_csv('SportsBetting.csv')
#print(data_1)

AbbrevList = []
with open("SportsInfo.csv", "r") as csv_file:
    read_csv = csv.reader(csv_file, delimiter =',')
    for lines in read_csv:
        AbbrevList.append(lines[1])
#AbbrevList.pop(0)        
print(AbbrevList)

StateList = []
with open("SportsInfo.csv", "r") as csv_file:
    read_csv = csv.reader(csv_file, delimiter =',')
    for lines in read_csv:
        StateList.append(lines[0])
#StateList.pop(0)        
print(StateList)

user_state = input("Please enter your state i.e. New York, NY").upper()
if user_state in StateList or user_state in AbbrevList:
    print(StateList.index(user_state))