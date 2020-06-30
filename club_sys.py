from merchants import merchant
from membership import membership
from clubcards import clubcards
from members import member
from beneficiaries import beneficiaries
from location import location
from agents import agent
from transactions import transactions
from club_functions import insertMerchantsToDb
from club_functions import insertmembershipToDb
from club_functions import insertclubcardsToDb
from club_functions import insertMembersToDb
from club_functions import insertbeneficiariesToDb
from club_functions import insertlocationToDb
from club_functions import insertagentsToDb
from club_functions import inserttransactionsToDb


noofmembers = int(input("Enter No of members: "))

members = []
for x in range(1,noofmembers+1):
    merchants_name =input("Enter merchants_name: ")
    phone_no =int(input("Enter phone_no: "))
    Address =input("Enter Address: ")

    merchants = merchant(merchants_name,Address,phone_no)
    merchantsAddress= insertMerchantsToDb(merchants)
    merchant.Address=merchantsAddress


    member_type=input("Enter the type of member: ")
    membership_Id=input("Enter membership_Id: ")
    membership = membership(member_type,membership_Id)
    membershipmember_Id=insertmembershipToDb(membership)
    membership.member_Id=membershipmember_Id
    
    
    member_name =input("Enter member_name: ")
    Address =input("Enter Address: ")
    phone_no=input("Enter phone_no: ")
    Id_no=input("Enter Id_no: ")
    membership_Id=input("Enter membership_id: ")
    merchant_Id =int(input("Enter merchant_Id: "))
    

    
    members = member(member_name,Address,phone_no,Id_no,membership_Id,merchant_Id)
    memberAddress=insertMembersToDb(members)
    member.Address=memberAddress



    
    card_no=int(input("Enter card_no: "))
    card_balance=int(input("Enter card_balance: "))
    serial_no=input("Enter serial_no: ")
    phone_no=input("Enter phone_no: ")
    member_Id=input("Enter member_Id: ")

    clubcards= clubcards(card_no,serial_no,phone_no,card_balance,member_Id)
    clubcardsbalance=insertclubcardsToDb(clubcards)
    clubcards.balance=clubcardsbalance



noofbeneficiaries = input("Enter noofbeneficiaries: ")

beneficiaries = []
for x in range(noofbeneficiaries+1):
    
    name =input("Enter name: ")
    age =input("Enter age: ")
    phone_no =input("Enter phone_no: ")
    member_Id =input("Enter membership_Id: ")
    Id_no=input("Enter Id_no: ")

    beneficiaries= beneficiaries(name,age,Id_no,phone_no,member_Id)
    beneficiariesage= insertbeneficiariesToDb(beneficiaries)
    beneficiaries.age=beneficiariesage



nooflocaion = int(input("Enter nooflocation: "))

location = []
for x in range(1,nooflocaion+1):
    location_name=input("Enter location_name: ")
    merchant_Id=input("Enter merchant_Id: ")

   
    location = location(location_name,merchant_Id)
    locationmerchant_Id = insertlocationToDb(location)
    location.merchant_Id = locationmerchant_Id


    noofagents = int(input("Enter noofagents: "))

    agents = []
    for x in range(1,noofagents+1):
        agent_name=input("Enter agent_name: ")
        location_Id=input("Enter location_Id: ")

        agents=agent(agent_name,location_Id)
        agentsagent_name=insertagentsToDb(agent)
        agents.agent_name=agentsagent_name



    nooftransactions = int(input("Enter nooftransactions: "))

    transactions = []
    for x in range(1,nooftransactions+1):
        amount=int(input("Enter amount: "))
        balance=int(input("Enter balance: "))
        member_Id=input("Enter mermber_Id: ")
        clubcards_Id=input("Enter clubcards_Id: ")
        agents_Id=input("Enter agents_Id: ")


        transactions= transactions(amount,balance,member_Id,clubcards_Id,agents_Id)
        transactionsamount=inserttransactionsToDb(transactions)
        transactions.amount=transactionsamount

    
    for tran in transactions:
        print(tran.member_Id,tran.amount,tran.balance)
        for mem in members:
            print(mem.member_name,mem.merchant_Id,mem.phone_no)


    










    
    




    





     
