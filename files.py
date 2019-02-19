#!/usr/bin/python36
print("content-type:text/html\n")

import subprocess as sp
import cgi,cgitb
from os import environ
cgitb.enable()

print('''
<html>
<head>
	<title>Print Project</title>
	<style type="text/css">
		strong
		{
			font-size: 20px;
			padding-left: 10px;
			float: left;
		}
		.field
		{
			float: right;
			padding: 5px !important;
			width: 330px;
			border-radius: 3px !important;
		}
		#logical_form, #login_form
		{
			border: 1px solid red;
			padding: 25px;
			padding-bottom: 10px;
			width:500px; 
		}
		#submit
		{
			padding: 8px; 
			font-size: 14px;
			margin-left: -40px;
			width: 100px;
			border-radius: 5px;
		}

		#upload_file
		{
			text-align:center; 
			position: absolute; 
			top: 15%; 
			left: 40%;
			font-size: 25px;
		}


		* 
		{
			box-sizing: border-box
		}

		/* Style the tab */
		.tab {
		  float: left;
		  border: 1px solid #ccc;
		  background-color: #f1f1f1;
		  width: 20%;
		  height: 100%;
		}

		/* Style the buttons that are used to open the tab content */
		.tab button {
		  display: block;
		  background-color: inherit;
		  color: black;
		  padding: 22px 16px;
		  width: 100%;
		  border: none;
		  outline: none;
		  text-align: left;
		  font-size: 20px;
		  cursor: pointer;
		  transition: 0.3s;
		}

		/* Change background color of buttons on hover */
		.tab button:hover {
		  background-color: #ddd;
		}

		/* Create an active/current "tab button" class */
		.tab button.active {
		  background-color: #ccc;
		}

	</style>
</head>
<body>


	<div class="tab">
	  <button class="tablinks" id="default" onclick="doit(event, 'files')">Files</button>
	  <button class="tablinks" onclick="doit(event, 'upload_file')">Upload File</button>
	  <button class="tablinks" onclick="doit(event, 'new_folder')">New Folder</button>
	</div>


	<br>
	<div id="files" class="tabcontent">
'''
)


#write codes for listing the folder files.


user_id=""
if 'HTTP_COOKIE' in environ:
	cookies=environ['HTTP_COOKIE']
	cookies=cookies.split('; ')
	for cookie in cookies:
		cookie=cookie.split("=")
		#print(cookie[0]+" "+cookie[1])
		if cookie[0] == "username":
			user_id = cookie[1]


print("User->"+user_id)


a=sp.getstatusoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.200 mount /dev/storage_sea/{0} /logical_mount/{1}".format(user_id,user_id))

pp=sp.getoutput("sudo ls -1 /logical_mount/{0}".format(user_id))
#print(pp)

i=pp.split('\n')
temp="lost+found"

print("<html>")
print("<body>")
for str in i:
	if str!=temp:
        	print("<h3><a href='down.py?drive=%s&name=%s'>%s</a></h3>" % (user_id,str,str))
print("</body>")
print("</html>")


print('''
	</div>
	<div id="upload_file" class="tabcontent">
		<h1 style="text-align:center;"><u>Upload File</u></h1><br>
		<div id="logical_form">
			<form enctype="multipart/form-data" method="post" action="upload_file.py">
				<strong>Select File:</strong>
				<input type="file" name="userfile">
				<br><br><br>
				<!--<strong>Select User:</strong>
                                <input type="text" name="user">
                                <br><br><br>-->
				<input type="submit" align="center" name="submit" id="submit" value="Upload">
			</form>
		</div>
	</div>
	<!-- <div id="see_storage" class="tabcontent">
		<h1 style="text-align:center;"><u>Login</u></h1><br>
		<div id="login_form">
			<form action="cgi-bin/login.py">
				<strong>User:</strong>
				<input type="text" name="name" class="field" placeholder="Enter Username">
				<br><br><br>
				<strong>Password:</strong>
				<input type="password" name="size" class="field" placeholder="Enter Password">
				<br><br><br>
				<input type="submit" name="submit" id="submit" value="See Storage">
			</form>
		</div>
	</div> -->
</body>
<script type="text/javascript">
	function doit(evt, cityName) {
		  var i, tabcontent, tablinks;
		  tabcontent = document.getElementsByClassName("tabcontent");
		  for (i = 0; i < tabcontent.length; i++) {
		    tabcontent[i].style.display = "none";
		  }
		  tablinks = document.getElementsByClassName("tablinks");
		  for (i = 0; i < tablinks.length; i++) {
		    tablinks[i].className = tablinks[i].className.replace(" active", "");
		  }
		  document.getElementById(cityName).style.display = "block";
		  evt.currentTarget.className += " active";
	}
	document.getElementById("default").click();
</script>
</html>
'''
)
