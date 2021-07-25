from tkinter import *
from functools import partial
from tkinter import messagebox
import requests, json

top=Tk()

citi=StringVar()

citylabel=Label(top,background='#f3327c',text="Enter City Name: ",foreground="White",font="Courier 20 bold").place(x=400,y=100)
citien=Entry(top,width=20,font="Courier 14 ",textvariable=citi).place(x=670,y=106)

top.geometry('13000x800')
top.title('Weather Application')
top.config(background='#f3327c')


def cred():
    cr=Toplevel()
    cr.geometry('300x200')
    cr.title('CREDITS')
    Label(cr,text='version:1.0').place(x=10,y=10)
    Label(cr,text='Created By: Siddhant V.').place(x=10,y=30)
    Label(cr,text='API generated from OpenweatherMap.').place(x=10,y=50)

heading=Label(top,text="Weather Application",background='#f3327c',foreground="white",font="Calibri 30 bold italic").place(x=550,y=1)
bl=Button(top,text="CREDITS",fg="White",bg="#f3327c",activebackground="yellow",command=cred).place(x=1280,y=5)

lb=Label(top,bg="#f3327c",text="*CITY NAME*",fg="White",font="Calibri 25 bold italic").place(x=240,y=130)

#base url
base="https://api.openweathermap.org/data/2.5/weather"
#Enter API key here
apikey="d7802c3edc254081d6e569d0f5ebea1c"

def pro(citi):
    cityname=citi.get()
    completeurl=base+"?q="+cityname+"&appid="+apikey
    response=requests.get(completeurl)
    x=response.json()
    if apikey=="":
        return messagebox.showerror('Error','Enter your API key:')
    elif cityname=='':
        return messagebox.showerror('Error','Enter City Name:')
    else:
        if x['cod']=="404":
            return messagebox.showerror('Error','City Not Found')
        else:
            lb.config(text=cityname) 
            #temperature
            y=x["main"]
            #temperature in kelvin
            currenttemp_kel=y["temp"]
            #temp in celcius
            currenttemp=str(round(currenttemp_kel-273.15))+str(chr(176))+"c"
            #placing at label temp2
            temp2.config(text=currenttemp)

            #pressure
            pre=y["pressure"]
            pressure=str(pre)+"hPa"
            #placing at label pre2
            pre2.config(text=pressure)

            #humidity
            hum=y["humidity"]
            humidity=str(hum)+"%"
            #placing at label hum2
            hum2.config(text=humidity)

            #weather Description
            z=x["weather"]
            weatherdescription=z[0]["description"]
            wd=str(weatherdescription)
            #placing at label wd2
            wd2.config(text=wd)



main1=PhotoImage(file="main.png")
labelmain1=Label(top,height=430,width=516,image=main1,bg="#f3327c")
labelmain1.place(x=730,y=140)

img1=PhotoImage(file="temperature.png")
labeltempimg=Label(top,height=100,width=100,image=img1,bg="#f3327c")
labeltempimg.place(x=130,y=160)

temp1= Label(top,text='TEMPERATURE',bg='#f3327c',fg="blue")
temp1.config(font=("Calibri", 20))
temp1.place(x=240,y=185)

temp2= Label(top,text='*Temperature*',bg='#f3327c',fg="white")
temp2.config(font=("Calibri", 14))
temp2.place(x=240,y=220)

img2=PhotoImage(file="pressure-gauge.png")
labelpressureimg=Label(top,height=100,width=100,image=img2,bg="#f3327c")
labelpressureimg.place(x=130,y=260)

pre1= Label(top,text='PRESSURE',bg='#f3327c',fg="blue")
pre1.config(font=("Calibri", 20))
pre1.place(x=240,y=285)

pre2= Label(top,text='*Pressure*',bg='#f3327c',fg="white")
pre2.config(font=("Calibri", 14))
pre2.place(x=240,y=320)

img3=PhotoImage(file="humidity.png")
labelhumidityimg=Label(top,height=100,width=100,image=img3,bg="#f3327c")
labelhumidityimg.place(x=130,y=360)

hum1= Label(top,text='HUMIDITY',bg='#f3327c',fg="blue")
hum1.config(font=("Calibri", 20))
hum1.place(x=240,y=385)

hum2= Label(top,text='*Humidity*',bg='#f3327c',fg="white")
hum2.config(font=("Calibri", 14))
hum2.place(x=240,y=420)


img4=PhotoImage(file="description.png")
labeldescriptionimg=Label(top,height=100,width=100,image=img4,bg="#f3327c")
labeldescriptionimg.place(x=130,y=460)

wd1= Label(top,text='WEATHER DESCRIPTION',bg='#f3327c',fg="blue")
wd1.config(font=("Calibri", 20))
wd1.place(x=240,y=485)

wd2= Label(top,text='*Weather Description*',bg='#f3327c',fg="white")
wd2.config(font=("Calibri", 14))
wd2.place(x=240,y=520)



#la=Label(top,font="Calibri 12")
#la.place(x=150,y=250)
pro=partial(pro,citi)
btn=Button(top,text="PROCEED",activebackground="black",activeforeground="white",bg="#f3327c",fg="white",command=pro).place(x=900,y=107)

top.mainloop()

        



