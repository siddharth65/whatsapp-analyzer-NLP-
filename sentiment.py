dates={}
datesn={}
textp={}
textn={}
names={}
namesn={}
times={}
dicp={}
hour={}
hourn={}
times={}
minute={}
timesn={}
minuten={}
dicn={}
words=[]
i=0


#split data

for line in open('pat.txt'):
	if(line.split('-') == [line] or line.split(':')== [line]):
		continue
	dates[i], textp[i] = line.split('-',1)
	names[i], textp[i] = textp[i].split(':',1)
	dates[i], times[i] = dates[i].split(', ',1)
	hour[i], minute[i] = times[i].split(':',1)
	i = i+1




for text in textp:
	for word in textp[text].split():
		if word.lower() in dicp:
			dicp[word.lower()] += 1
		else:
			dicp[word.lower()] = 1
			words.append(word.lower())


nm=0

for w in sorted(dicp,key=dicp.get,reverse=True):
	if(w!="<media" and w!="omitted>"):
		print(w,dicp[w])

threadsp={}
for name in names:
	if names[name] in threadsp:
		threadsp[names[name]] +=1
	else:
		threadsp[names[name]] = 1
fdatep={}
def get_ke(val): 
    for key, value in fdatep.items(): 
         if val == value: 
             return key
for i in dates:
	if dates[i] in fdatep:
		fdatep[dates[i]]+=1
	else:
		fdatep[dates[i]]=1
print ("Maximum Conversation on"),
print get_ke(max(fdatep.values())),":-", max(fdatep.values()), "threads"
'''
for w in (dicp):
	print w	
	if w=="<media":
		nm+=1
print "Media Shared", nm ,"times."
'''
print("-----------------------------------------------------------------------------")
print("/////////////////////////////////////////////////////////////////////////////")
print("-----------------------------------------------------------------------------")

for line in open('khn.txt'):
	if(line.split('-') == [line] or line.split(':')== [line]):
		continue
	datesn[i], textn[i] = line.split('-',1)
	namesn[i], textn[i] = textn[i].split(':',1)
	datesn[i], timesn[i] = datesn[i].split(', ',1)
	hourn[i], minuten[i] = timesn[i].split(':',1)
	i = i+1

for text in textn:
	for word in textn[text].split():
		if word.lower() in dicn:
			dicn[word.lower()] += 1
		else:
			dicn[word.lower()] = 1
			words.append(word.lower())

for w in sorted(dicn,key=dicn.get,reverse=True):
	print(w,dicn[w])

'''
pm=0
for w in dicp:
	if w=="<media":
		pm+=1
		print w

print "Media Shared", pm ,"times."
'''
print("-----------------------------------------------------------------------------")
threads={}
for name in namesn:
	if namesn[name] in threads:
		threads[namesn[name]] +=1
	else:
		threads[namesn[name]] = 1

print(threads)
print("-----------------------------------------------------------------------------")
hours={}
for h in hour:
	if hour[h] in hours:
		hours[hour[h]] += 1
	else:
		hours[hour[h]] = 1
def get_k(val): 
    for key, value in hours.items(): 
         if val == value: 
             return key
print "Peak time", get_k(max(hours.values())),"00 hours ", max(hours.values()), "threads"

fdate={}
def get_key(val): 
    for key, value in fdate.items(): 
         if val == value: 
             return key
for i in datesn:
	if datesn[i] in fdate:
		fdate[datesn[i]]+=1
	else:
		fdate[datesn[i]]=1
print ("Maximum Conversation on"),
print get_key(max(fdate.values())),":-", max(fdate.values()), "threads"
test = raw_input();
c=0
q=0
p=0

for word in test.split():
	if word.lower() in dicp:
		p=dicp[word]
		
	else:
		p=0
	#print p
	if word.lower() in dicn:
		q=dicn[word]
	else:
		q=0
	#print q
	if(p>q):
		c+=1
	elif(p<q):
		c-=1
	else:
		c=c
	#print c

if(c<0):
	print ("Negative")
else:
	print("Positive")
