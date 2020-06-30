from functions import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

sql= "SELECT *from merchant WHERE Id=1"

mycursor.execute(sql)

myresult=mycursor.fetchall()

for x in myresult:
    print(x)
