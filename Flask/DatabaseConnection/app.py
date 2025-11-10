from flask import *
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='your_sql_password'

mysql =MySQL(app)      #cursor for performing a sql cmd

@app.route('/')
def Home():
  return 'Hi'

if __name__=='__main__':
  app.run(debug=True,port=3157)