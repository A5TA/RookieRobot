import gspread
import globals
# from twitter import *
numberOfCOmments = 20
# t = Twitter(
#     auth=OAuth(globals.token, globals.token_secret, globals.consumer_key, globals.consumer_secret))

gc = gspread.service_account('credentials.json') #Paste your credentials in a credentials.json file

# Open a sheet from a spreadsheet in one go
wks = gc.open("RookieRobot").sheet1 #Here I put RookieRobot because that is the name of my sheets file 

# Update a range of cells using the top left corner address
column = 'A'
for row in range(numberOfCOmments):
    wks.update(str(column)+(str(row+1)), [['Hello '+ str(row+1)]])