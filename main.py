from flask import Flask, request, render_template, redirect, url_for
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html', username = '', username_error = '', password = '', password_error = '', verify_password = '', verify_password_error = '', email = '', email_error = '')

@app.route('/', methods=['POST'])
def user_signup():    
    userStr = request.form['username']
    userStrShow = userStr
    passStr = request.form['password']
    verifyPassStr = request.form['verify_password']
    emailStr = request.form['email']
    userStrBlankError = ""
    userStrLenError = ""
    passStrError = ""
    verifyPassStrError = ""
    emailError1 = ""
    emailError2 = ""
    if userStr == "":
        userStrBlankError += "Username cannot be blank."
    elif len(userStr) < 3 or len(userStr) > 20:
        userStrLenError += "Username must be longer than 2 characters and shorter than 20 characters." 
    if passStr == "" or len(passStr) < 3 or len(passStr) > 20: 
        passStrError += "Passsword cannot be blank. Password must be longer than 2 characters and shorter than 20 characters."
    if verifyPassStr == "" or passStr != verifyPassStr:
        verifyPassStrError = ""
        verifyPassStrError += "Passwords don't match."
    if emailStr != "":
        if "@" not in emailStr and "." not in emailStr:
            emailError2 += "Check the formatting of the email address you provided."
        if len(emailStr) < 3 or len(emailStr) > 20:
            emailError1 += "Check the length of the email address you provided."
                  
    if userStrBlankError != "" or userStrLenError != "" or passStrError != "" or verifyPassStrError != "" or emailError1 != "" or emailError2 != "":
        return render_template('form.html', username = userStrShow, username_error = userStrBlankError + " " + userStrLenError, password = "", password_error = passStrError, verify_password = "", verify_password_error = verifyPassStrError, email = emailStr, email_error = emailError1 + " " + emailError2)
    else:
        return redirect(url_for('welcome', finalUsername = userStr))
       
@app.route('/welcome')
def welcome():    
     return render_template('welcome.html',  username = request.args.get('finalUsername'))

app.run()