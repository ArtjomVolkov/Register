def game(play:int):
	"""
	"""
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
