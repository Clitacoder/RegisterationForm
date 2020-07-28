from tkinter import *
import pymysql
root=Tk()
root.title=("Registration form")

Fullname=StringVar()
email=StringVar()
gen=StringVar()
#con=StringVar()
sub=StringVar()
db=pymysql.connect("localhost","root","","form")
def database():
	name1=Fullname.get()
	email_id=email.get()
	gender=gen.get()
	#country=con.get()
	subject=sub.get()
	cursor=db.cursor()
	cursor.execute("Create table if not exists REGISTRATION_FORM(\
					Fullname varchar(100) unique NOT NULL,\
					Email varchar(50) NOT NULL,\
					Gender varchar(10) NOT NULL,\
					Country varchar (50) NOT NULL,\
					Subject varchar(20) NOT NULL)")
	cursor.execute("INSERT INTO REGISTRATION_FORM VALUES(\
					'%s','%s',gender,country,subject)"%(name1,email))
	db.commit()
	
label_0=Label(root,text="Registration form", width=20, font=('bold', 15))
label_0.grid(row=1, column=2)

label_1=Label(root, text="Full Name", width=20, font=('bold', 10))
label_1.grid(row=2, column=1)
e1= Entry(root,textvar=Fullname)
e1.grid(row=2,column=2)

label_2=Label(root, text="Email id", width=20, font=('bold', 10))
label_2.grid(row=3, column=1)
e2= Entry(root,textvar=email)
e2.grid(row=3,column=2)

label_3=Label(root, text="Gender", width=20, font=('bold', 10))
label_3.grid(row=4, column=1)
Radiobutton(root, text="Male", padx=5, value=1).grid(row=4, column=2, sticky=W, pady=2)
Radiobutton(root, text="Female", padx=5, value=2).grid(row=5, column=2, sticky=W, pady=2)

"""label_4=Label(root, text="Country", width=20, font=('bold', 10))
label_4.grid(row=5, column=1)

list1=['Canada','India','America','Europe','UK','Pakistan','Italy','Australia','Thailand'];
 
droplist=OptionMenu(root,c,*list)
droplist.config(width=15)
c.set('Select your country')
droplist.grid(row=5,column=2)"""

label_5=Label(root, text="Subject", width=20, font=('bold', 10))
label_5.grid(row=6, column=1)
var2=IntVar()
Checkbutton(root, text="Java").grid(row=6,column=2)
Checkbutton(root, text="Python").grid(row=7,column=2)
Checkbutton(root, text="C++").grid(row=8,column=2)
Button(root, text="Submit", width=20, bg='brown', fg='white', command=database).grid(row=10, column=2)
root.mainloop()
