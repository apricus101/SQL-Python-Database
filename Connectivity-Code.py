gen=input("Enter gender(either M/F):")
dob=input("Enter Date of Birth:")
age=int(input("Enter age:"))
nof=input("Enter name of father:")
oof=input("Enter occupation of father:")
fcn=int(input("Enter father's contact number:"))
nom=input("Enter name of mother:")
oom=input("Enter occupation of mother:")
mcn=int(input("Enter mother's contact number:"))
nog=input("Enter name of guardian(if any):")
ph=int(input("Enter contact number of guardian(if any):"))
oc=input("Are you the only child?(YES/NO):")
qry="INSERT INTO REGISTRATION_DETAILS
VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(rno,na
me,cl,gen,dob,age,nof,oof,fcn,nom,oom,mcn,nog,ph,oc)
cur.execute(qry)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
===============================================================
=")
#to delete records
def delete():
print("Do you want to- 1.Delete by Name or 2.Delete by Reg.No?")
c=int(input("Enter your choice '1' for Name and '2' for Reg.No:"))
if c==1:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter name of student:")
qry="DELETE FROM REGISTRATION_DETAILS WHERE
NAME='{}'".format(name)
cur.execute(qry)
print()
print("Record deleted successfully!!!")
print("=========================================================
============================================================")
obj.commit()
cur.close()
obj.close()
elif c==2:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
r=int(input("Enter Reg.No.:"))
qry="DELETE FROM REGISTRATION_DETAILS WHERE
REGNO='{}'".format(r)
cur.execute(qry)
print()
print("Record deleted successfully!!!")
print("=========================================================
============================================================")
obj.commit()
cur.close()
obj.close()
else:
print("Option invalid!!!")
#to display records
def displayrec():
print("Do you want to- 1.Search by Name or 2.Search by Reg.No?")
print()
c=int(input("Enter your choice'1' for Name and '2' for Reg.No:"))
if c==1:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter name of student:")
qry="SELECT *FROM REGISTRATION_DETAILS WHERE
NAME='{}'".format(name)
cur.execute(qry)
a=cur.fetchall()
for x in a:
print(x)
obj.commit()
cur.close()
obj.close()
print("=========================================================
========================================================")
elif c==2:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
r=int(input("Enter Reg.No.:"))
qry="SELECT * FROM REGISTRATION_DETAILS WHERE
REGNO='{}'".format(r)
cur.execute(qry)
a=cur.fetchall()
for x in a:
print(x)
print("=========================================================
========================================================")
obj.commit()
cur.close()
obj.close()
else:
print("Option invalid!!!")
print("=========================================================
========================================================"
#feedback form
def feedback():
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
qry="create table feedback(PREVIOUS_BOARD
char(10),REVIEW_OF_PREVIOUS_SCHOOL char(200),WHY_THIS_SCHOOL
char(200),PREVIOUS_PERCENTAGE char(10))"
cur.execute(qry)
cur.close()
obj.close()
#to insert records into feedback table
def insertfeedback():
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
b=input("Enter previous board:")
c=input("Enter feedback of your previous school:")
print("Why this school?")
n=input("Enter your views:")
m=float(input("Specify your previous class %:"))
qy="insert into feedback values('{}','{}','{}','{}')".format(b,c,n,m)
cur.execute(qy)
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
===================================")
obj.commit()
cur.close()
obj.close()
def disfeed():
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
cur.execute("select *from feedback")
a=cur.fetchall()
print("PREVIOUS BOARD","REVIEW OF OLD SCHOOL","WHY THIS
SCHOOL?","PREVIOUS PERCENTAGE")
for x in a:
print(x)
#Fees structure
def fees():
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
cur.execute("create table fees_structure(TUTION_FEES float, EXAM_FEES
float, LAB_FEES float, CO_CURRICULAR_FEES float, GROUND_FEES float,
TRANSPORT_FEES float)")
cur.close()
obj.close()
#to insert records in fees table
def insertfees():
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
cla=input("Enter class:")
tf=float(input("Enter tution fees:"))
ef=float(input("Enter exam fees:"))
lf=float(input("Enter lab fees:"))
ccf=float(input("Enter co-curricular fees:"))
gf=float(input("Enter ground fees:"))
tf=float(input("Enter transport fees:"))
qry="INSERT INTO fees_structure
VALUES('{}','{}','{}','{}','{}','{}','{}')".format(cla,tf,ef,lf,ccf,gf,tf)
cur.execute(qry)
print("LATE_FEE=Rs25")
obj.commit()
cur.close()
obj.close()
print("RECORD INSERTED SUCCESSFULLY!!!")
#to display fees structure
def disfees():
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
cur.execute("select *from feedback")
a=cur.fetchall()
print("CLASS","TUTION FEES","EXAM FEES","LAB FEES","CO-
CURRICULAR FEES","GROUND FEES","TRANSPORT FEES")
for x in a:
print(x)
#Mark Sheet
#creation of table for different subject combinations
def markstables():
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
qry1=("create table marks1(NAME char(20),CLASS char(8),English float, Hindi
float, Maths float, Science float, Marathi float, SST float)")
cur.execute(qry1)
qry2="create table marks2(NAME char(20),CLASS char(8),English float, Hindi
float, Maths float, Science float, Sanskrit float, SST float)"
cur.execute(qry2)
qry3=("create table marks3(NAME char(20),CLASS char(8),English float, Maths
float, EVS float)")
cur.execute(qry3)
cur.execute("create table marks4(NAME char(20),CLASS char(8),English float,
Maths float, Science float, Marathi float, SST float)")
cur.execute("create table marks5(NAME char(20),CLASS char(8),English float,
Hindi float, Maths float, Science float, Sanskrit float, SST float)")
cur.execute("create table marks6(NAME char(20),CLASS char(8),English float,
Maths float, Science float, Hindi float, SST float)")
cur.execute("create table marks7(NAME char(20),CLASS char(8),Physics float,
Chemistry float, Maths float, Computer_Science float, English float)")
cur.execute("create table marks8(NAME char(20),CLASS char(8),Physics float,
Chemistry float, Maths float, Physical_Education float, English float)")
cur.execute("create table marks9(NAME char(20),CLASS char(8),Physics float,
Chemistry float, Biology float, Physical_Education float, English float)")
cur.execute("create table marks10(NAME char(20),CLASS
char(8),Business_Studies float, Accounts float, Economics float, Maths float, English
float)")
cur.execute("create table marks11(NAME char(20),CLASS
char(8),Business_Studies float, Accounts float, Economics float, Physical_Education
float, English float)")
cur.execute("create table marks 12(NAME char(20),CLASS char(8),Physics float,
Chemistry float, Maths float, Biology float, English float)")
cur.close()
obj.close()
def report():
menu=int(input("Enter your class:"))
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter you name:")
cla=input("Enter your class:")
eng=float(input("Enter marks for English:"))
hin=float(input("Enter marks for Hindi:"))
mat=float(input("Enter marks for Maths:"))
sci=float(input("Enter marks for Science:"))
san=float(input("Enter marks for Sanskrit:"))
sst=float(input("Enter marks for SST:"))
qy="insert into marks2
values('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,cla,eng,hin,mat,sci,san,sst)
cur.execute(qy)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
======================================================")
else:
print("No such option available")
#for students grade
elif menu<5:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter you name:")
cla=input("Enter your class:")
eng=float(input("Enter marks for English:"))
mat=float(input("Enter marks for Maths:"))
evs=float(input("Enter marks for EVS:"))
qy="insert into marks3
values('{}','{}','{}','{}','{}')".format(name,cla,eng,mat,evs)
cur.execute(qy)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
======================================================")
#for students of 9th and 10th
if menu in range(9,11):
print("The optional subject is Marathi/Sanskrit/Hindi")
choice=input("Enter your choice:")
if choice=="Marathi" or choice=="1":
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter you name:")
cla=input("Enter your class:")
eng=float(input("Enter marks for English:"))
mat=float(input("Enter marks for Maths:"))
sci=float(input("Enter marks for Science:"))
Mar=float(input("Enter marks for Marathi:"))
sst=float(input("Enter marks for SST:"))
qy="insert into marks4
values('{}','{}','{}','{}','{}','{}','{}')".format(name,cla,eng,mat,sci,Mar,sst)
cur.execute(qy)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
======================================================
if choice=="Sanskrit" or choice=="2":
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter you name:")
cla=input("Enter your class:")
eng=float(input("Enter marks for English:"))
mat=float(input("Enter marks for Maths:"))
sci=float(input("Enter marks for Science:"))
san=float(input("Enter marks for Sanskrit:"))
sst=float(input("Enter marks for SST:"))
qy="insert into marks5
values('{}','{}','{}','{}','{}','{}','{}')".format(name,cla,eng,mat,sci,san,sst)
cur.execute(qy)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
======================================================")
if choice=="Hindi" or choice=="3":
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter you name:")
cla=input("Enter your class:")
eng=float(input("Enter marks for English:"))
mat=float(input("Enter marks for Maths:"))
sci=float(input("Enter marks for Science:"))
hin=float(input("Enter marks for Sanskrit:"))
sst=float(input("Enter marks for SST:"))
qy="insert into marks6
values('{}','{}','{}','{}','{}','{}','{}')".format(name,cla,eng,mat,sci,hin,sst)
cur.execute(qy)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
======================================================")
#for students of class 11th or 12th
if menu==11 or menu==12:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
print("Which stream have you enrolled in?")
print("1.Science")
print("2.Commerce")
stream=input("Enter your stream:")
#for science
if stream=="Science" or stream=="science" or stream=="1":
print("What is your optional subject?")
print("1.Maths")
print("2.Biology")
print("3.Both Maths and Biology")
choice=input("Enter your optional subject:")
#for maths
if choice=="1":
print("What is your second optional subject?")
print("1.Computer Science")
print("2.Physical Education")
ch=input("Enter your second optional subject:")
#for maths with computer science
if ch=="1":
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter you name:")
cla=input("Enter your class:")
eng=float(input("Enter marks for English:"))
mat=float(input("Enter marks for Maths:"))
phy=float(input("Enter marks for Physics:"))
chem=float(input("Enter marks for Chemistry:"))
cs=float(input("Enter marks for CS:"))
qy="insert into marks7
values('{}','{}','{}','{}','{}','{}','{}')".format(name,cla,phy,chem,mat,cs,eng)
cur.execute(qy)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!"
print("=========================================================
=========================================")
#for maths with physical education
elif ch=="2":
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter you name:")
cla=input("Enter your class:")
eng=float(input("Enter marks for English:"))
mat=float(input("Enter marks for Maths:"))
phy=float(input("Enter marks for Physics:"))
chem=float(input("Enter marks for Chemistry:"))
pe=float(input("Enter marks for PE:"))
qy="insert into marks8
values('{}','{}','{}','{}','{}','{}','{}')".format(name,cla,phy,chem,mat,pe,eng)
cur.execute(qy)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
===========================================")
#for biology
if choice=="2":
print("What is your second optional subject?")
print("1.Physical Education")
ch=input("Enter your second optional subject:")
#for biology with physical education
if ch=="1":
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter you name:")
cla=input("Enter your class:")
eng=float(input("Enter marks for English:"))
bio=float(input("Enter marks for Biology:"))
phy=float(input("Enter marks for Physics:"))
chem=float(input("Enter marks for Chemistry:"))
pe=float(input("Enter marks for PE:"))
qy="insert into marks9
values('{}','{}','{}','{}','{}','{}','{}')".format(name,cla,phy,chem,bio,pe,eng)
cur.execute(qy)
obj.commit()
cur.close
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
=========================================")
# for maths with biology
if choice=="3":
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter you name:")
cla=input("Enter your class:")
eng=float(input("Enter marks for English:"))
bio=float(input("Enter marks for Biology:"))
phy=float(input("Enter marks for Physics:"))
chem=float(input("Enter marks for Chemistry:"))
mat=float(input("Enter marks for Maths:"))
qy="insert into marks12
values('{}','{}','{}','{}','{}','{}','{}')".format(name,cla,phy,chem,mat,bio,eng)
cur.execute(qy)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
=============================================")
#for commerce
if stream=="Commerce" or stream=="2":
  obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter you name:")
cla=input("Enter your class:")
bst=float(input("Enter marks for Business Studies:"))
acc=float(input("Enter marks for Accounts:"))
eco=float(input("Enter marks for Economics:"))
pe=float(input("Enter marks for PE:"))
eng=float(input("Enter marks for English:"))
qy="insert into marks11
values('{}','{}','{}','{}','{}','{}','{}')".format(name,cla,bst,acc,eco,mat,eng)
cur.execute(qy)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
================================================")
#staff details
def stde():
#create table stde
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
qry="create table STAFF_DETAILS(REGNO INT PRIMARY KEY,NAME
char(30),GENDER char(10),AGE int,SUBJECT char(20),QUALIFICATIONS
char(25))"
cur.execute(qry)
cur.close()
obj.close()
#insert new record
def innr():
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
regno=int(input("Enter registration number:"))
name=input("Enter Name:")
gender=input("Enter gender(M/F):")
age=int(input("Enter age:"))
subject=input("Enter subject:")
qual=input("Enter your qualifications:")
qry="insert into STAFF_DETAILS
VALUES('{}','{}','{}','{}','{}','{}')".format(regno,name,gender,age,subject,qual)
cur.execute(qry)
obj.commit()
cur.close()
obj.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
===============================================================
=")
#search record
def sr():
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
print("How do you wanna search???")
print("1.Search by name")
print("2.Search by reg.no")
print("3. Display all records")
ch=int(input("Enter your choice:"))
if ch==1:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter name:")
qry="select *from STAFF_DETAILS where NAME='{}'".format(name)
cur.execute(qry)
a=cur.fetchall()
for x in a:
print(x)
print()
print("=========================================================
============================================================")
obj.commit()
cur.close()
obj.close()
if ch==2:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
r=int(input("Enter reg.no:"))
qry="select *from STAFF_DETAILS where REGNO='{}'".format(r)
cur.execute(qry)
a=cur.fetchall()
for x in a:
print(x)
print()
print("=========================================================
============================================================")
obj.commit()
cur.close()
obj.close()
if ch==3:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
qry="select *from STAFF_DETAILS"
cur.execute(qry)
print("REGNO","NAME","GENDER","AGE","SUBJECT","QUALIFICATION
")
a=cur.fetchall()
for x in a:
print(x)
print()
print("=========================================================
============================================================")
def delerec():
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
print("1.Delete by name")
print("2.Delete by reg.no")
print()
ch=int(input("Enter your choice:"))
if ch==1:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
name=input("Enter name:")
qry="delete from STAFF_DETAILS where NAME='{}'".format(name)
cur.execute(qry)
print()
print("RECORD DELETED SUCCESSFULLY!!!")
print()
print("=========================================================
============================================================")
obj.commit()
cur.close()
obj.close()
if ch==2:
import mysql.connector as con
obj=con.connect(host="localhost",user="root",password="tiger",database="SMPp
roject")
cur=obj.cursor()
r=int(input("Enter reg.no:"))
qry="delete from STAFF_DETAILS where REGNO='{}'".format(r)
cur.execute(qry)
print()
print("RECORD DELETED SUCCESSFULLY!!!")
print()
print("=========================================================
============================================================")
obj.commit()
cur.close()
obj.close()
#creating table for transfer certificate
##REMEMBER##
#Function to be called only ONCE
def createtabletc():
import mysql.connector as mc
from datetime import date
cnx=mc.connect(user='root',password='tiger',host='localhost',database='SMPproje
ct')
cur=cnx.cursor()
ct="Create table Transfer_Certificate(SNo int PRIMARY KEY,Students_Name
char(30),Grade char(5),Section char(5),Date_of_birth char(10),Month_of_leaving
char(10),Year_of_leaving char(10),Library_dues char(10),Attendance char(5),
Reason_for_leaving char(30),Place_of_transfer char(15),Father_Name
char(30),Contact_Number1 int,Mother_Name char(30),Contact_Number2 int)"
cur.execute(ct)
cur.close()
cnx.close()
#To insert record into table tc of students leaving
def insertintotc():
import mysql.connector as mc
from mysql.connector import errorcode
cnx=mc.connect(user='root',password='tiger',host='localhost',database='SMPproje
ct')
cur=cnx.cursor()
sno=int(input("Enter S.No:"))
name=input("Enter student's name:")
grade=input("Enter grade:")
sec=input("Enter section:")
dob=input("Enter Date of Birth:")
mol=input("Enter month of leaving:")
yol=input("Enter year of leaving:")
libdues=input("Enter library dues(if remaining):")
Attendence=input("Enter attendace percentage of last session:")
rof=input("State reason for leaving(in brief):")
pot=input("Enter place of transfer:")
fn=input("Enter father's name:")
fcn=float(input("Enter father's contact number:"))
mn=input("Enter mother's name:")
mcn=float(input("Enter mother's contact number:"))
qry="INSERT INTO Transfer_Certificate
VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,na
me,grade,sec,dob,mol,yol,libdues,Attendence,rof,pot,fn,fcn,mn,mcn)
cur.execute(qry)
cnx.commit()
cur.close()
cnx.close()
print()
print("RECORD INSERTED SUCCESSFULLY!!!")
print("=========================================================
===============================================================
=")
#for displaying tc records
def distc():
import mysql.connector as mc
from mysql.connector import errorcode
cnx=mc.connect(user='root',password='tiger',host='localhost',database='SMPproje
ct')
cur=cnx.cursor()
qry=("select *from Transfer_Certificate")
cur.execute(qry)
data=cur.fetchall()
print("The records are as follows:")
print("SNO","NAME","GRADE","SECTION","DOB","MONTH OF
LEAVING","YEAR OF
LEAVING","LIB_DUES","ATTENDENCE","REASON","PLACE OF
TRANSFER","FATHER NAME","FATHER CONTACT","MOTHER
NAME","MOTHER CONTACT")
print()
for row in data:
print(row)

#main program
while True:
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::")
print("Select desired function to implement")
print()
print("1.To fill up student registration form.")
print("2.Delete student record")
print("3.Display student record")
print("4.Feedback")
print("5.To display all feedbacks")
print("6.To update Fees structure")
print("7.To display fees structure")
print("8.Report")
print("9.To fill up staff's registration form")
print("10.To search staff's record")
print("11.To delete staff record")
print("12.To issue transfer certificate")
print("13.To display transfer certificate records")
print("Press any other key to exit")
print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::")
print()
ch=int(input("Enter your choice:"))
print()
print("=========================================================
===============================================================
")
if ch==1:
insertingrec()
elif ch==2:
delete()
elif ch==3:
displayrec()
elif ch==4:
insertfeedback()
elif ch==5:
disfeed()
elif ch==6:
insertfees()
elif ch==7:
disfees()
elif ch==8:
report()
elif ch==9:
innr()
elif ch==10:
sr()
elif ch==11:
delerec()
elif ch==12:
insertintotc()
elif ch==13:
distc()
else:
break
