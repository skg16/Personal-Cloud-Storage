#!/usr/bin/python36

import sys
import subprocess as sp
import os
import cgi
import cgitb
cgitb.enable()

file=cgi.FieldStorage()
fname=file.getvalue('name')
fdrive=file.getvalue('drive')

#print("content-type:text/html\r\n\r\n")
#print(fname)
#print(fdrive)

print("Content-Type:application/octet-stream;")
print("Content-Disposition: attachment; filename="+fname+";")
print("Content-Transfer-Encoding: binary;")
print()

loc=fdrive+'/'+fname
#print(loc)
fo = open('/logical_mount/'+loc, 'rb')
str=fo.read()
sys.stdout.flush()
sys.stdout.buffer.write(str)
#print(str)
fo.close()
