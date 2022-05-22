import json
import gspread
import time
import globals
import random
from twitter import *
import tweepy


numberOfQuotes = 348

# client = tweepy.Client(bearer_token=globals.bearer_token)

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    consumer_key=globals.consumer_key,
    consumer_secret=globals.consumer_secret,
    access_token=globals.token,
    access_token_secret=globals.token_secret,
    bearer_token=globals.bearer_token
)

gc = gspread.service_account('credentials.json') #Paste your credentials in a credentials.json file

# Open a sheet from a spreadsheet in one go
wks = gc.open("RookieRobot").sheet1 #Here I put RookieRobot because that is the name of my sheets file 

# Update the speadsheet with the quotes

'''Uncomment this code segment to copy over the contents of the txt file to your google sheets
column = 'A'
row = 1
file = open('quotes.txt','r', encoding='utf-8') #open the file
line = file.readline() #read the first line
quote = [] #Use a list to append quotes to the spreadsheet

while line != "ENDofFile":
    if line == "\n":
        x = ' '.join(quote)
        try:
            wks.update(str(column)+(str(row)), [[x]]) 
            time.sleep(1)
        except:
            time.sleep(10)
            wks.update(str(column)+(str(row)), [[x]]) 
        row += 1
        quote.clear() #clear the list for the next quote
    else:
        quote.append(line.strip("\n"))
    line = file.readline()
file.close()
'''

#Pull a tweet from the spreadsheet
tweet_quote = wks.acell('A'+str(random.randint(1,348))).value

screen_name = input("Enter username: ").strip() #SEND USER INPUT FROM FLASK SITE TO THIS VARIABLE
idforuser = str(client.get_users(usernames=[screen_name])) #finds the users id from given @...
#loop over the data from user to pull only the id from it
targetID = ""
for num in range(24, len(idforuser)):
    if idforuser[num] == " ":
        break
    targetID += str(idforuser[num])
#Submit a follow to the target user using the id from the loop
client.follow_user(target_user_id=targetID, user_auth=True)

#Post the tweet with Twitter API
response = client.create_tweet(
    text='@'+screen_name + ' ' + tweet_quote
)
