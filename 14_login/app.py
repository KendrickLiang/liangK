#Blue_Rainbow Shin Bamba, Kendrick Liang
#SoftDev1 pd8
#K14 Do_I_Know_You?
#2018-10-01
import os

from flask import Flask, render_template, request, url_for, redirect, session
app = Flask(__name__)

app.secret_key = os.urandom(32)#Generate random key to assign to secret_key

user = "BlueRainbow" #Account Username
passwd = "softdev" #Account Password

@app.route("/")
def home():
	#print(user)
	#print(passwd)
	if 'BlueRainbow' in session: #if User is logged on
		return render_template("welcome.html", user = 'BlueRainbow')
	else:
		return render_template("page.html")

@app.route("/auth", methods = ["POST", "GET"])
def woah():
	#print(app)
	#print(request)
	#print(request.method)
	#print(request.form)
	if request.form["username"] == user and request.form["password"] == passwd:
		session['BlueRainbow'] = 'softdev'#logs in user
		return redirect(url_for('home'))#Send to welcome page
	else: #If username/password are not correct send to error page
		if request.form["username"] != user:
			message = "bad username"#if wrong username
		elif request.form["password"] != passwd:
			message = "bad password"#if wrong password
		else:
			message = "bad juju"
		return render_template("error.html",
								error = message)#go to error page

@app.route("/logout", methods = ["POST", "GET"])
def gohome():
	#print(session)
	session.pop('BlueRainbow')#logs out user
	return redirect(url_for('home'))#Send to login page
	
if __name__ == "__main__":
    app.debug = True
    app.run()
