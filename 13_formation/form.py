from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('form.html')
@app.route('/auth', method = ["GET", "POST"])
def authenticate():
    print(request.args['username'])
    return render_template('entered.html')
if __name__ == "__main__":
    app.debug = True
    app.run()
