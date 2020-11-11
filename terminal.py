import os, platform, readline

if(platform.system() == "Linux"):
    import getpass
    if(os.getgid == 0): usr = "root"
    elif(os.getgid != 0): usr = "other"
    cwd = os.getcwd()
    if(cwd[0:len(getpass.getuser())+6] == ("/home/"+getpass.getuser())): cwd = "~"+cwd[len(getpass.getuser())+6:]
    device = open("/etc/hostname", "r").read()[0:-1]

    while(True):
        if(usr == "root"):
            print("\x1b[38;2;170;170;170m"+getpass.getuser()+"@"+device+":"+cwd+" # \r", end="")
            cmd = input("\x00"*len(getpass.getuser()+"@"+device+":"+cwd+" # "))
        elif(usr == "other"):
            print("\x1b[38;2;10;255;10m"+getpass.getuser()+"@"+device+"\x1b[38;2;170;170;170m:\x1b[38;2;10;10;255m"+cwd+" \x1b[38;2;170;170;170m$ ", end="")
            cmd = input("\x00"*len(getpass.getuser()+"@"+device+":"+cwd+" $ "))

        if(cmd):
            print("py-terminal: \""+cmd+"\" Unknown Command")
