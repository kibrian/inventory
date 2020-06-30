from functions import createDbconnection

dbconnection=createDbconnection()

mycursor=dbconnection.cursor()

mycursor.execute("CREATE TABLE membership (id int(11) AUTO_INCREMENT  primary key,member_type varchar(255))")







