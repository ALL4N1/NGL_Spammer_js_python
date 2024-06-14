import os
import subprocess

def msg_num():
    ch = input("How much you wanna spam (Default 100)? ")
    if(ch==""):
        return 100
    else:
        return int(ch)

input_txt = "@echo off\necho 2\n"
target_user = input("Enter who you wanna spam? ")
target_msg = input("Enter the spam msg: ")
target_msg = target_msg.replace(" ","_")
msg_count = msg_num()
input_txt += f"echo {target_user}\necho {target_msg}\necho {msg_count}"

f = open("inputs.bat","w")
f.write(input_txt)
f.close()
subprocess.run(["run_7_alot.bat"], shell=True)