from flask import render_template, Blueprint
import socket
import mysql.connector
from mysql.connector import Error

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html", host_name=socket.gethostname())

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route('/database')
def version():
    config = {
        'user': 'root',
        'password': 'secret',
        'host': '127.0.0.1',
        'port': '3306',
        'database': 'mySchema'
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