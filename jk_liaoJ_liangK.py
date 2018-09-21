#Team Jk -- Joyce Liao, Kendrick Liang
#SoftDev1 pd8
#K09 -- Solidfy
#2018-09-20

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Navigate to /static/seed.html!"

app.debug = True
app.run()


