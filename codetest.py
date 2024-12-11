#Write a python program to generate a random password with a mix of characters

import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9',]
symbols=['!','@','#','$','%','&','*','+']
print("welcome to passward generator!")
n_let=int(input("how many letter do you want in your passward"))
n_num=int(input("how many symbol do you want in your passward"))
n_spechar=int(input("how many special charater do you want in your passward"))
passward=" "
for i in range(1,n_let+1):
         char=random.choice(letters)
         passward+=char
for i in range (1,n_num+1):
         char=random.choice(numbers)
         passward+=char
for i in range (1,n_spechar+1):
         char=random.choice(symbols)
         passward+=char         
print(passward)         
         
         

         
