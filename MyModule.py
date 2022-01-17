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

#def passkontroll(password:str):
#	"""parooli kinnitamine
#	:param srt password:parool, mille kasutaja sisestas
#	:rtype:str
#	"""
#	ls=list(psword)
#	for e in ls:
#		if e.isdigit(): a=True
#		if e.isalpha(): b=True
#		if e.isupper(): c=True
#		if e.islower(): d=True
#	if a==True and b==True and c==True and d==True:
#		k=True
#	else:
#		k=False
#	return k

def passOK(password:str):
	"""parooli kinnitamine
	:param srt password:parool, mille kasutaja sisestas
	:rtype:str
	"""
	str0 = ".,:;!_*-+()/#¤%&"
	alpha=digit=upper=special=0
	ls = list(str0)
	psword = list(password)
	for i in range(len(psword)):
		if psword[i].isupper():
			upper=1
		if psword[i].isalpha():
			alpha=1
		if psword[i].isdigit():
			digit=1
		if psword[i] in ls:
			special=1
	if alpha==1 and digit==1 and upper==1 and special==1:
		passOK=True
	else:
		passOk=False
	return passOk

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
import time, sys
def update_progress(progress):
    barLength = 10 # Muutke seda, et muuta edenemisriba pikkust
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "viga: progressi var peab olema ujuv\r\n"
    if progress < 0:
        progress = 0
        status = "Peata...\r\n"
    if progress >= 1:
        progress = 1
        status = "Valmis...\r\n"
    block = int(round(barLength*progress))
    text = "\rProtsenti: [{0}] {1}% {2}".format( "■"*block + "☻"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

def failist_lugemine(f:str,u:list):
	"""Info failist f listisse l
	"""
	fail=open(f,"r")
	for rida in fail:
		u.append(rida.strip())
	fail.close()
	return u

def failist_pass(a:str,p:list):
	"""Info failist f listisse l
	"""
	fail=open(a,"r")#чтение файла
	for rida in fail:
		p.append(rida.strip())
	fail.close()
	return p

def failisse_salvestamine(f:str,u:list):
	fail=open(f,"w")#перезапись файла
	for el in u:
		fail.write(el+"\n")
	fail.close()

def rida_salvestamine(f:str,rida:str):
	fail=open(f,"a")#режим до записи
	fail.write(rida+"\n")
	fail.close()
