import os, getpass

if(os.getgid == 0): usr = "root"
elif(os.getgid != 0): usr = "other"
cwd = os.getcwd()
if(cwd[0:len(getpass.getuser())+6] == ("/home/"+getpass.getuser())): cwd = "~"+cwd[len(getpass.getuser())+6:]
device = open("/etc/hostname", "r").read()[0:-1]

while(True):
    if(usr == "root"): cmd = input("\x1b[38;2;170;170;170mroot@"+device+":"+cwd+" # ")
    elif(usr == "other"): cmd = input("\x1b[38;2;10;255;10m"+getpass.getuser()+"@"+device+"\x1b[38;2;170;170;170m:\x1b[38;2;10;10;255m"+cwd+" \x1b[38;2;170;170;170m$ ")
    
    if(cmd):
        print("py-terminal: Unknown Command")
