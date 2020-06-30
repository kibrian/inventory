from functions import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

mycursor.execute("CREATE TABLE merchants (Id int(11)AUTO_INCREMENT primary key,merchants_name varchar(255),Address int(11),phone_no int(11))")
