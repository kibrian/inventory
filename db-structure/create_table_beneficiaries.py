from functions import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

mycursor.execute ("CREATE TABLE beneficiaries (Id int(11) AUTO_INCREMENT primary key,name varchar(255),age  int(11),Id_no int(11),phone_no  int(11),member_Id  int(11))")

