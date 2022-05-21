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
    access_token_secret=globals.token_secret
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

#Post the tweet with Twitter API

response = client.create_tweet(
    text=tweet_quote
)

#Delete the tweet from the spreadsheet
#wks.delete_rows(4)