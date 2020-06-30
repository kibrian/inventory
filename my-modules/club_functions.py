import mysql.connector

def createDbconnection():
  mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  port="3306",
    database="clubs_inventory"
  )
  return mydb

def insertMerchantsToDb(merchants):
  mydbconnection=createDbconnection()
  sql="INSERT INTO merchants(merchants_name,Address,phone_no) VALUES(%s,%s,%s)"
  val=(merchants.merchants_name,merchants.Address,merchants.phone_no)
  mycursor=mydbconnection.cursor()
  mycursor.execute(sql,val)
  mydbconnection.commit()
  print(mycursor.rowcount,"record inserted.")


  sqlselect="select * from merchants WHERE merchants_name=%s"
  val=(merchants.merchants_name,)
  mycursor.execute(sqlselect,val)
  insertedmerchants=mycursor.fetchone()
  print(insertedmerchants)

  for record in insertedmerchants:
    print(record)



  return insertedmerchants [0]

def insertMembersToDb(members):
  mydbconnection=createDbconnection()
  sql="INSERT INTO members (member_name,Address,phone_no,Id_no,merchant_Id,membership_Id) VALUES (%s,%s,%s,%s,%s,%s)"
  val=(members.member_name,members.Address,members.phone_no,members.Id_no,members.merchant_Id,members.membership_Id)
  mycursor=mydbconnection.cursor()
  mycursor.execute(sql,val)
  mydbconnection.commit()
  print(mycursor.rowcount,"record inserted.")



  sqlselect="select * From members where Id_no='%s'"
  val=(members.Id_no)
  mycursor.execute(sqlselect,val)
  insertedMembers=mycursor.fetchone()
  print(insertedMembers)
    



def insertmembershipToDb(membership):
  mydbconnection=createDbconnection()
  sql="INSERT INTO membership(member_type,membership_Id) VALUES(%s,%s)"
  val=(membership.member_type,membership.membership_Id)
  mycursor=mydbconnection.cursor()
  mycursor.execute(sql,val)
  mydbconnection.commit()
  print(mycursor.rowcount,"membership record inserted")


  sqlselect="select *from membership where membership_Id='%s'"
  val=(membership.membership_Id)
  mycursor.execute(sqlselect,val)
  insertedmembership=mycursor.fetchone()
  print(insertedmembership)
  for mbrship in insertedmembership:
    print(mbrship)

  return insertedmembership[0]




def insertbeneficiariesToDb(beneficiaries):
  mydbconnection=createDbconnection()
  sql="INSERT INTO beneficiaries(name,age,phone_no,Id_no,mermber_Id)VALUES(%s,%s,%s,%s,%s)"
  val=(beneficiaries.name,beneficiaries.age,beneficiaries.phone_no,beneficiaries.Id_no,beneficiaries.mermber_Id)
  mycursor=mydbconnection.cursor()
  mycursor.execute(sql,val)
  mydbconnection.commit()
  print(mycursor.rowcount,"beneficiary inserted")


  sqlselect="select *from beneficiaries where Id_no='%s'"
  val=(beneficiaries.Id_no)
  mycursor.execute(sqlselect,val)
  insertedbeneficiaries=mycursor.fetchone()
  print(insertedbeneficiaries)
  for x in beneficiaries:
    print(x) 

  return insertedbeneficiaries[0]



def insertclubcardsToDb(clubcards):
  mydbconnection=createDbconnection()
  sql="INSERT INTO clubcards(card_no,serial_no,phone_no,card_balance,member_Id)VALUES(%s,%s,%s,%s,%s)"
  val=(clubcards.card_no,clubcards.serial_no,clubcards.phone_no,clubcards.card_balance,clubcards.member_Id)
  mycursor=mydbconnection.cursor()
  mycursor.execute(sql,val)
  mydbconnection.commit()
  print(mycursor.rowcount,"clubcards inserted")



  sqlselect="select *from clubcards where card_balance='%s'"
  val=(clubcards.card_balance)
  mycursor.execute(sqlselect,val)
  insertedclubcards=mycursor.fetchone()
  print(insertedclubcards)
  
  for card in insertedclubcards:
    print(card)

  return insertedclubcards[0]


def insertlocationToDb(location):
  mydbconnection=createDbconnection()
  sql="INSERT INTO location(location_name,merchant_Id)VALUES(%s,%s,%s)"
  val=(location.location_name,location.merchant_Id)
  mycursor=mydbconnection.cursor()
  mycursor.execute(sql,val)
  mydbconnection.commit()
  print(mycursor.rowcount,"location inserted")
   

  sqlselect="select *from location where merchant_Id='%s'"
  val=(location.merchant_Id)
  mycursor.execute(sqlselect,val)
  insertedlocation=mycursor.fetchone()
  print(insertedlocation)
  for x in insertedlocation:
    print(x)


  return insertedlocation[0]



def insertagentsToDb(agents):
  mydbconnection=createDbconnection()
  sql="INSERT INTO agents(agent_name,location_Id)VALUES(%s,%s,%s)"
  val=(agents.agent_name,agents.location_Id)
  mycursor=mydbconnection.cursor()
  mycursor.execute(sql,val)
  mydbconnection.commit()
  print(mycursor.rowcount,"agents inserted")


  sqlselect="select *from agents where location_Id='%s'"
  val=(agents.location_Id)
  mycursor.execute(sqlselect,val)
  insertedagents=mycursor.fetchone()
  print(insertedagents)
  
  for agent in insertedagents:
    print(agent)


  return insertedagents[0]


def inserttransactionsToDb(transactions):
  mydbconnection=createDbconnection()
  sql="INSERT INTO transactions(date,amount,balance,member_Id,clubcards_Id,agents_Id)VALUES(%s,%s,%s,%s,%s,%s,%s)"
  val=(transactions.date,transactions.amount,transactions.balance,transactions.member_Id,transactions.clubcards_Id,transactions.agents_Id)
  mycursor=mydbconnection.cursor()
  mycursor.execute(sql,val)
  mydbconnection.commit()
  print(mycursor.rowcount,"transactions inserted")



  sqlselect="select *from transactions where amount='%s'"
  val=(transactions.amount)
  mycursor.execute(sqlselect,val)
  insertedtransactions=mycursor.fetchone()
  print(insertedtransactions)
  for tran in insertedtransactions:
    print(tran)


  return insertedtransactions[0]
    
   
  
     


