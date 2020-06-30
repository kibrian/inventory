from functions import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

mycursor.execute("CREATE TABLE location (Id int(11) AUTO_INCREMENT primary key,location_name  varchar(255),merchant_Id  int(11))")


