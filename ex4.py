# Exercise 4
#code with harry
#coding and decoding
import random
import string
message = str(input("Enter the message: "))
print(f"Do you want to code or decode the { message } ")
input_by_the_user=str(input("code/decode:")).upper()
if(input_by_the_user=="CODE"):
    print(input_by_the_user)
    idx=len(message)
    decode=message[1:int(len(message))-1]
    fletter=message[0]                               #firstr letter of string given by the user
    lletter=message[int(idx)-1]
    print(random.choice(string.ascii_lowercase)*3+lletter+decode+fletter+random.choice(string.ascii_lowercase))
else: 
    print("end")

