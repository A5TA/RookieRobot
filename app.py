from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
import gspread
import time
import globals
import random
from twitter import *
import tweepy

app = Flask(__name__)

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    consumer_key=globals.consumer_key,
    consumer_secret=globals.consumer_secret,
    access_token=globals.token,
    access_token_secret=globals.token_secret,
    bearer_token=globals.bearer_token
)
#adding main.py stuff to allow functionality with the website
gc = gspread.service_account('credentials.json') #Paste your credentials in a credentials.json file

# Open a sheet from a spreadsheet in one go
wks = gc.open("RookieRobot").sheet1 #Here I put RookieRobot because that is the name of my sheets file 

@app.route('/thankyou')
def thank_you():
    return render_template('thank_you.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    error = "" #Make a message for errors
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        username = request.form.get('username')
        custom_message = request.form.get('custom_message')

        # Validate form data
        if len(username) == 0:
            # Form data failed validation; try again
            error = "Please supply the Username"
        else:
            # Form data is valid; move along
            #SEND USER INPUT FROM FLASK SITE TO THIS VARIABLE
            if len(custom_message) == 0 or len(custom_message) > 260: 
                custom_message = wks.acell('A'+str(random.randint(1,348))).value #Add message from spreadsheet if not provided
                rookierobot(username,custom_message)
                error="Your custom message wasn't the appropriate format, now using: \"" +  custom_message +"\""
            else: 
                rookierobot(username,custom_message)
            return redirect(url_for('thank_you'))

    # Render the sign-up page
    return render_template('base.html', message=error)


def rookierobot(screen_name,tweet_quote):
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

if __name__ == "__main__":
    app.run(debug=True)