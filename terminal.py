import os, getpass

if(os.getgid == 0): usr = "root"
elif(os.getgid != 0): usr = "other"

while(True):
    if(usr == "root"): cmd = input("root@device:~ # ")
    elif(usr == "other"): cmd = input(getpass.getuser() + "@device:~ $ ")
    
    if(cmd):
        print("py-terminal: Unknown Command")
