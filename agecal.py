import tkinter
from tkinter import *
from datetime import date
root=Tk()
root.geometry("800x600")
root.resizable(FALSE,FALSE)
root.title("Age Calculator")
image1=PhotoImage(file="agecalcbg.png")
Label(root,image=image1,height=0,width=1000).place(x=-1,y=1)
def calculateAge():
    today=date.today()
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    Label(text=f"{nameValue.get()}, you are {age} year's old.",font=30).place(x=200,y=450)
Label(text="Name:",font=25,background="black",width=8,fg="white").place(x=200,y=200)
Label(text="Year:",font=20,background="black",width=8,fg="white").place(x=200,y=250)
Label(text="Month:",font=20,background="black",width=8,fg="white").place(x=200,y=300)
Label(text="Day:",font=20,background="black",width=8,fg="white").place(x=200,y=350)
nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()
nameEntry=Entry(root,textvariable=nameValue,width=25,bd=2,font=30)
nameEntry.place(x=300,y=200)
yearEntry=Entry(root,textvariable=yearValue,width=25,bd=2,font=30)
yearEntry.place(x=300,y=250)
monthEntry=Entry(root,textvariable=monthValue,width=25,bd=2,font=30)
monthEntry.place(x=300,y=300)
dayEntry=Entry(root,textvariable=dayValue,width=25,bd=2,font=30)
dayEntry.place(x=300,y=350)
Button(text="Calculate Age",font=30,bg="white",background="#4784c9",borderwidth=1,fg="white",width=12,height=1,command=calculateAge).place(x=330,y=400)
root.mainloop()