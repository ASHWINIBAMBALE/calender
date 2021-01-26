from tkinter import *
from tkinter import ttk
import calendar
class main:
    def __init__(self,master):
        self.master=master
        self.month= IntVar()
        self.year=IntVar()
        self.months=(1,2,3,4,5,6,7,8,9,10,11,12)
    def getcal(self):
        m= self.month.get()
        y=self.year.get()
        cal=calendar.month(y,m,1,2)
        self.area.delete(0.0,END)
        self.area.insert(0.0,cal)
    def widgets(self):
        Label(self.master,text="calendar",font=("freesansbold",30),bd=10).pack()
        f=Frame(self.master,pady=10,padx=10)
        Label(f,text="months : ",font=("freesansbold",13)).grid()
        mon=ttk.combobox(f,width=7,font=("freesansbold",13),values=self.months,textvariable=self.month)
        mon.grid(row=0,column=1)
        mon.current(0)
        Lable(f,text="year:",font=("freesansbold",13)).grid(row=0,column=2)
        ttk.entry(f,width=9,font=("freesansbold",13),textvariable=self.year).grid(row=0,column=3)
        f.pack()
        self.area=text(self.master,font=('',15,'bold'),width=20,height=9,bd=15)
        self.area.pack()
        Button(self.master,command=self.getcal,text='get calandar',font=('',15,'bold'),bd=10).pack()
if __name__ == '__main__':
    root=Tk()
    main(root)
    root.title('calender')
    root.mainloop()