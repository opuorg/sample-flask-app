#!/usr/bin/env python3
import socket
from flask import Flask, render_template, request

application = Flask(__name__)

@application.route("/")
def home():
    return render_template("home.html", host_name=socket.gethostname())

@application.route("/page1")
def page1():
    return render_template("page1.html")

@application.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

if __name__ == "__main__":
    application.run(host='0.0.0.0')