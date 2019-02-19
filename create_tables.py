import pymysql

db=pymysql.connect("localhost","root","Shivam@1604","drive")
"""
db = pymysql.connect(
	host="localhost",
	user="root",
	password="Shivam@1604"
)
"""
cur=db.cursor()

sql='''CREATE TABLE user(
	username VARCHAR(255),
	password VARCHAR(255),
	ip VARCHAR(255),
	PRIMARY KEY(username))
'''
#cur.execute("CREATE DATABASE drive")

cur.execute(sql)
cur.execute("SHOW TABLES")
rows=cur.fetchall()
for eachRow in rows:
	print (eachRow)
#print(db)
