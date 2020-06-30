from functions import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

mycursor.execute("SELECT * FROM merchants")

myresult=mycursor.fetchall()

for merchant in myresult:
    print(merchant)

