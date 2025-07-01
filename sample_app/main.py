# #!/usr/bin/env python3
# import socket
# from flask import Flask, render_template, request
# from typing import List, Dict
# from flask import Flask, render_template, request, session, redirect, url_for
# import mysql.connector
# from mysql.connector import Error
# import json

# application = Flask(__name__)

# @application.route("/")
# def home():
#     return render_template("home.html", host_name=socket.gethostname())

# @application.route("/page1")
# def page1():
#     return render_template("page1.html")

# @application.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello %s!' % name

# @application.route('/database')
# def version():
#     config = {
#         'user': 'root',
#         'password': 'secret',
#         'host': '127.0.0.1',
#         'port': '3306',
#         'database': 'mySchema'
#     }
#     try:
#         connection = mysql.connector.connect(**config)
#         cursor = connection.cursor()
#         db_Info = connection.get_server_info()
#         cursor.close()
#         connection.close()
#         return "Connected to MySQL Server {}".format(db_Info)+"<br>"+"If you want to insert users to MySQL, access with /insert"
#     except:
#         return "Oops!! Unable to Connect to MySQL DB"
# if __name__ == "__main__":
#     application.run(host='0.0.0.0')