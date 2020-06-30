import mysql.connector

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  port="3306",
    database="Clubs_inventory"
  )

mycursor=mydb.cursor()
sql="INSERT INTO merchants(Id,merchants_name,Address,phone_no) VALUES(%s,%s,%s,%s)"
val=("1","kisumu_sportsclub","kisumu","0712345678"),
val=("2","homabay_roster_club","homabay","0716253447")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount,"record inserted")

mycursor.execute("SELECT * FROM merchants")

myresult=mycursor.fetchall()

for record in myresult:
  print(record)

    