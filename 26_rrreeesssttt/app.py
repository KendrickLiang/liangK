# Kendrick Liang
# SoftDev1 pd7
# K26 -- Getting More REST
# 2018-11-16 F
import urllib         
import json           

from flask import Flask, render_template 


app = Flask(__name__)
@app.route("/")
def homepage():
    
    USDA_KEY = "ldLj8pq7XcUKiLQP3AvUsUh6v3It05DuDKk7zaN1"
    URL_STUB = "https://api.nal.usda.gov/ndb/search/?q=cheese&format=json&max=5&api_key="
    URL = URL_STUB + USDA_KEY
    u = urllib.request.urlopen(URL)
    response = u.read()
    data = json.loads(response)
    foodName = data['list']['item'][0]['name']
    
    url = 'https://api.twitch.tv/helix/streams?first=1'
    req = urllib.request.Request(url)
    req.add_header("Client-ID","lqxq1fabf3axbkq64ynldvyd2m5pnd")
    resp = urllib.request.urlopen(req)
    data = resp.read()
    dic = json.loads(data)
    print(dic["data"][0]["user_name"])
    
    DICT_KEY = 'https://dictionaryapi.com/api/v3/references/collegiate/json/test?key='
    DICT_URL = '590d0f34-7422-4671-b4a1-b70b179b0c15'
    URL = DICT_KEY + DICT_URL
    x = urllib.request.urlopen(URL)
    str = x.read()
    list = json.loads(str)
    
    return render_template("index.html",
                            food=foodName,
                           image=dic["data"][0]["user_name"],
                           l=list)
if __name__ == "__main__":
    app.debug = True  
app.run()
