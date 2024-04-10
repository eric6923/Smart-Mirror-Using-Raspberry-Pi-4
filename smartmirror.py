from time import strftime
import tkinter  as tk 
from tkinter import ttk
from tkinter import *
import requests
import time

while True:
    try:
        requests.get('https://www.google.com/').status_code
        break
    except:
        time.sleep(5)
        pass
from pygooglenews import GoogleNews
gn = GoogleNews(lang = 'en', country = 'IN')
my_w = tk.Tk()

#my_w .state('zoomed')
my_w ['bg']='black'
my_w.attributes('-zoomed', True)


def weather():
    city="coimbatore"
    key='321d97c23fec5c922bd3a96e06055ed1'
    source=requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city +'&appid='+key)
    data=source.json()  

    a = "      "+data['name']+'\n'
    b="Weather : "+data['weather'][0]['description']+'\n'
    c = "Temp : " + str(round(data['main']['temp']/10,2))+"'c"+" \n  Pressure : "+str(data['main']['pressure'])+" hpa"+" \nHumidity : "+str(data['main']['humidity'])+"%"
    e=data['weather'][0]['description']
    l2.config(text=str(a+b+c))
    #print(str(a+b+c))
    
    lw=Label(my_w,image=img2,anchor='c')
    lw.image = img2
    l2.after(1000000,weather)

def get_titles():
	search=gn.top_news()
	newsitem=search['entries']
	c=0
	mydata=[]
	for item in newsitem[:12]:
		if(c>1):
			mydata.append((item.title).partition(" - ")[0])
		c=c+1
	#print(mydata)
	for i in range(10):
		Button(frame, text=mydata[i],bg='black',fg='white',font=my_font1).grid(row=i, column=0, sticky='ew')
	frame.place(x=650,y=670) 
	frame.after(120000,get_titles)


def my_time():
    time_string = strftime('%H:%M:%S %p \n %A \n %x') # time format
    l1.config(text=time_string)
    l1.after(1000,my_time) 
	
my_font=('times',42,'bold') 
my_font1=('times',16,'bold') 

l1=tk.Label(my_w,font=my_font,bg='black',fg='white')
l1.place(x=200,y=500)

l2=tk.Label(my_w,font=('times',30,'bold'),bg='black',fg='white')
l2.place(x=300,y=40)

l3=tk.Label(my_w,font=my_font1,bg='black',fg='white')
l3.place(x=30,y=250,width=1000)

frame = Frame(my_w, bg='#F2B33D')
for i in range(10):
    Button(frame, text="",font=my_font1).grid(row=0, column=0, sticky='ew')
frame.place(x=200,y=570)

l4=tk.Label(my_w,text="NEWS",font=my_font,bg='black',fg='white')
l4.place(x=990,y=600)

imgn=PhotoImage(file="4.png")
ln=Label(my_w,image=imgn,bg='black',anchor='c')
ln.image = imgn
ln.place(x=1200,y=550)

img2=PhotoImage(file="3.png")
lw=Label(my_w,image=img2,bg='black',anchor='c')
lw.image = img2
lw.place(x=50,y=10)

my_time()
get_titles()
weather()
my_w.mainloop()