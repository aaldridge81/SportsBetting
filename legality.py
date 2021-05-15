#import os
#import pandas as pd
import csv
import time

#data_1 = pd.read_csv('SportsBetting.csv')
#print(data_1)

delay = 1.5

AbbrevList = []
with open("SportsInfo.csv", "r") as csv_file:
    read_csv = csv.reader(csv_file, delimiter =',')
    for lines in read_csv:
        AbbrevList.append(lines[1])
AbbrevList.pop(0)        
#print(AbbrevList)

StateList = []
with open("SportsInfo.csv", "r") as csv_file:
    read_csv = csv.reader(csv_file, delimiter =',')
    for lines in read_csv:
        StateList.append(lines[0])
StateList.pop(0)        
#print(StateList)

LegalList = []
with open("SportsInfo.csv", "r") as csv_file:
    read_csv = csv.reader(csv_file, delimiter =',')
    for lines in read_csv:
        LegalList.append(lines[2])
LegalList.pop(0)        
#print(LegalList)

OnlineList = []
with open("SportsInfo.csv", "r") as csv_file:
    read_csv = csv.reader(csv_file, delimiter =',')
    for lines in read_csv:
        OnlineList.append(lines[3])
OnlineList.pop(0)        
#print(OnlineList)


RegisterList = []
with open("SportsInfo.csv", "r") as csv_file:
    read_csv = csv.reader(csv_file, delimiter =',')
    for lines in read_csv:
        RegisterList.append(lines[4])
RegisterList.pop(0)        
#print(RegisterList)

FutureList = []
with open("SportsInfo.csv", "r") as csv_file:
    read_csv = csv.reader(csv_file, delimiter =',')
    for lines in read_csv:
        FutureList.append(lines[5])
FutureList.pop(0)        
#print(FutureList)




user_state = input("Please enter your state i.e. New York, NY").upper()
if user_state in StateList:
    user_index = (StateList.index(user_state))
elif user_state in AbbrevList:
    user_index = (AbbrevList.index(user_state))
else:
    time.sleep(delay)
    print("Please input a valid state")

if OnlineList[user_index] == "Yes":
    time.sleep(delay)
    print("")
    print("It looks like online betting is legal in your area!")
    if RegisterList[user_index] == "Yes":
        time.sleep(delay)
        print("")
        print("Just a heads up! Your state requires that you register in-person before online gambling")
else: 
    time.sleep(delay)
    print("")
    print("Hmm...online betting is not currently legal in your area")
    if FutureList[user_index] == "Yes":
        time.sleep(delay)
        print("")
        print("Based on current legislation, online gambling in your state should be available by the end of 2021")
    else: 
        time.sleep(delay)
        print("")
        print("It does not appear as though legislation will allow online gambling by the end of 2021")
    if LegalList[user_index] == "Yes":
        time.sleep(delay)
        print("")
        print("The good news is in-person gambling is legal in your state!")
