#!/usr/bin/python36
print("content-type:text/html\n")

import subprocess as sp
import cgi,cgitb
cgitb.enable()

print('''
<html>
<head>
        <title>Print Project</title>
        <style type="text/css">
                strong
                {
                        font-size: 20px;
                }
                .field
                {
                        float: right;
                        padding: 5px !important;
                        width: 330px;
                        border-radius: 3px !important;
                }
                #logical_form, #login_form, #signup_form
                {
                        border: 1px solid red;
                        padding: 25px;
                        padding-bottom: 10px;
                        width:550px;
                }
                #see_storage, #get_storage, #signup
                {
                        position: absolute;
                        top: 10%;
                        left: 50%;
                        margin-left: -100px;
                }
                #submit
                {
                        position: relative;
                        left: 50%;
                        padding: 8px;
                        font-size: 14px;
                        margin-left: -40px;
                        border-radius: 5px;
                }

                #home
                {
                        text-align:center;
                        position: absolute;
                        top: 26%;
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
                <button class="tablinks" id="default" onclick="doit(event, 'home')">Home</button>
			
                <!--button class="tablinks" onclick="doit(event, 'get_storage')">Get Storage</button-->
                <button class="tablinks" onclick="doit(event, 'signup')">Sign Up</button>
                <button class="tablinks" onclick="doit(event, 'see_storage')">Login</button>
        </div>


        <br>
        <div id="home" class="tabcontent">
                <h1>Welcome</h1>
                <h1>to</h1>
                <h1>Switcher Cloud Providers</h1>
        </div>
        <!--<div id="get_storage" class="tabcontent">
                <h1 style="text-align:center;"><u>Switcher Cloud Providers</u></h1><br>
                <div id="logical_form">
                        <form action="../cgi-bin/drive/logical.py" method="post">
                                <strong>Your IP Address:</strong>
                                <input type="text" name="ip" class="field" placeholder="Enter Your IP">
                                <br><br><br>
                                <strong>Folder Name:</strong>
                                <input type="text" name="name" class="field" placeholder="Enter Folder Name">
                                <br><br><br>
                                <strong>Storage Size:</strong>
                                <input type="text" name="size" class="field" placeholder="Enter Size">
                                <br><br><br>
                                <input type="submit" name="submit" id="submit" value="Get Storage">
                        </form>
                </div>
        </div>-->
        <div id="see_storage" class="tabcontent">
                <h1 style="text-align:center;"><u>Login</u></h1><br>
                <div id="login_form">
                        <form action="login.py" method="post">
                                <strong>User:</strong>
                                <input type="text" name="user" class="field" placeholder="Enter Username">
                                <br><br><br>
                                <strong>Password:</strong>
                                <input type="text" name="password" class="field" placeholder="Enter Password">
                                <br><br><br>
                                <input type="submit" name="submit" id="submit" value="See Storage">
                        </form>
                </div>
        </div>
        <div id="signup" class="tabcontent">
                <h1 style="text-align:center;"><u>Sign Up</u></h1><br>
                <div id="signup_form">
                        <form action="signup.py" method="post">
                                <strong>User:</strong>
                                <input type="text" name="user" class="field" placeholder="Enter Username">
                                <br><br><br>
                                <strong>Password:</strong>
                                <input type="text" name="password" class="field" placeholder="Enter Password">
                                <br><br><br>
                                <strong>Your IP:</strong>
                                <input type="text" name="ip" class="field" placeholder="Enter Your IP">
                                <br><br><br>
                                <strong>Size:</strong>
                                <input type="text" name="size" class="field" placeholder="Enter Size in GB">
                                <br><br><br>
                                <input type="submit" name="submit" id="submit" value="Sign Up">
                        </form>
                </div>
        </div>
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
