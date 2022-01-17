from MyModule import*
from random import *
import time, sys
from module1 import *
users=[]
password=[]
users=failist_lugemine("Users.txt",users)
print(users)
password=failist_pass("Pass.txt",password)
print(password)

while True:
	print("Registreerimine = 1 \nAutoriseerimine = 2 \nLogin välja = 3")
	i=int(input())
	if i==1:
		print("Registreemine")
		while 1:
			login=input("Kasutajanimi -> ")
			if login not in users:
				print("Kasutajanimi soobib")
				users=rida_salvestamine("Users.txt",login)
				#users.append(login)
				break
			else:
				print("See kasutajanimi juba registreeritud!")
		i=input("Valige, kas soovite parooli luua arvuti(A) või teie enda poolt(I) => ")
		if i.upper()=="A":
				pas=autopass()
				password=rida_salvestamine("Pass.txt",pas)
				#password.append(pas)
		elif i.upper()=="I":
			pas=input("Sisestage oma parool -> ")
			kont=passOK(password)
			if kont==True:
				password=rida_salvestamine("Pass.txt",pas)
				#password.append(pas)
				break
			else:
				print("Parool ei soobib")
	elif i==2:
		print("Avtoriseerimine")
		login=input("Sisestage oma kasutajanimi -> ")
		passworde=input("Sisestage oma parool -> ")
		if password.index(passworde)==users.index(login):
			print("Tere tulemast!")
			print()
			while 1:
				try:
					play=int(input("Kas soovite mängida arvu 1 kuni 100 ära arvamist? 1 - (jah) 2 - (ei) =>"))
				except ValueError:
					print("Ainult numbrid")
				if play==2:
					print("Head aega!")
					exit(0)
				print ("")
				print ("Edenemine: 0->100")
				for i in range(101):
				   time.sleep(0.1)
				   update_progress(i/100.0)
				print ("")
				print ("Test lõpetatud")
				time.sleep(0.5)
				NumberRandom=randint(1,100)
				User=0
				while User!=NumberRandom: 
					User=int(input("Arva ära arv vahemikus 1 kuni 100 => ")) 
					if User > NumberRandom:
					  print("Arv peab olema väiksem!") 
					elif User < NumberRandom: 
						print("Arv peab olema suurem!") 
					else: 
						print("Arvasite ära, see number = ",NumberRandom) 
				break
	elif i==3:
		print("Head aega!")
		exit(0)
	else:
		print("Valige 1,2 või 3!")
		print("")
