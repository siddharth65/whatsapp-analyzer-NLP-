import os
cmd ="clear"
os.system(cmd)
print "\n\n--------------------------------------------------------------"
print "------------------- WHATSAPP CHAT ANALYZER -------------------"
print "--------------------------------------------------------------"
print "------------------------------------------  Siddharth Agarwal "
print "-----------------------------------------Under the guidance of"
print "-------------------------------------------  Mr. R.Srinivasan "
dates={}
texts={}
names={}
times={}
dictWords={}
hour={}
time={}
minute={}
words=[]
count={}

i=0

for line in open('chat.txt'):
	if(line.split('-') == [line] or line.split(':')== [line]):
		continue
	dates[i], texts[i] = line.split('- ',1)
	names[i], texts[i] = texts[i].split(':',1)
	dates[i], times[i] = dates[i].split(', ',1)
	hour[i], minute[i] = times[i].split(':',1)
	i = i+1
#rint names
for i in names:
	#print names[i],
	if names[i] in count:
		count[names[i]]+=1
	else:
		count[names[i]]=1
#print names[0]
i=0
cwords={list(count)[0]:0,list(count)[1]:0}
for text in texts:
	for word in texts[text].split():
		if word.lower() in dictWords:
			dictWords[word.lower()] += 1
		else:
			dictWords[word.lower()] = 1
			words.append(word.lower())
		cwords[names[i]]+=1
	i+=1
print "\n\n",cwords, "\n\n\n"
# most used words
'''
for w in sorted(dictWords,key=dictWords.get,reverse=True):
	print(w,dictWords[w])
'''
# conversations list:
conversation = 0
j=1

print "Total Different Conversations:\n"
for t in range(i-1):
	if t == 43550:
		break
	if (dates[t]!=dates[t+1] or hour[t]!=hour[t+1]):
		print j,")",dates[t+1],times[t+1],(texts[t+1],t+2)
		conversation = conversation +1
		j+=1
hours={}
for h in hour:
	if hour[h] in hours:
		hours[hour[h]] += 1
	else:
		hours[hour[h]] = 1

'''for h in sorted(hours,key=hours.get,reverse=True):
	print(h,hours[h])
'''
print list(cwords)[0],list(cwords)[1]
m=0
o=0
ig=0
for i in texts:
	if names[i]=="Sid":
		m+=1
	else:
		o+=1
print o,m

for i in range(0,20):
	if (hour[i]==hour[i+1]):
		if minute[i]==minute[i+1] or int(minute[i])==int(minute[i+1])-1:
			x=1
		elif int(minute[i+1])-int(minute[i])>2:
			ig+=1
	else:
		if minute[i]>=59 and minute[i+1]<=1:
			x=1
		else:
			ig+=1
print "No of times reply is late:",ig
if ig < (m+o)/5:
	print "Interested"
else:
	print "Not Interested"

if o>2*m:
	print "Me less interested"
elif m>2*o:
	print "Other less interested"

