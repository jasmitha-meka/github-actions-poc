import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="mysql",
    port="3306",
    user="test",
    password="test"
 )

  print(mydb.is_connected())
  print("Mysql connection Successful")
except Exception as e:
  print("Mysql connection Unuccessful")  
