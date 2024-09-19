import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',passwd='TT@york1234',database='car')
mycursor=mycon.cursor()
def login():
    uid=int(input("Enter your userid"))
    mycursor.execute("select * from user")
    for i in mycursor:
        if i[0]==uid:
            up=input("Enter your passwoord")
            if i[2]==up:
                print("Signin successful")
                return(i[5])
            else:
                print("ERROR!!! WRONG PASSWORD")

            break
        else:
            print("ERROR USERID INVALID")
#login()

def insertitem():
    ch='y'
    while ch=='y':
        mycursor.execute("Select * from carinf")
        st1=mycursor.fetchall()
        cn=mycursor.rowcount
        if cn>0:
            Cid=cn+1
        else:
            Cid=1
        Cname=input ("Enter car name: ")
        Ccolour=input ("Enter car colour: ")
        Cfuel=input ("Enter type of fuel: ")
        Cseats=int (input ("Enter no of seats in car: "))
        Cprice=float (input ("Enter car price: "))
        Cstock=int (input ("Enter the car stock: "))
        sg="insert into carinf values('{}','{}','{}',{},{},{})".format(Cname,Ccolour,Cfuel,Cseats,Cprice,Cid)
        sql="insert into car_stock values({},'{}',{})".format(Cid, Cname, Cstock)
        mycursor.execute(sg)
        mycursor.execute(sql)
        mycon.commit()
        ch=input("Type y to enter more rows or press any key to exit: ")

#insertitem()

def updateitem():
    cid=int(input("enter the carid of the car to be updated: "))
    print ("1. update car colour")
    print ("2. update car fuel type")
    print ("3. update no of seats in the car")
    print ("4. update car price")
    print ("5. update car stock")
    ch=int(input("Enter your choice"))
    if ch==1:
        ucc=input ("Enter the new car colour: ")
        up="update carinf set carColor='{}' where carID={}".format(ucc,cid)
        mycursor.execute(up)
        mycon.commit()
        print ("updated successfully")

    elif ch==2:
        ucft=input("Enter the new fuel type of the car: ")
        up="update carinf set carfuel='{}' where carID={}".format(ucft,cid)
        mycursor.execute(up)
        mycon.commit()
        print("updated successfully")
        
    elif ch==3:
        ucs=int(input("Enter the new no of seats of the car: "))
        up="update carinf set Noofseats={} where carID={}".format(ucs, cid)
        mycursor.execute(up)
        mycon.commit()
        print("updated successfully")
        
    elif ch==4:
        ucp=int(input("Enter the new price of the car: "))
        up="update carinf set carPrice={} where carID={}".format(ucp, cid)
        mycursor.execute(up)
        mycon.commit()
        print("updated successfully")

    elif ch==5:
        ucst=int(input("Enter updated stock: "))
        up="update car_stock set stock={} where carID={}".format(ucst, cid)
        mycursor.execute(up)
        mycon.commit()
        print("updated successfully")
        
    else:
        print("Invalid input given")


def displayitem():
    st="select* from carinf"
    mycursor.execute(st)
    for x in mycursor:
        print(x)
        
def displaystock():
    st="select* from car_stock"
    mycursor.execute(st)
    for x in mycursor:
        print (x)
        
def displayCustomer():
    st="select* from cust_omer"
    mycursor.execute(st)
    for x in mycursor:
        print (x)
        
def displayUsers():
    st="select* from user"
    mycursor.execute(st)
    for x in mycursor:
        print (x)
        
def displaySales():
    st="select* from sales"
    mycursor.execute(st)
    for x in mycursor:
        print (x)

def registration ():
    mycursor.execute("Select* From user")
    st1=mycursor.fetchall ()
    cn=mycursor.rowcount
    if cn>0:
        Ui=st1[-1][0]+1
    else:
        Ui=101
    print ("your userid is: ",Ui)
    Un=input ("Enter your name: ")
    Up=input ("Enter your password:")
    Upn=input ("Enter your phone number: ")
    Uadd=input ("Enter your address: ")
    User='Y'
    mycursor.execute("insert into user values ({}, '{}','{}','{}','{}','{}')".format(Ui, Un, Up, Upn, Uadd, User))
    mycon.commit()
#registration()

def billing():
    def choice():
        from datetime import date
        mycursor.execute("Select* From sales")
        stl=mycursor.fetchall()
        cn=mycursor.rowcount
        if cn>0:
            billno=st1[-1][0]+1
        else:
            billno=101

        mycursor.execute("Select* from carinf")
        for x in mycursor:
            print (x)
        mycursor.execute("Select* From cust_omer")
        stl=mycursor.fetchall()
        cnl=mycursor.rowcount
        if cn>0:
            Ci=cn+1
        else:
            Ci=101
        print("Enter the carid of the car you want to buy")
        ch=int(input(""))
        py=input("Enter the payment mode")
        st=("Select carname,carPrice from carinf where carID={}".format(ch))
        mycursor.execute(st)
        st1=mycursor.fetchone()
        print("Car showroom".center(95,'='))
        Ui=int(input("Enter your Userid: "))
        print("Billingno: ",billno)
        print("Date:",date.today())
        print("Carname     Price")
        print(st1[0],"   ",st1[1])
        st="Update car_stock set stock=stock-1 where carID={}".format(ch)
        mycursor.execute(st)
        mycon.commit()
        ist="insert into sales values({},{},'{}',{},{},'{}')".format(billno,ch,date.today(),Ci,st1[1],py)
        mycursor.execute(ist)
        mycon.commit()
        mycursor.execute("Select * from user")
        for x in mycursor:
            ict="insert into cust_omer values({},'{}','{}','{}',{})".format(Ci,x[1],x[4],x[3],x[0])
            mycursor.execute(ict)
            mycon.commit()
    choice()
    
#Mainfunction
c='y'
while c.lower()=='y':
    print("Car Showroom". center (90,"="))
    print("1.Login")
    print("2.Register")
    print("3.Exit")
    cO=int(input("Enter the serial nunber of your choice: "))
    if cO==1:
        u=login()
        if (u=="y"):
            c1='y'
            while cl.lower ()=='y' :
                print ("Car Showroom".center (90,"="))
                print ("1.Display item")
                print ("2.Place order")
                print ("3.Exit")
                ch=int(input ("Enter the serial nunber of your choice: "))
                if ch==1:
                    print ("car information".center (90,"="))
                    displayitem()
                    print ("1.Place order")
                    print ("2.Exit")
                    if ch1==1:
                        billing()
                    elif ch1==2:
                        print ("Good Bye")
                        break
                    else:
                        print ("Invalid choice")
                elif ch==2:
                   billing()
                elif ch==3:
                   break
                else:
                   print("Invallid choice")
                c1= input("Do you want to continue (y/[n]) : ")

        if u=="n":
            c2='y'
            while c2.lower()=='y':
                print ("Welcome admin".center (90,"="))
                print ("1.Display item")
                print ("2.Insert item")
                print ("3.Update item")
                print ("5.View usertable")
                print ("6.View customertable")
                print ("7.View salestable")
                print ("8.View stock")
                print ("9.Exit")
                ch1=int (input ("Enter the serial number of your choice: "))
                if ch1==1:
                    print("car information".center(90,"=") )
                    displayitem()
                elif chl==2:
                    print("inserting information".center(90,"="))
                    insertitem()
                elif ch1==3:
                    print("Updating information". center(90,"="))
                    updateitem()
                elif chl==5:
                    print("User Table". center(90,"="))
                    displayUsers()
                elif chl==6:
                    print("Customer table".center(90,"="))
                    displayCustomer()
                elif chl==7:
                    print("Sales table".center(90,"="))
                    displayCustomer()
                elif chl==8:
                    print("Car stock".center(90,"="))
                    displayCustomer()
                elif chl==9:
                    print("Goodbye")
                c2=input("Do you want to continue yes or no:")

    elif cO==2:
        registration()
    elif cO==3:
        print("Good bye")
        break
    else:
        print("INVALID CHOICE")
        c=input("Do you want to return to main menu (y/[n]): ")
else:
    print("GOOD BYE")
                    










                    
                   

                
                        
