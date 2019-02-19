#!/usr/bin/python36

import subprocess as sp
import os
import cgi
import cgitb
cgitb.enable()

form=cgi.FieldStorage()
fileitem=form['userfile']
#name=form.getvalue('user')


user_id=""
if 'HTTP_COOKIE' in os.environ:
        cookies=os.environ['HTTP_COOKIE']
        cookies=cookies.split('; ')
        for cookie in cookies:
                cookie=cookie.split("=")
                #print(cookie[0]+" "+cookie[1])
                if cookie[0] == "username":
                        user_id = cookie[1]



print("content-type:text/html\r\n\r\n")


#print(user_id)
#print(fileitem)

if fileitem.filename:
	out =os.path.basename(fileitem.filename)
	loc=user_id+'/'+out
	#print(loc)
	sp.getoutput("sudo touch /logical_mount/{0}".format(loc))
	sp.getoutput("sudo chmod -R 777 /logical_mount/{0}".format(loc))
	f=open('/logical_mount/' + loc, 'wb')
	f.write(fileitem.file.read())
	
	message='The file "' + out + '" was successfully uploaded.'
else:
        message="No file was uploaded"

print(message)

print('''
        <html>
        <body onload="document.location='files.py'"> </body>
        </html>
        ''')


