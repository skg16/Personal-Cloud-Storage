#!/usr/bin/python36

"""
print("Set-Cookie:Username = chandan;")
print("content-type:text/html")
print("")
"""

import subprocess as sp
import cgi,cgitb,pymysql
cgitb.enable()

form=cgi.FieldStorage()
user=form.getvalue('user')
password=form.getvalue('password')
print("Set-Cookie:username = "+user+";")
print("content-type:text/html")
print("")


#match pass and username


flag=0
db=pymysql.connect("localhost","root","Shivam@1604","drive")
cur=db.cursor()
cur.execute("SELECT * FROM user")
rows=cur.fetchall()
for eachRow in rows:
	if eachRow[0]==user and eachRow[1]==password:
		flag=1
db.close()


#if user=="chandan" and password=="Chandan@123":


if flag==1:
	print("Successfully Login!")
	print('''
	<html>
	<body onload="document.location='files.py'"> </body>
	</html>	
	''')
else:
	print("Unsuccessful login attempt")
	print('''
        <html>
        <body onload="document.location='login.py'"> </body>
        </html>
        ''')
