from flask import Flask, request, Response, render_template
import os
from io import BytesIO
from gtts import gTTS
import socket  

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/")
def home():

    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '

    return render_template("index.html", computername=hostname)

@app.route("/menu")
def menu():
    return render_template("menu.html")


if __name__ == '__main__':
    app.run('0.0.0.0', 80, debug=True) 
