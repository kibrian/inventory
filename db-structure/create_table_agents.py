from functions import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

mycursor.execute("CREATE TABLE agents (Id int(11) AUTO_INCREMENT primary key,agent_name  varchar(255),location_Id int(11))")

