import requests
from bs4 import BeautifulSoup
def get_data_contests():
	r=requests.get("https://clist.by/")
	soup=BeautifulSoup(r.text,'html.parser')
	body=soup.find(id="contests")
	items=body.find_all(class_="row contest coming")
	return items
def get_contests_now(items):
	lis=[]
	co=0
	for timel in items:
		time=timel.find(class_="col-md-4 col-sm-6 timeleft countdown")
		s=str(time.get_text())
		st=""
		ok=0
		for i in range(0,len(s)) :
			t=(s[i])
			if t.isdigit() or t.isalpha():
				st=st+t
			if t.isalpha() :
				ok=1
		c=0
		if ok==1 :
			for i in range(0,len(st)):
				if st[i]=='d' :
					st=st[:i]+" "+st[i:]
		else:
			for i in range(0,len(st)-1):
				if i%2==1 :
					st=st[:i+1+c]+":"+st[i+1+c:]
					c=c+1
		st="Time Left : "+st
		if ok==0 and st[12]=="0" and ord(st[13])<ord('4') :
			ok=0
		else:
			ok=1
		item=timel.find(class_="col-md-7 col-sm-8 event")
		webadd=item.find(class_="title")
		we=webadd.find('a')
		t=str(we.get('href'))
		t="Link      : "+t
		if ok==0 :
			lis.append((st,t))
		return lis
def print_data(lists):
	if (len(lists))==0 :
		print("No Contests!Practice Now")
	else:
		for lis in lists:
			print(lis[0])
			print(lis[1])
			print("******************")
if __name__ == '__main__':
	info=get_data_contests()
	lists=get_contests_now(info)
	print_data(lists)
	