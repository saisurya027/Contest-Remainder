import requests
from bs4 import BeautifulSoup
r=requests.get("https://clist.by/")
soup=BeautifulSoup(r.text,'html.parser')
lis=[]
strs=[]
contest=soup.find(id="contests")
items=contest.find_all(class_="row contest coming")
co=0
comp="4"
for dat in items:
	#dat=items[2].find(class_="col-md-5 col-sm-4")
	into=dat.find(class_="col-md-4 col-sm-6 timeleft countdown")
	s=str(into.get_text())
	st=""
	ok=0
	for i in range(0,len(s)) :
		t=(s[i])
		if(t.isdigit() or t.isalpha()):
			st=st+t
		if(t.isalpha()):
			ok=1
	#print(st)
	c=0
	#co=0
	if(ok==1):
		for i in range(0,len(st)):
			if(st[i]=='d'):
				st=st[:i]+" "+st[i:]
	else:
		for i in range(0,len(st)-1):
			if(i%2==1):
				st=st[:i+1+c]+":"+st[i+1+c:]
				c=c+1
	st="Time Left : "+st
	if(ok==0 and st[12]=="0" and ord(st[13])<ord('4')):
		print(st)
	else:
		ok=1
	item=dat.find(class_="col-md-7 col-sm-8 event")
#print(item)
#for line in item.find_all('a'):
#	strs.append(line.get('href'))
	web=item.find(class_="title")
	we=web.find('a')
	t=str(we.get('href'))
	t="Link      : "+t
	if(ok==0):
		print(t)
		co=co+1
		print("***************************")
if(co==0):
	print("No Contests!Practice Now")
	