import mysql.connector 
con=mysql.connector.connect(host="localhost",user='root',passwd='',database='project') 
vehCur=con.cursor()
 #pgm to create table bike
vehCur.execute('create table bikes(Sl_No int,MODEL  char(30) primary key,COLOURS_AVAILABLE char(50),FUEL_TYPE varchar(20),BODY_TYPE varchar(30),MILEAGE float, TRANSMISSION varchar(20),ENGINE_TYPE char(50),FUEL_TANK_CAPACITY float,No_Of_CYLINDERS int,KERB_WEIGHT float,DISPLACEMENT float,EMISSION_STANDARD char(25),PRICE float,STOCK_LEFT int)')  
vehCur.execute("insert into bikes values(1,'APACHE RR 310','BLACK,RED,MAROON','PETROL','SPORTS BIKE',35,'MANUAL','SINGLE CYLINDER,4-STROKE,4-VALUE,REVERSE INCLINED DOHC S1 ENGINE',11,1,174,312.22,'bs6',219000,10)")
vehCur.execute("insert into bikes values(2,'APACHE RTR 160','BLUE,RED,BLACK,GREY,MAROON,WHITE','PETROL','SPORTS NAKED BIKES',47,'MANUAL','S1,4-STROKE,AIR-COOLED',12,1,174,159.7,'bs6',130000,20)")
vehCur.execute("insert into bikes values(3,'TVS STAR CITY PLUS','RED,WHITE','PETROL','COMMUTER BIKES',65,'MANUAL','SINGLE LINE,4 STROKE,AIR COOLED',10,1,116,109.7,'bs6',84561,100)")
vehCur.execute("insert into bikes values(4,'BAJAJ PULSAR F250','RED,GREY','PETROL','SPORTS BIKE',39,'MANUAL','SINGLE CYLINDER 4 STROKE SOHC2 VALVE OIL COOLED',14,1,162,249.07,'bs6',165000,50)")
vehCur.execute("insert into bikes values(5,'ROYAL ENFIELD BULLET 350','BLACK,RED,BLUE','PETROL','CRUISER BIKES',35,'MANUAL','SINGLE CYLINDER 4 STROKE,AIR COOLED FUEL INJECTION',13.5,1,191,346,'bs6',182000,20)")
vehCur.execute("insert into bikes values(6,'HONDA HORNET 2.0','BLUE,BLACK','PETROL','SPORTS NAKED BIKES',45,'MANUAL','4 STROKE,SL ENGINE,BS VI',12,1,142,184.4,'bs6',152000,100)")
vehCur.execute("insert into bikes values(7,'HONDA UNICORN','BLACK,GREY,RED','PETROL','COMMUTER BIKES',60,'MANUAL','4 STROKE,S1,BS-VI ENGINE',13,1,193,162.7,'bs6',177000,350)")
vehCur.execute("insert into bikes values(8,'ROYAL ENFIELD HIMALAYAN','MIRAGE SILVER','PETROL','ADVENTURE TOURER BIKES',36,'MANUAL','SINGLE CYLINDER,4 STROKE,AIR COOLED,SOHC',15.5,1,195,411,'bs6',242000,5)")
vehCur.execute("insert into bikes values(9,'HARLEY DAVIDSON ELECTRA GLIDE STANDARD','BLACK','PETROL','TOURER BIKES',18,'MANUAL','MILWAKEE-EIGHT R 107',22.7,2,354,1745,'bs6',2779000,10)")
vehCur.execute("insert into bikes values(10,'BMW R NINE T SCRAMBLER','GREY,BROWN,BLUE','PETROL','CAFE RACER BIKES',19.6,'MANUAL','Air/Oil cooled 2-cylinder,4-stroke,boxer engine with 2 camshafts & 4 radially arranged valves per cylinder as well as central counter balance shaft',17,2,223,1170,'bs6',1865000,10)")
vehCur.execute("insert into bikes values(11,'HERO XTREME 160R','RED','PETROL','SPORTS NAKED BIKES',19.6,'MANUAL','AIR COOLED,4 STROKE,2 VALVE SINGLE CYLINDER OHC',12,1,139.5,163,'bs6',134000,410)")
vehCur.execute("insert into bikes values(12,'SUZUKI INTRUDER','GREY,BLACK','PETROL','CRUISER BIKES',44,'MANUAL','4-STROKE,1-CYLINDER AIRCOOLED,SOHC',11,1,152,155,'bs6',148000,20)")
vehCur.execute("insert into bikes values(13,'DUCCATI STREETFIGHTER V4','BLACK','PETROL','SUPER BIKES',13,'MANUAL','Desmosedici strodale 90 VA',16,4,199,1103,'bs6',2577000,32)")
vehCur.execute("insert into bikes values(14,'KTM 200 DUKE','ORANGE,WHITE','PETROL','SPORTS NAKED BIKES',35,'MANUAL','SINGLE CYLINDER,4 VALVE LIQUID COOLED,F1,DOHC',13.5,1,159,199.5,'bs6',210000,100)")
vehCur.execute("insert into bikes values(15,'KAWASAKI NINJA ZX-10R','-','PETROL','SUPER BIKES',15,'MANUAL','LIQUID COOLED, 4-STROKE IN LINE FOUR',17,4,207,998,'bs6',1713000,2)")

#pgm to create table scooter
 
vehCur.execute("CREATE TABLE scooter(Sl_No int,MODEL char(25) primary key,COLOURS_AVAILABLE char(50),ENGINE_TYPE char(50),RANGE_ESCOOTER int,MOTOR_POWER int,CHARGING_TIME float,BATTERY_CAPACITY float,CHASSIS char(25),TOP_SPEED float, MILEAGE float,DISPLACEMENT float,EMISSION_STANDARD char(20),FUEL_TANK_CAPACITY float,LOAD_CAPACITY int,PRICE float,WARRANTY int,STOCK_LEFT int)")
vehCur.execute("INSERT INTO scooter VALUES(1,'BMW C 400 GT','Cherry Red,Blue,Pastel Pink,Black,White','Water-cooled, single-cylinder, 4 stroke engine, 4 valves per cylinder, overhead camshaft',Null,Null,Null,Null,Null,93.56,53.5,124.5,'BS6',12.8,201,950000,6,30)")
vehCur.execute("INSERT INTO scooter VALUES(2,'Suzuki Burgman Street','Red,Blue,Baby Pink,Black,White,Dark Green','4-Stroke, 1 Cylinder, Air Cooled',Null,Null,Null,Null,Null,90.48,46.85,124,'BS6',5.5,110,77500,5,350)")
vehCur.execute("INSERT INTO scooter VALUES(3,'Bajaj Chetak','Cherry Red,Blue,Pastel Blue,Black,White,Yellow,Grey','Single Cylinder, 4 stroke, Air cooled, 3 valves',Null,Null,Null,Null,Null,70,50.25,125,'BS6',8.4,126,350000,4,42)")
vehCur.execute("INSERT INTO scooter VALUES(4,'Hero Maestro 125','Yellow,Blue,Pink,Black,White','Air Cooled, 4-Stroke, SI Engine',Null,Null,Null,Null,Null,95.26,45.83,124.6,'BS6',5,122,74300,3,33)")
vehCur.execute("INSERT INTO scooter VALUES(5,'Honda Activa 125','Red,Blue,Yellow,Black,White,Purple,Grey','Fan Cooled, 4 Stroke, BS-VI Engine',Null,Null,Null,Null,Null,92.46,48.2,124,'BS6',5.3,111,82800,2,30)")
vehCur.execute("INSERT INTO Scooter VALUES(6,'Ather 450X','Charcoal Black',Null,100,5400,5.45,2.9,'Aluminium Cast',80,Null,Null,Null,Null,108,118000,3,20)")
vehCur.execute("INSERT INTO Scooter VALUES(7,'Simple One STD','Sky Blue',Null,236,4500,1.08,4.8,'Tubular',105,Null,Null,Null,Null,110,109000,4,25)")
vehCur.execute("INSERT INTO Scooter VALUES(8,'Ola S1','Cherry Red',Null,121,8500,4.48,2.98,'Tubular',90,Null,Null,Null,Null,121,85099,2,24)")
vehCur.execute("INSERT INTO Scooter VALUES(9,'TVS iQube Electric','White',Null,75,4400,6,2.7,'Telescopic',78,Null,Null,Null,Null,118,100000,3,18)")
vehCur.execute("INSERT INTO Scooter VALUES(10,'Hero Electric Optima','Cherry Red',Null,85,250,4.5,30,'Aluminium Cast',25,Null,Null,Null,Null,88,51400,3,30)")
con.commit()
 
#pgm to create table cars
 
vehCur.execute("CREATE TABLE Cars (Sl_No int, MODEL varchar(20),COLOURS_AVAILABLE varchar(100),FUEL_TYPE char(10),FUEL_TANK_CAPACITY_Litres float,EMISSION_STANDARD char(5), BODY_TYPE varchar(20),MILEAGE_kmpl float, PRICE float, INSURANCE int, WARRANTY int, STOCK_LEFT int)" )
vehCur.execute("INSERT INTO Cars VALUES(1,'Maruti Swift','White,Grey,Silver,Red,Orange,Blue','petrol',37.0,'BS6','Hatchback',23.76,982268,43878,5,14)")
vehCur.execute("INSERT INTO Cars VALUES(2,'Maruti Baleno','White,Grey,Silver,Red,Blue','petrol',37.0,'BS6','Hatchback',19.56,1081968,41518,6,9)")
vehCur.execute("INSERT INTO Cars VALUES(3,'Maruti Celerio','White,Grey,Red,Black','petrol',32.0,'BS6','Hatchback',26.00,774442,31862,4,10)")
vehCur.execute("INSERT INTO Cars VALUES(4,'Tata Altroz','White,Grey,Red,Black,Brown','diesel',37.0,'BS6','Hatchback',19.05,1048755,37712,5,8)")
vehCur.execute("INSERT INTO Cars VALUES(5,'Tata Tiago','White,Grey,Red,Blue,Black','petrol',35.0,'BS6','Hatchback',23.84,818637,30294,4,11)")
vehCur.execute("INSERT INTO Cars VALUES(6,'Hyundai i20','White,Grey,Red,Black','diesel',37.0,'BS6','Hatchback',20.28,1320806,40763,6,7)")
vehCur.execute("INSERT INTO Cars VALUES(7,'Honda Amaze','White,Grey,Silver,Black','diesel',35.0,'BS6','Sedan',18.6,1016430,34325,6,5)")
vehCur.execute("INSERT INTO Cars VALUES(8,'Toyota Fortuner','White,Grey,Silver,Black,Brown','diesel',80.0,'BS6','SUV',8.0,4407401,165296,7,3)")
vehCur.execute("INSERT INTO Cars VALUES(9,'Mahindra Scorpio','White,Red,Black','diesel',60.0,'BS6','SUV',20.5,1578589,63148,6,5)")
vehCur.execute("INSERT INTO Cars VALUES(10,'MG Hector','White,Red,Black,Brown,Blue','diesel',60.0,'BS6','SUV',20.0,1823465,67647,4,2)")
vehCur.execute("INSERT INTO Cars VALUES(11,'Hyundai Creta','White,Red,Orange,Silver,Black','diesel',50.0,'BS6','SUV',21.4,1579089,53018,5,4)")
vehCur.execute("INSERT INTO Cars VALUES(12,'Hyundai Venue','White,Red,Silver,Black','diesel',45.0,'BS6','SUV',23.7,1236679,44185,5,3)")
vehCur.execute("INSERT INTO Cars VALUES(13,'Kia Seltos','White,Grey,Silver,Black,Red,Orange,Blue','diesel',50.0,'BS6','SUV',20.6,2137249,65884,4,5)")
vehCur.execute("INSERT INTO Cars VALUES(14,'Tata Nexon','White,Grey,Red','diesel',44.0,'BS6','SUV',21.5,1568365,47903,4,1)")
vehCur.execute("INSERT INTO Cars VALUES(15,'Tata Harrier','White,Grey,Black','diesel',50.0,'BS6','SUV',17.0,2515732,87838,7,2)")
vehCur.execute("INSERT INTO Cars VALUES(16,'Mahindra Bolero','White,Silver','diesel',60.0,'BS6','SUV',16.0,1130629,37103,5,4)")
vehCur.execute("INSERT INTO Cars VALUES(17,'Toyota Innova Crysta','White,Grey,Red,Black','diesel',55.0,'BS6','MUV',12.0,2182707,94547,5,2)")
vehCur.execute("INSERT INTO Cars VALUES(18,'Mercedes-Benz V-Class','White,Silver,Black,Blue','diesel',57.0,'BS6','MUV',16.0,8407709,302309,6,1)")
vehCur.execute("INSERT INTO Cars VALUES(19,'Kia Carnival','White,Silver,Black','diesel',60.0,'BS6','MUV',14.11,3033800,108395,7,1)")
vehCur.execute("INSERT INTO Cars VALUES(20,'Maruti Ertiga','White,Silver,Black,Red,Blue','diesel',45.0,'BS6','MUV',19.01,910879,41504,5,0)")
vehCur.execute("INSERT INTO Cars VALUES(21,'Renault Triber','White,Silver,Blue,Mustard','petrol',40.0,'BS6','MUV',20.0,629520,30100,4,2)")
vehCur.execute("INSERT INTO Cars VALUES(22,'BMW X5','White,Black,Blue','diesel',80.0,'BS6','SUV',13.38,9044132,323132,5,1)")
vehCur.execute("INSERT INTO Cars VALUES(23,'BMW Z4','White,Black,Blue,Red','petrol',52.0,'BS6','Convertible',11.29,9549712,347812,6,0)")
vehCur.execute("INSERT INTO Cars VALUES(24,'Porsche 911','White,Black,Orange,Red,Yellow,Blue,Green','petrol',64.0,'BS6','Coupe',18.24,35409595,1216045,5,0)")
vehCur.execute("INSERT INTO Cars VALUES(25,'Bentley Continental','Silver,Black,Green,Yellow','petrol',90.0,'BS6','Convertible',9.8,44990236,1537710,5,1)")
vehCur.execute("INSERT INTO Cars VALUES(26,'Mercedes-Benz C-Class','White,Black,Blue','diesel',66.0,'BS6','Sedan',12.6,6023331,144211,5,1)")
vehCur.execute("INSERT INTO Cars VALUES(27,'Mercedes-Benz E-Class','White,Silver,Black','diesel',80.0,'BS6','Sedan',16.1,7775740,177081,5,0)")
vehCur.execute("INSERT INTO Cars VALUES(28,'Rolls-Royce Ghost','White,Silver,Black,Blue','petrol',90.0,'BS6','Sedan',6.33,79853217,2708217,6,0)")
vehCur.execute("INSERT INTO Cars VALUES(29,'Rolls-Royce Phantom','White,Silver,Black,Red,Blue','petrol',100.0,'BS6','Sedan',9.8,103283890,3494890,6,0)")
vehCur.execute("INSERT INTO Cars VALUES(30,'Rolls-Royce Dawn','Silver,Black,Red,Blue','petrol',100.0,'BS6','Convertible',9.8,83873185,2843185,6,0)")
vehCur.execute("INSERT INTO Cars VALUES(31,'Audi RS7','White,Silver,Black,Red,Blue','petrol',73.0,'BS6','Luxury',8.9,25267789,875539,6,0)")
vehCur.execute("INSERT INTO Cars VALUES(32,'Audi Q8','White,Silver,Black,Red,Orange','petrol',85.0,'BS6','SUV',9.8,11684890,419500,5,0)")
vehCur.execute("INSERT INTO Cars VALUES(33,'Audi e-tron','White,Silver,Black,Red,Blue','electric',0.0,'ZEV','SUV',9.8,10199990,0,4,0)")
con.commit()

#To input bank data
vehCur.execute("CREATE TABLE bank(Sl_No int,BANK char(20) primary key,LOWER_LIMIT float,UPPER_LIMIT float)")
vehCur.execute("INSERT INTO bank VALUES(1,'ICICI Bank',8.15,20.00)")
vehCur.execute("INSERT INTO bank VALUES(2,'HDFC Bank',8.00,20.00)")
vehCur.execute("INSERT INTO bank VALUES(3,'SBI Bank',7.70,15.00)")
vehCur.execute("INSERT INTO bank VALUES(4,'Axis Bank',7.00,17.75)")
vehCur.execute("INSERT INTO bank VALUES(5,'CBI Bank',8.90,10.75)")
vehCur.execute("INSERT INTO bank VALUES(6,'Canara Bank',7.30,9.90)")
vehCur.execute("INSERT INTO bank VALUES(7,'Bank Of Baroda',7.00,15.00)")
vehCur.execute("INSERT INTO bank VALUES(8,'Federal Bank',8.50,15.00)")
vehCur.execute("INSERT INTO bank VALUES(9,'IDBI Bank',9.10,9.70)")
vehCur.execute("INSERT INTO bank VALUES(10,'Syndicate Bank',8.85,10.00)")
con.commit()

vehCur.execute("create table Ally_Companies(Sl_no int,Company_name char(30),No_of_Cars int,N0_of_Scooters int, No_of_Bikes int, Total_Products int)") 
 
vehCur.execute("insert into Ally_Companies values(1,'Apache',0,0,2,2)") 
 
vehCur.execute("insert into Ally_Companies values(2,'Ather',0,1,0,1)") 
 
vehCur.execute("insert into Ally_Companies values(3,'Audi',3,0,0,3)") 
 
vehCur.execute("insert into Ally_Companies values(4,'Bajaj',0,1,1,1)") 
 
vehCur.execute("insert into Ally_Companies values(5,'BMW',2,1,1,4)") 
 
vehCur.execute("insert into Ally_Companies values(6,'Duccati',0,0,1,1)") 
 
vehCur.execute("insert into Ally_Companies values(7,'Harley Davidson',0,0,1,1)") 
 
vehCur.execute("insert into Ally_Companies values(8,'Hero',0,2,0,2)") 
 
vehCur.execute("insert into Ally_Companies values(9,'Honda',1,1,2,4)") 
 
vehCur.execute("insert into Ally_Companies values(10,'Hyundai',3,0,0,3)") 
 
vehCur.execute("insert into Ally_Companies values(11,'Kia',2,0,0,2)") 
 
vehCur.execute("insert into Ally_Companies values(12,'KTM',0,0,1,1)") 
 
vehCur.execute("insert into Ally_Companies values(13,'Kawasaki',0,0,1,1)") 
 
vehCur.execute("insert into Ally_Companies values(14,'Maruti',4,0,0,4)") 
 
vehCur.execute("insert into Ally_Companies values(15,'Mahindra',2,0,0,2)") 
 
vehCur.execute("insert into Ally_Companies values(16,'MG Hector',1,0,0,1)") 
 
vehCur.execute("insert into Ally_Companies values(17,'Mercedes Benz',2,0,0,2)") 
 
vehCur.execute("insert into Ally_Companies values(18,'Ola',0,1,0,1)") 
 
vehCur.execute("insert into Ally_Companies values(19,'Renault',1,0,0,1)") 
 
vehCur.execute("insert into Ally_Companies values(20,'Royal Enfield',0,0,2,2)") 
 
vehCur.execute("insert into Ally_Companies values(21,'Rolls Royce',3,0,0,3)") 
 
vehCur.execute("insert into Ally_Companies values(22,'Simple One',0,1,0,1)") 
 
vehCur.execute("insert into Ally_Companies values(23,'Suzuki',0,1,1,2)") 
 
vehCur.execute("insert into Ally_Companies values(24,'Tata',4,0,0,4)") 
 
vehCur.execute("insert into Ally_Companies values(25,'Toyota',2,0,0,2)") 
 
vehCur.execute("insert into Ally_Companies values(26,'TVS',0,1,1,2)")
con.commit()  
#To create Customers Table
vehCur.execute("create table Customers(Customer_ID int primary key,Name varchar(30),Phone_No int,Date_Of_Purchase date,Vehicle_Name varchar(20), Vehicle_Cost int,EMI_amountpermonth int,Final_Amount int)")
#To create employee table
vehCur.execute("CREATE TABLE Employee(Sl_No int,EMPLOYEE_ID char(30),FIRST_NAME char(20),SURNAME char(20),AGE int,YEAR_OF_JOINING int,POSITION char(20),BASIC_PAY float,DEARANCE_ALLOWANCE float,TRAVEL_ALLOWANCE float,HRA float,INCOME_TAX float,PF float,NET_PAY float,NO_OF_VEHICLES_SOLD float)")

#GLOBAL VARIABLES
SlNo=1 #Serial Number for Employee Table
nob=0
noc=0
nos=0
amnt=0
bsod=0
SlNO=1

#FUNCTIONS
#Code for inputting employee details
def employee():
     con=mysql.connector.connect(host="localhost",user='root',passwd='',database='project') 
     vehCur=con.cursor()
     global SlNo
     while True:
        print()
        eId=input("Enter Employee ID: ")
        fn=input("Enter First Name of the Employee: ")
        sn=input("Enter Surname of the Employee: ")
        age=int(input("Enter the age of the Employee: "))
        yoj=int(input("Enter the year the Employee joined the company: "))
        p=False
        bp=0
        da=0
        ta=0
        hra=0
        pf=0
        it=0
        np=0
        while p==False:
            po=input("Enter the position of the Employee: ")
            p=True
            if(po.upper()=="SALES MANAGER"):
                bp=60000
                da=0.20*bp
                ta=0.10*bp
                hra=0.30*bp
                pf=0.15*bp
                it=0.20*bp
            elif(po.upper()=="ASSISTANT MANAGER"):
                bp=55000
                da=0.18*bp
                ta=0.12*bp
                hra=0.25*bp
                pf=0.13*bp
                it=0.20*bp
            elif(po.upper()=="SALESPERSON"):
                bp=56000
                da=0.15*bp
                ta=0.15*bp
                hra=0.23*bp
                pf=0.12*bp
                it=0.20*bp
            elif(po.upper()=="SECURITY GUARD"):
                bp=27500
                da=0.13*bp
                ta=0.15*bp
                hra=0.20*bp
                pf=0.12*bp
                it=0.30*bp
            elif(po.upper()=="ACCOUNTANT"):
                bp=50000
                da=0.17*bp
                ta=0.10*bp
                hra=0.24*bp
                pf=0.13*bp
                it=0.30*bp
            elif(po.upper()=="RECEPTIONIST"):
                bp=42000
                da=0.15*bp
                ta=0.12*bp
                hra=0.23*bp
                pf=0.13*bp
                it=0.30*bp
            elif(po.upper()=="SWEEPER"):
                bp=24000
                da=0.13*bp
                ta=0.15*bp
                hra=0.20*bp
                pf=0.12*bp
                it=0.30*bp
            elif(po.upper()=="MECHANIC"):
                bp=45000
                da=0.10*bp
                ta=0.15*bp
                hra=0.22*bp
                pf=0.13*bp
                it=0.30*bp
            else:
                print("Wrong Input.Please try again")
                p=False
        np=bp+da+ta+hra-pf-it
        vs=int(input("Enter no of vehicles sold till date: "))
        dat="INSERT INTO Employee VALUES("+str(SlNo)+",'"+eId+"','"+fn+"','"+sn+"',"+str(age)+","+str(yoj)+",'"+po+"',"+str(bp)+","+str(da)+","+str(ta)+","+str(hra)+","+str(pf)+","+str(it)+","+str(np)+","+str(vs)+")"
        vehCur.execute(dat)
        con.commit()
        SlNo+=1
        ch=input("Do you want to enter details of more employees?(Y/N): ")
        if(ch=="N" or ch=="n"):
            break

#Comparison between models
def Comparison(v):
        global noc
        global nob
        global nos
        global Vehicle
        global Vehicledata
        global Vc
        import mysql.connector
        Vcon=mysql.connector.connect(host="localhost",user="root",passwd="",database="Project")
        Vcur=Vcon.cursor()
        if v==1:
            b="Yes"
            while b=="Yes":
                Vcur.execute("select MODEL from bikes")
                bNames=Vcur.fetchall()
                print("Select from:")
                blist=[]
                for bMname in bNames:
                    print(bMname[0])
                    blist.append(bMname[0])
                print()
                bn1=input("Enter name of first bike: ")
                bn2=input("Enter name of second bike: ")
                print()
                
                if bn1 and bn2 in blist:
                    Vcur.execute("select * from bikes where MODEL='"+bn1+"'")
                    Datab1=Vcur.fetchone()
                    print()
                    Vcur.execute("select * from bikes where MODEL='"+bn2+"'")
                    Datab2=Vcur.fetchone()
                    print("COLOURS AVAILABLE\n",Datab1[1],":",Datab1[2],"\n"+Datab2[1],":"+Datab2[2],"\nFUEL TYPE\n",Datab1[1],":"+Datab1[3],"\n",Datab2[1],":",Datab2[3],
                          "\nBODY TYPE\n",Datab1[1],":",Datab1[4],"\n",Datab2[1],":",Datab2[4],"\nMILEAGE(kmpl)\n",Datab1[1],":",Datab1[5],"\n",Datab2[1],":",Datab2[5],
                          "\nTRANSMISSION\n",Datab1[1],":",Datab1[6],"\n",Datab2[1],":",Datab2[6],"\nENGINE TYPE\n",Datab1[1],":",Datab1[7],"\n",Datab2[1],":",Datab2[7],
                          "\nFUEL TANK CAPACITY(L)\n",Datab1[1],":",Datab1[8],"\n",Datab2[1],":",Datab2[8],"\nNo Of CYLINDERS\n",Datab1[1],":",Datab1[9],"\n",Datab2[1],":",Datab2[9],
                          "\nKERB WEIGHT\n",Datab1[1],":",Datab1[10],"\n",Datab2[1],":",Datab2[10],"\nDISPLACEMENT\n",Datab1[1],":",Datab1[11],"\n",Datab2[1],":",Datab2[11],
                          "\nEMISSION STANDARD\n",Datab1[1],":",Datab1[12],"\n"+Datab2[1],":"+Datab2[12],"\nPRICE\n",Datab1[1],":",Datab1[13],"\n",Datab2[1],":",Datab2[13],
                          "\nWARRANTY\n",Datab1[1],":",Datab1[14],"\n",Datab2[1],":",Datab2[14])
                    print()
                    print()
                    b=input("Do you want to compare again?(Yes/No): ")
                else:
                    print("Model Name entered is wrong. Kindly enter again")
                    b="Yes"
            print("ENTER THE MODEL NAME YOU HAVE CHOSEN")
            Vehicle=input("[Make sure you have chosen the vehicle you wish to buy]:")
            Vcur.execute("select * from bikes where MODEL='"+Vehicle+"'")
            Vehicledata=Vcur.fetchone()
            Vc=Vehicledata[13]
            nob+=1
 
        elif v==2:
            s="Yes"
            while s=="Yes":
                Vcur.execute("select MODEL from scooter")
                sNames=Vcur.fetchall()
                print("Select from:")
                slist=[]
                for sMname in sNames:
                    print(sMname[0])
                    slist.append(sMname[0])
                print()
                sn1=input("Enter name of first scooter: ")
                sn2=input("Enter name of second scooter: ")
                print()
                
                if sn1 and sn2 in slist:                   
                    Vcur.execute("select * from scooter where MODEL='"+sn1+"'")
                    Datas1=Vcur.fetchone()
                    print()
                    Vcur.execute("select * from scooter where MODEL='"+sn2+"'")
                    Datas2=Vcur.fetchone()
                    print("COLOURS AVAILABLE\n",Datas1[1],":",Datas1[2],"\n",Datas2[1],":",Datas2[2],"\nENGINE TYPE\n",Datas1[1],":",Datas1[3],"\n",Datas2[1],":",Datas2[3],
                          "\nRANGE_ESCOOTER\n",Datas1[1],":",Datas1[4],"\n",Datas2[1],":",Datas2[4],"\nMOTOR POWER\n",Datas1[1],":",Datas1[5],"\n",Datas2[1],":",Datas2[5],
                          "\nCHARGING TIME\n",Datas1[1],":",Datas1[6],"\n",Datas2[1],":",Datas2[6],"\nBATTERY CAPACITY\n",Datas1[1],":",Datas1[7],"\n",Datas2[1],":",Datas2[7],
                          "\nCHASSIS\n",Datas1[1],":",Datas1[8],"\n",Datas2[1],":",Datas2[8],"\nTOP SPEED\n",Datas1[1],":",Datas1[9],"\n"+Datas2[1],":",Datas2[9],
                          "\nMILEAGE\n",Datas1[1],":",Datas1[10],"\n",Datas2[1],":",Datas2[10],"\nDISPLACEMENT\n",Datas1[1],":",Datas1[11],"\n",Datas2[1],":",Datas2[11],
                          "\nEMISSION STANDARD\n",Datas1[1],":",Datas1[12],"\n",Datas2[1],":",Datas2[12],"\nFUEL TANK CAPACITY\n",Datas1[1],":",Datas1[13],"\n",Datas2[1],":",Datas2[13],
                          "\nLOAD CAPACITY\n",Datas1[1],":",Datas1[14],"\n",Datas2[1],":",Datas2[14],"\nPRICE\n",Datas1[1],":",Datas1[15],"\n",Datas2[1],":",Datas2[15],
                          "\nWARRANTY\n",Datas1[1],":",Datas1[16],"\n",Datas2[1],":",Datas2[16] )
                    print()
                    print()
                    s=input("Do you want to compare again?(Yes/No):")
                else:
                    print("Model Name entered is wrong. Kindly enter again")
                    s="Yes"
            print("ENTER THE MODEL NAME YOU HAVE CHOSEN")
            Vehicle=input("[Make sure you have chosen the vehicle you wish to buy]:")
            Vcur.execute("select * from scooter where MODEL='"+Vehicle+"'")
            Vehicledata=Vcur.fetchone()
            Vc=Vehicledata[15]
            nos+=1
                
        elif v==3:
            c="Yes"
            while c=="Yes":
                Vcur.execute("select MODEL from Cars")
                cNames=Vcur.fetchall()
                print("Select from:")
                clist=[]
                for cMname in cNames:
                    print(cMname[0])
                    clist.append(cMname[0])
                print()
                cn1=input("Enter name of first Car: ")
                cn2=input("Enter name of second Car: ")
                print()
                
                if cn1 and cn2 in clist:                    
                    Vcur.execute("select * from Cars where MODEL='"+cn1+"'")
                    Datac1=Vcur.fetchone()
                    print()
                    Vcur.execute("select * from Cars where MODEL='"+cn2+"'")
                    Datac2=Vcur.fetchone()
                    print("COLOURS AVAILABLE\n",Datac1[1],":",Datac1[2],"\n",Datac2[1],":",Datac2[2],"\nFUEL TYPE\n",Datac1[1],":",Datac1[3],"\n",Datac2[1],":",Datac2[3],
                          "\nFUEL TANK CAPACITY in Litres\n",Datac1[1],":",Datac1[4],"\n",Datac2[1],":",Datac2[4],"\nEMISSION STANDARD\n",Datac1[1],":",Datac1[5],"\n",Datac2[1],":",Datac2[5],
                          "\nBODY TYPE\n",Datac1[1],":",Datac1[6],"\n",Datac2[1],":",Datac2[6],"\nMILEAGE in kmpl\n",Datac1[1],":",Datac1[7],"\n",Datac2[1],":",Datac2[7],
                          "\nPRICE\n",Datac1[1],":",Datac1[8],"\n",Datac2[1],":",Datac2[8],"\nINSURANCE\n",Datac1[1],":",Datac1[9],"\n",Datac2[1],":",Datac2[9],"\nWARRANTY\n",Datac1[1],":",Datac1[10],"\n",Datac2[1],":",Datac2[10]) 
                    print()
                    print()
                    c=input("Do you want to compare again?(Yes/No):")
                else:
                    print("Model Name entered is wrong. Kindly enter again")
                    c="Yes"
            print("ENTER THE MODEL NAME YOU HAVE CHOSEN")
            Vehicle=input("[Make sure you have chosen the vehicle you wish to buy]:")
            Vcur.execute("select * from Cars where MODEL='"+Vehicle+"'")
            Vehicledata=Vcur.fetchone()
            Vc=Vehicledata[8]
            noc+=1
        print()
        print("DETAILS of",Vehicle,"\n",Vehicledata)
        Vcon.close()
 
#To insert data into customer table
def Customers(N,Phone,date,VehiN,Vcost,emi,fa):
        import mysql.connector as my
        mycon=my.connect(host="localhost",user="root",passwd="",database="Project")
        mycur=mycon.cursor()
        global SlNO                
        mycur.execute("INSERT INTO Customers VALUES("+str(SlNO)+",'"+N+"',"+str(Phone)+",'"+str(date)+"','"+VehiN+"',"+str(Vcost)+","+str(emi)+","+str(fa)+")")
        mycon.commit()
        SlNO+=1
        mycon.close()

#To update agent details
def updateagent():
        import mysql.connector
        UAcon=mysql.connector.connect(host="localhost",database='Project',user='root',passwd='')
        UAcur=UAcon.cursor()
        AgentID=input("Enter Agent ID:")
        UAcur.execute("select NO_OF_VEHICLES_SOLD from Employee where EMPLOYEE_ID="+str(AgentID))
        NO_of_Vehiold=int(UAcur.fetchone()[0])
        UAcur.execute("update Employee set NO_OF_VEHICLES_SOLD="+str(NO_of_Vehiold+1)+" where EMPLOYEE_ID="+str(AgentID))
        UAcon.commit()
        UAcon.close()

#To calculate EMI
def EMIfunc(amount):
        import  mysql.connector as slt 
        EMICon=slt.connect(host='localhost',user='root',password='',database='project')  
        EMICur=EMICon.cursor() 
        EMICur.execute("select * from bank") 
        Data=EMICur.fetchall() 
        for i in Data: 
                print('Bank =',i[1],end='\t') 
                print('Lower Limit =',i[2],end='\t') 
                print('Upper Limit =',i[3],end='\t') 
                print()
        global Bank
        Bank=input('Enter the preferred bank:') 
        rate=float(input('Enter the preferred rate:'))
        Rate=rate/100 
        global time 
        time=int(input('Enter the no.of months: ')) 
        x=(amount*Rate/12)*(1+Rate/12)**time 
        y=((1+Rate/12)**time)-1 
        emi=x/y
        EMICon.commit() 
        EMICon.close()
        return emi


#AGENCY POV
def agency_pov():
  con=mysql.connector.connect(host="localhost",user='root',passwd='',database='project')
  vehCur=con.cursor()

 
  print("                                 ---WELCOME TO PHOENIX AUTOMOBILES' COMPANY PORTAL---")
  while True:
    print()
    print()
    print("PLEASE CHOOSE THE ACTION TO BE CARRIED OUT.")
    print("  1.To add Employee Details.")
    print("  2.To view Employee Details.")
    print("  3.To view Customer Details.")
    print("  4.To view Number of Vehicles sold so far.")
    print("  5.To view Ally Company Details.")
    print("  6.To view Amount Collected so far with the Biggest Sale Of the Day")
    print("  7.Exit Agency POV")
    cho=int(input("PLEASE ENTER OPTION NUMBER: "))
    print()
    if(cho==1):
        employee()
    elif(cho==2):
        con=mysql.connector.connect(host="localhost",user='root',passwd='',database='project')
        vehCur=con.cursor()
        vehCur.execute("SELECT * FROM Employee")
        det=vehCur.fetchall()
        if(len(det)==0):
            print("No Employee Details found")
        else:
            for i in det:
                print()
                print("                         Details of Employee No.",i[0],":")
                print()
                print("Employee ID:",i[1])
                print("First Name:",i[2])
                print("Surname:",i[3])
                print("Age:",i[4])
                print("Year of Joining:",i[5])
                print("Position in Office:",i[6])
                print("Number of vehicles sold:",i[14])
                print("Basic Pay:",i[7])
                print("Dearance Allowance:",i[8])
                print("Travel Allowance:",i[9])
                print("House Rent Allowance:",i[10])
                print("PF:",i[11])
                print("Income Tax:",i[12])
                print("Net Salary:",i[13])
    elif(cho==3):
        vehCur.execute("SELECT * FROM Customers")
        det=vehCur.fetchall()
        if(len(det)==0):
            print("No Customer Details found")
        else:
            con=mysql.connector.connect(host="localhost",user='root',passwd='',database='project')
            vehCur=con.cursor()
            for i in det:
                print("DETAILS OF CUSTOMER WITH CUSTOMER ID",i[0])
                print()
                print("Customer Name:",i[1])
                print("Phone Number:",i[2])
                print("Date of Purchase:",i[3])
                print("Vehicle Purchased:",i[4])
                print("Cost of",i[4],":",i[5])
                if(i[6]==0):
                    print("EMI option not selected!")
                else:
                    print("EMI per month:",i[6])
                print("Final Amount:",i[7])
                print()
        print()
       
    elif(cho==4):
        print()
        print("No of Cars sold:",noc)
        print("No of Scooters sold:",nos)
        print("No of Bikes sold:",nob)
        print()
    elif(cho==5):
        print()
        con=mysql.connector.connect(host="localhost",user='root',passwd='',database='project')
        vehCur=con.cursor()
        vehCur.execute("SELECT * FROM Ally_Companies")
        dat=vehCur.fetchall()
        for i in dat:
            print("Company No.",i[0])
            print("  Name:",i[1])
            print("  Number of Cars:",i[2])
            print("  Number of Bikes:",i[4])
            print("  Number of Scooters:",i[3])
            print()
    elif(cho==6):
        print()
        print("Amount Collected:",amnt)
        print("Biggest sale of the day:",bsod)
        print()
    elif(cho==7):
        break
    else:
        print("Wrong input! Please try again!")
    con.close()


#Customer pov              
def Customerpov():
        print("-----------------------------WELCOME TO PHOENIX AUTOMOBILES' SHOWROOM PORTAL-----------------------------")
        print("Enter 1 for Bikes")
        print("Enter 2 for Scooters")
        print("Enter 3 for Cars")
        vehiclechoice=int(input("Enter your choice: "))
 
        Comparison(vehiclechoice)
        print()
        global Vehicle
        global Vc
        global amnt
        global bsod
        
        Vn=Vehicle
        print("TO CHOOSE BANK")
        EMI=EMIfunc(Vc)
        global Bank
        global time
        FA=EMI*time
        amnt+=FA
        if FA>=bsod:
                bsod=FA
        print()
        updateagent()
        print()
        print("ENTER YOUR DETAILS")
        NM=input("Enter the name of Customer:")
        Ph=int(input("Enter the phone number of the Customer:"))
        import mysql.connector
        con=mysql.connector.connect(host="localhost",database='Project',user='root',passwd='') 
        mycur=con.cursor() 
        mycur.execute("select curdate()")
        dt=mycur.fetchone()[0]
        Customers(NM,Ph,dt,Vn,Vc,EMI,FA)
        print()
        print("YOUR ORDER HAS BEEN PLACED")
        print()
 
        print("-----------------------------BILLING------------------------------")
        print("Name                       :",NM)
        print("Vehicle Purchased          :",Vn)
        print("Contact no.                :",Ph)
        print("Date of Purchase           :",dt)
        print("Price of Vehicle           :",Vc)
        print("EMI(amount per month)      :",EMI)
        print("Number of months of payment:",time)
        print("Bank selected              :",Bank)
        print("Total Amount               :",FA)
 
        print()
        print("-----------WE THANK YOU FOR YOUR CORRESPONDENCE WITH US-----------")
        con.close()

#DRIVER PROGRAM
while True:
    print("\t\t\t\t\t\t\t\t\t WELCOME TO PHOENIX AUTOMOBILES")
    print()
    print()
    print("Portals Available:")
    print("  1. Company Portal")
    print("  2. Showroom Portal")
    print("  3. EXIT")
    print()
    op=int(input("Please enter the Portal you want to access: "))
    print()
    print()
    if(op==1):
        agency_pov()
    elif(op==2):
        Customerpov()
    else:
        break

