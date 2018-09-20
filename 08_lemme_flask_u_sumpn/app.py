#Kendrick Liang
#SoftDev1 pd8
#K8 -- Fill Yer Flask
#2018-09-20
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("about to print __name__...")
    print(__name__)
    return "No hablo queso!"
@app.route('/<username>')
def show_user(username):
    return username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return str(post_id)
if __name__ == "__main__":
    app.debug = True
    app.run()
