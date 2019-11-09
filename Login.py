import time
import datetime
import sys
import socket
import os
import pathlib
import errno
os.system('cls')
os.system('cls')
## Error Handler ##
currentDT = datetime.datetime.now()



print("")
print("\033[1;36;40m         :::        ::::::::   :::::::: ::::::::::: ::::    :::\033")
print("\033[1;36;40m        :+:       :+:    :+: :+:    :+:    :+:     :+:+:   :+:\033")  
print("\033[1;36;40m       +:+       +:+    +:+ +:+           +:+     :+:+:+  +:+\033")  
print("\033[1;36;40m      +#+       +#+    +:+ :#:           +#+     +#+ +:+ +#+\033")    
print("\033[1;36;40m     +#+       +#+    +#+ +#+   +#+#    +#+     +#+  +#+#+#\033")     
print("\033[1;36;40m    #+#       #+#    #+# #+#    #+#    #+#     #+#   #+#+#\033")      
print("\033[1;36;40m   ########## ########   ######## ########### ###    ####\033")       
print("\033[1;36;40m                        by ClamLq ")               
print("\033[1;36;40m                       \033")
print("")
  
welcome = input("_\033[1;36;40mDo you have an acount? \033[1;32;40my\033\033[1;36;40m/\033\033[1;36;40m\033[1;31;40mn\033\033[1;36;40m:\033\033[1;35;40m ")

    
if welcome == "y":
    while True:
            login1 = input("\033[1;36;40mLogin:\033\033[1;35;40m")
            login2 = input("\033[1;36;40mPassword:\033\033[1;35;40m")
            try:
                file = open(login1+".txt", "r")
                data = file.readline()
                file.close()
            except FileNotFoundError:
                file = open("Log.txt" , "a")
                file.write("[Server] Attempted Login From: ")
                file.write(login1+"@"+login2)
                file.write(" {Account Does Not Exist, Or Wrong Password}\n")
                file.close()
                os.system('cls')
                print("\033[1;36;40m[+] Error, Wrong Username/Pass [+]\033")
                time.sleep(1)
                print("\033[1;36;40m[+] Restarting [+]\033")
                time.sleep(1)
                ###########################################
                # Here Import or pass to your landing code#
                ###########################################
            
            if data == login1+":"+login2:
                try:
                    file = open("Log.txt" , "a")
                    file.write("[Server] Acc Login From ")
                    file.write(login1+"@"+login2)
                    file.write('\n')
                    file.close()
                    os.system('cls')
                    time.sleep(1)
                    print("\033[1;36;40m[+] Login Sucsessful [+]\n[+] Welcome To Lewd [+]\033")
                    time.sleep(2)
                ###########################################
                # Here Import or pass to your landing code#
                ###########################################

        
                    
                except FileNotFoundError:
                    file = open("Log.txt" , "a")
                    file.write("[Server] Attempted Login From: ")
                    file.write(username+"@"+password)
                    file.write(" {Account Does Not Exist, Or Wrong Password}\n")
                    file.close()
                    os.system('cls')
                    print("\033[1;36;40m[+] Error, Wrong Username/Pass [+]\033")
                    time.sleep(1)
                    print("\033[1;36;40m[+] Restarting [+]\033")
                    time.sleep(1)
                    import Login
                    
                
                break
            print("\033[1;36;40mIncorrect username or password.\033")
if welcome == "n":
        
    username  = input("\033[1;36;40m[+] Username:\033\033[1;35;40m")
    password  = input("\033[1;36;40m[+] Password:\033\033[1;35;40m")
    try:
        file = open(username+".txt", "x")
        file.write(username+":"+password)
        file.close()
        os.system('cls')
                
    except FileExistsError:
        os.system('cls')
        time.sleep(0.5)
        print("\033[1;36;40m[+] Error - Username Already Exists :/ [+]\033")
        time.sleep(1)
        print("\033[1;36;40m[Restarting]\033")
        time.sleep(1)
        import Login
                
print("\033[1;36;40m[+] Acc Added [+]\033\033[1;35;40m")
key = input("\033[1;36;40mAutho Key:\033\033[1;35;40m ")
try:
    file = open(key+".txt", "r")
    dataa = file.readline()
    file.close()
            #error Handler
except FileNotFoundError:
    file = open("Log.txt" , "a")
    file.write("[Server] Wrong/Fake Autho Key From : ")
    file.write(username+"@"+password)
    file.write(" Using Key:")
    file.write(key)
    file.write("{Key Dosnt Exist}\n")
    file.close()
    os.system('cls')
    os.remove(username+".txt") ## Deletes Account 
    print("\033[1;36;40m[+] Error, Wrong Authentication Key [+]\033\033[1;36;40m\033")
    time.sleep(1)
    print("\033[1;36;40m[+] Restarting [+]\033")
    time.sleep(1)
    import Login
            
if dataa == key+"@ClamLq":
        os.system('cls')
        print("\033[1;36;40m[+] Account Authorised.. Please Wait [+]")
        time.sleep(1)
        os.system('cls')
        print("\n════════════════════════════                         [+] Acc Details [+]")
        print(" [+] Username:", username)
        print("════════════════════════════ ")
        print(" [+] Password:", password)
        print("════════════════════════════ ")
        print(" [+] AuthCode:", key)
        print("════════════════════════════ ")
        print(" [+] Date:",currentDT.day,"/",currentDT.month,"/",currentDT.year)
        print("════════════════════════════ ")
        print(" [+] Time:",currentDT.hour,":",currentDT.minute)
        print("════════════════════════════ ")
        print("\n")
        print("                                                      [+] WARNING [+]\n")
        print("\033[1;36;40m[+] By Typing Yes, One Time AuthCode Will be Deleted [+]")
        accept = input("\033[1;36;40m[+] I Accept The Agreement and Accept that Coderbox Is Not Reliable For Refund Upon forgeting of password [y/n]:\033\033[1;35;40m ")
                        
        if accept == 'y':
            file.close()
            os.remove(key+".txt")
            os.system('cls')
            file = open("Log.txt" , "a")
            file.write("[Server] Acc Creation From ")
            file.write(username+"@"+password)
            file.write(" Using Key:")
            file.write(key)
            file.write(" {Key Deleted Sucsessfuly}\n")
            file.close()
            print("[+] Welcome, Loading.. [+]")
            time.sleep(2)
             ###########################################
             # Here Import or pass to your landing code#
             ###########################################
                    
           
            
                
        if accept == 'n':
            os.system('cls')
            print("\033[1;36;40m[+] Please Accept Agereement, {Acc Creation Terminated} [+]\033")
            os.remove(username+".txt")
            time.sleep(2)
            import Login
                    

