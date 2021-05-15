
#import pandas as pd
import os
import csv
import time
import json
import requests
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ.get("API_KEY")


#data_1 = pd.read_csv('SportsBetting.csv')
#print(data_1)

delay = 1.5

# An api key is emailed to you when you sign up to a plan


# First get a list of in-season sports
sports_response = requests.get('https://api.the-odds-api.com/v3/sports', params={
    'api_key': apikey
})

sports_json = json.loads(sports_response.text)

if not sports_json['success']:
    print(
        'There was a problem with the sports request:',
        sports_json['msg']
    )

else:
    print()
    print(
        'Successfully got {} sports'.format(len(sports_json['data'])),
        'Here\'s the first sport:'
    )
    print(sports_json['data'][3])



# To get odds for a sepcific sport, use the sport key from the last request
#   or set sport to "upcoming" to see live and upcoming across all sports
sport_key = 'baseball_mlb'                                                      

odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
    'api_key': apikey,                                                         
    'sport': sport_key,                                                         
    'region': 'us', # uk | us | eu | au                                         
    'mkt': 'spreads', # h2h | spreads | totals           
    'dateFormat': 'unix'                      #This might be a user input
})

odds_json = json.loads(odds_response.text)
if not odds_json['success']:
    print(
        'There was a problem with the odds request:',
        odds_json['msg']
    )

else:
    # odds_json['data'] contains a list of live and 
    #   upcoming events and odds for different bookmakers.
    # Events are ordered by start time (live events are first)
    print()
    print(
        'Successfully got {} events'.format(len(odds_json['data'])),
        'Here\'s the first event:'
    )

    baseball = (odds_json['data'][3])


    print(baseball)


    # Check your usage
    print()
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])
    




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

