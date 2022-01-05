from MyModule import*
users=["Artjom"]
password=["qwerty"]

while True:
	print("Registreerimine = 1 \nAutoriseerimine = 2 \nLogin välja = 3")
	i=int(input())
	if i==1:
		print("Registreemine")
		while 1:
			login=input("Kasutajanimi -> ")
			if login not in users:
				print("Kasutajanimi soobib")
				break
			else:
				print("See kasutajanimi juba registreeritud!")
		i=input("Valige, kas soovite parooli luua arvuti(A) või teie enda poolt(I)")
		if i.upper()=="A":
				pas=autopass()
		elif i.upper()=="I":
			pas=input("Sisestage oma parool -> ")
			kont=passkontroll(paspassword)
			if kont==True:
				users.append(login)
				password.append(pas)
				break
			else:
				print("Parool ei soobib")
	elif i==2:
		print("Avtoriseerimine")
		login=input("Sisestage oma kasutajanimi -> ")
		passworde=input("Sisestage oma parool -> ")
		if password.index(passwords)==users.index(user):
			print("Tere tulemast!")
	elif i==3:
		print("Head aega!")
		exit(0)
	else:
		print("Valige 1,2 või 3!")
		print("")
