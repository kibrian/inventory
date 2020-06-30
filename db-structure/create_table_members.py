from functions import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

mycursor.execute ("CREATE TABLE members (Id int(11)AUTO_INCREMENT primary key,member_name  varchar(255),Address  varchar(255),phone_no  int(11),Id_no  int(11),membership_Id  int(11),merchant_Id  int(11))")

