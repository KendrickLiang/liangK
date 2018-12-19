from flask import Flask
from flask import request
from flask import render_template
import urllib
import json
app = Flask(__name__)
@app.route('/')
def home():
    enter = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=BM40zJZKfQRSolaD95desU5DhA0YbS8m73dMzqUf&date=2018-11-15")
    display = enter.read()
    print (display)
    data=json.loads(display)
    PIX_URL = "https://pixabay.com/api/?key=" + "10698567-19efb24bc53e467c50ad5a2ff" + "&q=yellow+flowers&image_type=photo&pretty=true"
    r = urllib.request.urlopen(PIX_URL)
    content = r.read()
    print("content:")
    print(content)
    pix_data = json.loads(content)
    pix_data = pix_data['hits']
    print("pix_data:")
    print(pix_data)
    return render_template("index.html", pic=data['url'], description=data['explanation'], name=pix_data[0]['user'], pic2=pix_data[0]['largeImageURL'], info=pix_data[0]['tags'])
if (__name__ == "__main__"):
    app.debug = True
    app.run()
