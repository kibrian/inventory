from functions import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

mycursor.execute("CREATE TABLE clubcards (Id int(11)AUTO_INCREMENT  primary key,card_no int(11),serial_no int(11),phone_no int(11),member_Id int(11),card_balance  int(11))")

