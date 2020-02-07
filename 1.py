f = open('mat_dv.txt', 'r')

max8=0
max9=0
max10=0
max11=0

for i in f:
	person = i.split()
	if(int(person[2])==8):
		if(int(person[3])+int(person[4])>max8):
			max8=int(person[3])+int(person[4])
			max8_name = person[0]+' '+person[1]
	if(int(person[2])==9):
		if(int(person[3])+int(person[4])>max9):
			max9=int(person[3])+int(person[4])
			max9_name = person[0]+' '+person[1]
	if(int(person[2])==10):
		if(int(person[3])+int(person[4])>max10):
			max10=int(person[3])+int(person[4])
			max10_name = person[0]+' '+person[1]
	if(int(person[2])==11):
		if(int(person[3])+int(person[4])>max11):
			max11=int(person[3])+int(person[4])
			max11_name = person[0]+' '+person[1]
print(max8_name, max10_name, max9_name, max11_name,sep='\n')
f.close()


f = open('mat_dv.txt', 'r')
k=0
algebra_max=0
algebra_winners = list()
geometrie_max=0
geometrie_winners = list()
for i in f:
	person = i.split()
	if(int(person[3])>algebra_max):
		algebra_max = int(person[3])
		algebra_winners.clear()
		algebra_winners.append(k)
	elif(int(person[3])==algebra_max):
		algebra_winners.append(k)
	if(int(person[4])>geometrie_max):
		geometrie_max = int(person[4])
		geometrie_winners.clear()
		geometrie_winners.append(k)
	elif(int(person[4])==geometrie_max):
		geometrie_winners.append(k)
	k+=1
print(algebra_winners)	
print(geometrie_winners)
f.close()
	

f = open('mat_dv.txt', 'r')	
k=0
for i in f:
	person = i.split()
	for a in algebra_winners:
		if(k==a):
			print(person[0]+' '+person[1])
	k+=1
f.close()

f = open('mat_dv.txt', 'r')	
k=0
for i in f:
	person = i.split()
	for g in geometrie_winners:
		if(k==g):
			print(person[0]+' '+person[1])
	k+=1
f.close()