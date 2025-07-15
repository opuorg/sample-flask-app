from flask import render_template, Blueprint, current_app
import socket
import mysql.connector
from mysql.connector import Error

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html", host_name=socket.gethostname())

@main.route("/upload")
def upload():
    return render_template("upload.html", host_name=socket.gethostname())

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route('/database')
def version():
    config = {
        'user': current_app.config['DATABASE_USER'],
        'password': current_app.config['DATABASE_PASSWORD'],
        'host': current_app.config['DATABASE_HOST'],
        'port': '3306',
        'database': current_app.config['DATABASE_NAME'],
    }
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        db_Info = connection.get_server_info()
        cursor.close()
        connection.close()
        return "Connected to MySQL Server {}".format(db_Info)+"<br>"+"If you want to insert users to MySQL, access with /insert"
    except:
        return "Oops!! Unable to Connect to MySQL DB"