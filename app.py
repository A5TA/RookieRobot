from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form


app = Flask(__name__)

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
            return redirect(url_for('thank_you'))
        if len(custom_message) == 0:
          custom_message = "pull message from the spreadsheet" #TODO: add message from spreadsheet
        

    # Render the sign-up page
    return render_template('base.html', message=error)

if __name__ == "__main__":
    app.run(debug=True)