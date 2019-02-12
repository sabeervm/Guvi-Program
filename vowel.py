vw=['a','e','i','o','u']
alp=input()
if((alp>='a' and alp<= 'z') or (alp>='A' and alp<='Z')):
	if alp in vw:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
