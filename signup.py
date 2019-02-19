#!/usr/bin/python36

import subprocess as sp
import os,pymysql
import cgi
import cgitb
cgitb.enable()

form=cgi.FieldStorage()
name=form.getvalue('user')
size=form.getvalue('size')
ip=form.getvalue('ip')
password=form.getvalue('password')



#sending data into table.

db=pymysql.connect("localhost","root","Shivam@1604","drive")
cur=db.cursor()


sql='INSERT INTO user VALUES ("{0}","{1}","{2}")'.format(name,password,ip)
cur.execute(sql)
db.commit()

"""
cur.execute("SELECT * FROM user")

rows=cur.fetchall()
for eachRow in rows:
        print (eachRow)
"""

db.close()





print("content-type:text/html\r\n\r\n")

sp.getoutput("sudo lvcreate storage_sea --size +{0}G --name {1}".format(int(size),name))
sp.getoutput("sudo mkfs.ext4 /dev/storage_sea/{0}".format(name))
sp.getoutput("sudo mkdir /logical_mount/{0}".format(name))
sp.getoutput("sudo chmod -R 777 /logical_mount/{0}".format(name))

a=sp.getstatusoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.200 mount /dev/storage_sea/{0} /logical_mount/{1}".format(name,name))
if a[0]==0:
	print("Storage allocated successfully. Please login to use the storage")
	print("<html><body><a href='logical_html.py'>Login</a></body></html>")
	#print("<html>")
      	#print("<body onload="+"document.location='login.py?user=%s&password=%s'"+"> </body>" % (name,password))
        #print("</html>")
else:
	print("Something went wrong")
	print(a)
