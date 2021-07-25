from tkinter import *
from functools import partial
import random

top=Tk()
top.geometry("1300x800")
top.title("Random Password Generator")
top.config(background="grey")

img=PhotoImage(file="key.png")
key=Label(top,image=img,bg="grey").place(x=425,y=15)
heading=Label(top,text="Password Generator",bg="grey",fg='White',font="Calibri 30 italic").place(x=520,y=20)


def gen(lower,upper,number,symbol,ambig,leng):

    lengt=leng.get()
    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    symbols="!@#$%^&*"
    ambi="~`()_-+=/\|{}[]()<>:';?.,"
    
    all=""

    if lower.get()==1:
        all=all+lowercase
    if upper.get()==1:
        all=all+uppercase
    if number.get()==1:
        all=all+numbers
    if symbol.get()==1:
        all=all+symbols
    if ambig.get()==1:
        all=all+ambi



    generate="".join(random.sample(all,lengt))
    place=Label(top,text=generate,width=50,bg="#f3327c",font="Calibri 14 bold italic").place(x=780,y=390)
    
lower=IntVar()
upper=IntVar()
number=IntVar()
symbol=IntVar()
ambig=IntVar()


leng=IntVar()
l=Label(top,text="Enter the Length for Password : ",fg="white",bg="grey",font="Calibri 14 italic").place(x=780,y=200)
length=Entry(top,textvariable=leng,width=30,font="Calibri 14 italic").place(x=780,y=250)


lo=Label(top,text="Lowercase Characters : ",fg="white",bg="grey",font="Calibri 14 ").place(x=250,y=150)
cb1=Checkbutton(top,text="(e.g.abcde)",variable=lower,onvalue=1,offvalue=0,activebackground="grey",activeforeground="white",bg="grey",fg="blue",font="Calibri 14 italic").place(x=450,y=148)

up=Label(top,text="Uppercase Characters : ",fg="white",bg="grey",font="Calibri 14 ").place(x=250,y=250)
cb2=Checkbutton(top,text="(e.g.ABCDE)",variable=upper,onvalue=1,offvalue=0,activebackground="grey",activeforeground="white",bg="grey",fg="blue",font="Calibri 14 italic").place(x=450,y=248)

num=Label(top,text="Numbers : ",fg="white",bg="grey",font="Calibri 14 ").place(x=250,y=350)
cb3=Checkbutton(top,text="(e.g.123456)",variable=number,onvalue=1,offvalue=0,activebackground="grey",activeforeground="white",bg="grey",fg="blue",font="Calibri 14 italic").place(x=450,y=348)

sy=Label(top,text="Symbols : ",fg="white",bg="grey",font="Calibri 14 ").place(x=250,y=450)
cb4=Checkbutton(top,text="(e.g.!@#$%)",variable=symbol,onvalue=1,offvalue=0,activebackground="grey",activeforeground="white",bg="grey",fg="blue",font="Calibri 14 italic").place(x=450,y=448)

am=Label(top,text="Ambiguous Characters : ",fg="white",bg="grey",font="Calibri 14 ").place(x=250,y=550)
cb5=Checkbutton(top,text="(e.g.`~-_(){}[]?/\|<>)",variable=ambig,onvalue=1,offvalue=0,activebackground="grey",activeforeground="white",bg="grey",fg="blue",font="Calibri 14 italic").place(x=450,y=548)

gen=partial(gen,lower,upper,number,symbol,ambig,leng)

img2=PhotoImage(file="gen.png")
gene=Label(top,width=100,height=100,bg="grey",image=img2).place(x=700,y=350)


btn=Button(top,text="Generate Password",command=gen,font="Calibri 14 italic",bg="black",fg="white",activebackground="magenta",activeforeground="blue",width=30).place(x=780,y=300)


top.mainloop()
