import random
def autopass()->str:
	"""loo juhuslik parool
	:rtype:str
	"""
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper()
    # 'QWERTYUIOPASDFGHJKLZXCVBNM'
	str4 = str0+str1+str2+str3
	ls = list(str4)
	random.shuffle(ls)
	psword="".join([random.choice(ls) for x in range(12)])
	print("See on sinu password -> ",psword)
	return psword

def passkontroll(password:str):
	"""parooli kinnitamine
	:param srt password:parool, mille kasutaja sisestas
	:rtype:str
	"""
	ls=list(psword)
	for e in ls:
		if e.isdigit(): a=True
		if e.isalpha(): b=True
		if e.isupper(): c=True
		if e.islower(): d=True
	if a==True and b==True and c==True and d==True:
		k=True
	else:
		k=False
	return k

def kõik(user=str,passwords=str):
	"""näitab kõiki kasutajaid ja kõiki paroole
	:param str user:kasutajad
	:param str passwords:paroolid
	:rtype:str
	"""
	k=0
	for users in user:
		print(user,end="_")
		print(passwords[k])
		k+=1
