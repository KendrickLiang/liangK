from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('form.html')
@app.route('/auth')
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.args['username'])
    print(request.headers)
    return render_template('entered.html')
if __name__ == "__main__":
    app.debug = True
    app.run()
