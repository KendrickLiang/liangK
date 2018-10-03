#Blue_Rainbow Shin Bamba, Kendrick Liang
#SoftDev1 pd8
#K15 Oh yes, perhaps I do...
#2018-10-02
import os

from flask import Flask, render_template, request, url_for, redirect, session, flash
app = Flask(__name__)

app.secret_key = os.urandom(32)#Generate random key to assign to secret_key

user = "BlueRainbow" #Account Username
passwd = "softdev" #Account Password

@app.route("/")
def home():
	#print(user)
	#print(passwd)
	if 'BlueRainbow' in session: #if User is logged on
		return render_template("welcome.html", user = 'BlueRainbow')#send to welcome page
	else:
		return render_template("page.html")#send to login page

@app.route("/auth", methods = ["POST", "GET"])
def woah():
	if request.form["username"] == user and request.form["password"] == passwd:
		session['BlueRainbow'] = 'softdev'#logs in user
		return redirect(url_for('home'))#Send to welcome page
	else: #If username/password are not correct send to error page
		if request.form["username"] != user:
			message = "bad username"#if wrong username
		else:
			message = "bad password"#if wrong password
		flash(message)#flashes error message
		return render_template("error.html")#go to error page

@app.route("/logout", methods = ["POST", "GET"])
def gohome():
	session.pop('BlueRainbow',None)#logs out user. None used if no users are logged in
	return redirect(url_for('home'))#Send to login page

if __name__ == "__main__":
    app.debug = True
    app.run()
