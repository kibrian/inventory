from functions import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

mycursor.execute("CREATE TABLE transactions(Id int(11)AUTO_INCREMENT primary key,amount int(11),balance int(11),member_Id int(11),agents_Id int(11),clubcards_Id int(11))")

