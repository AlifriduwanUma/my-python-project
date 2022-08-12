from tkinter import *

## โปรอกรมคำนวนณพื้นที่สี่เหลี่ยม

## Creat tkinter
window = Tk()
window.title('โปรอกรมคำนวนณพื้นที่สี่เหลี่ยม')
window.geometry('250x100+450+250')

## Creat Label
Label(text='กรุณากรอกความกว้าง').grid(row=0,sticky=W)
Label(text='กรุณากรอกความยาว').grid(row=1,sticky=W)
Label(text='พื้นที่สี่หลี่ยม').grid(row=2,sticky=W)

widht_ = IntVar()
length_ = IntVar()

## Creat Entry

et1 = Entry(textvariable=widht_,)
et1.grid(row=0,column=1)

et2 = Entry(textvariable=length_)
et2.grid(row=1,column=1)

et3 = Entry()
et3.grid(row=2,column=1)

## Creat function

def calculate():
    et3.delete(0,END)
    a = widht_.get()
    b = length_.get()
    are = a * b
    et3.insert(0,are)

def deleteText():
    et1.delete(0,END)
    et2.delete(0,END)
    et3.delete(0,END)

btn1 = Button(text='คำนวณ',command=calculate).grid(row=3,column=1,sticky=W)
btn2 = Button(text='ล้างข้อมูล',command=deleteText).grid(row=3,column=1,sticky=E)


window.mainloop()

