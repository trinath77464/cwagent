from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
import logging

app = Flask(__name__)
logging.basicConfig(filename='application.log', level=logging.INFO,format='%(levelname)s:%(message)s')
app.config['MYSQL_HOST'] = 'database-teja.caomyyms75ok.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'teja'
app.config['MYSQL_PASSWORD'] = 'teja8352'
app.config['MYSQL_DB'] ='mydb'

mydb = mysql.connector.connect(
  host="database-teja.caomyyms75ok.us-east-1.rds.amazonaws.com",
  user="teja",
  password="teja8352"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS regform")



mydb = mysql.connector.connect(
  host="database-teja.caomyyms75ok.us-east-1.rds.amazonaws.com",
  user="teja",
  password="teja8352",
  database="mydb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS userdata(username VARCHAR(150), role VARCHAR(150), age INT(3), email VARCHAR(100), hobby VARCHAR(100))")

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        username = details['username']
        logging.info(username)
        role = details['role']
        age = details['age']
        email = details['email']
        hobby = details['hobby']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO userdata(username, role, age, email, hobby) VALUES (%s, %s, %s, %s, %s)", (username, role, age, email, hobby))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


@app.route('/users')
def users():
    cur =mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM userdata")
    if resultValue > 0:
        usersDetails = cur.fetchall()

        return render_template('users.html',usersDetails=usersDetails)

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=80,debug=True)
