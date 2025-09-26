import hashlib
import os
from flask import Flask, request, jsonify, render_template, flash, url_for
from dotenv import load_dotenv
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from unicodedata import category
from werkzeug.utils import redirect

from flask_mail import Mail, Message

# Flask-Mail config


load_dotenv()

app = Flask(__name__)
app.secret_key = "mysupersecretkey123"

MAILCHIMP_API_KEY = os.getenv("MAILCHIMP_API_KEY")
MAILCHIMP_SERVER_PREFIX = os.getenv("MAILCHIMP_SERVER_PREFIX")
MAILCHIMP_LIST_ID =  os.getenv("MAILCHIMP_LIST_ID")

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("EMAIL_USER")   # your Gmail
app.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASS")

mail=Mail(app)

client = MailchimpMarketing.Client()
client.set_config({
    "api_key": MAILCHIMP_API_KEY,
    "server": MAILCHIMP_SERVER_PREFIX
})


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/join_waitlist', methods=['GET','POST'])
def join_waitlist():
    if request.method =='GET':
        return "waitlist endpoint is available"

    email = request.form.get('email')

    if not email or '@' not in email:
        flash("please enter a valid email.", "error")
        return redirect(url_for('home'))
        # return jsonify({
        #     "status": "error",
        #     "message": "Invalid_email"
        # }),400
    try:
       response= client.lists.add_list_member(MAILCHIMP_LIST_ID,{
           "email_address": email,
           "status": "subscribed"
       })

        
         # handles email from flask
       # msg = Message("Welcome to the Waitlist!",
       #               sender=app.config['MAIL_USERNAME'],
       #               recipients=[email])
       # msg.body = "Thanks for joining! We'll notify you when we launch 🚀"
       # mail.send(msg)

       flash("You are on the waitlist!", "success")
       return redirect(url_for('home'))
       # return jsonify({
       #     "status": "success",
       #     "message": "You're on the waitlist"
       # })
    except ApiClientError as error:
        # flash(f" Error: {error.text}", "error")
        #
        # return redirect(url_for('home'))
        # return jsonify({
        #     "status": "error",
        #     "message": str(error)
        # }),400
        error_msg = str("you have been registered")

        if "Member Exists" in error_msg:
            subscriber_hash = hashlib.md5(email.lower().encode()).hexdigest()
            client.lists.set_list_member(MAILCHIMP_LIST_ID, subscriber_hash,{
                "email_address": email,
                "status_if_new": "subscribed",
                "status": "subscribed"
            })
            flash("You are already on the waitlist!", 'info')
            return redirect(url_for('home'))

        flash( error_msg, "error")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)