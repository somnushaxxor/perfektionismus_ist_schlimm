f_ein = open('Perepis.txt', 'r')

counter = 0
for line in f_ein:
	line = line.split()
	geburtsdatum = line[3]
	geburtsdatum = geburtsdatum.split('.')
	geburtsjahr = geburtsdatum[2]
	if(int(geburtsjahr)<1978):
		print(line[0])
		counter+=1
print(counter)
r = input().split()
print(r)
f_ein.close()
f_ein = open('Perepis.txt', 'r')
for line in f_ein:
	line1 = line.split()
	geburtsdatum = line1[3]
	geburtsdatum = geburtsdatum.split('.')
	geburtsjahr = geburtsdatum[2]
	if(int(r[0])<int(geburtsjahr)<int(r[1])):
		print(line)