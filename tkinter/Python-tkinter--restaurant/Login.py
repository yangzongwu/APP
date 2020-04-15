#Author:YZW
import sqlite3
from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
from working_page import workingPage
from wp import workingPage as wp


def main():
    root = tkinter.Tk()
    app = Window1(root)

class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title('Restaurant Management System')
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        self.LabelTitle=Label(self.frame,text='Restaurant Management System',font=('arial',50,'bold'),bd=20,)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)

        self.Loginframe1=Frame(self.frame,width=1000,height=300,bd=20,relief='ridge')
        self.Loginframe1.grid(row=1,column=0)
        self.Loginframe2 = Frame(self.frame, width=1000, height=100,bd=20, relief='ridge')
        self.Loginframe2.grid(row=2, column=0)
        self.Loginframe3 = Frame(self.frame, width=1000, height=200,bd=20, relief='ridge')
        self.Loginframe3.grid(row=3, column=0)
#==============================================================================================
        self.lbUsername = Label(self.Loginframe1, width=6,text='Username', font=('arial', 30, 'bold'), bd=22)
        self.lbUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.Loginframe1, width=13,font=('arial', 30, 'bold'),
                                 textvariable=self.Username,bd=22)
        self.txtUsername.grid(row=0, column=1)

        self.lbPassword = Label(self.Loginframe1, width=6,text='Password', font=('arial', 30, 'bold'), bd=22)
        self.lbPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.Loginframe1, width=13,font=('arial', 30, 'bold'),
                                 textvariable=self.Password,bd=22)
        self.txtPassword.grid(row=1, column=1,padx=85)
#==============================================================================================

        self.btnLogin = Button(self.Loginframe2, text='Login',width=12,font=('arial',20,'bold'),
                               command=self.Login_System)
        self.btnLogin.grid(row=0, column=0)
        self.btnReset = Button(self.Loginframe2, text='Reset',width=12,font=('arial',20,'bold'),
                               command=self.Reset)
        self.btnReset.grid(row=0, column=1)
        self.btnExit = Button(self.Loginframe2, text='Exit',width=12,font=('arial',20,'bold'),
                              command=self.iExit)
        self.btnExit.grid(row=0, column=2)

#==============================================================================================

        self.btnRegistation=Button(self.Loginframe3,width=17,text='Registation System',state=NORMAL,
                                   font=('arial',20,'bold'),command=self.Registation_window)
        self.btnRegistation.grid(row=0,column=0)
        self.btnRestaurant = Button(self.Loginframe3,width=17,text='Working System', state=DISABLED,
                                  font=('arial',20,'bold'),command=self.Working_window)
        self.btnRestaurant.grid(row=0, column=1,pady=8,padx=22)

        self.master.mainloop()
#==============================================================================================
    def Login_System(self):
        user=self.Username.get()
        psw=self.Password.get()
        with sqlite3.connect("test.db") as db:
            cursor=db.cursor()
            sql = 'SELECT * FROM Userinfo'
            cursor.execute(sql)
            rows = cursor.fetchall()
            flag=False
            if rows:
                for row in rows:
                    if row[1]==user and row[2]==psw:
                        flag=True
            if flag==True:
                self.btnRegistation.config(state=NORMAL)
                self.btnRestaurant.config(state=NORMAL)
            else:
                tkinter.messagebox.askyesno('Management System','You have entered invalid login info.')
                self.btnRegistation.config(state=NORMAL)
                self.btnRestaurant.config(state=DISABLED)
                self.Username.set('')
                self.Password.set('')
                self.txtUsername.focus()
    def Reset(self):
        self.btnRegistation.config(state=DISABLED)
        self.btnRestaurant.config(state=DISABLED)
        self.Username.set('')
        self.Password.set('')
        self.txtUsername.focus()

    def iExit(self):
        self.iExit= tkinter.messagebox.askyesno('Management System','confirm you want to exit')
        if self.iExit>0:
            self.master.destroy()
            return

#==============================================================================================

    def Registation_window(self):
        self.newWindow = Toplevel(self.master)
        self.app =Window2(self.newWindow)

    def Working_window(self):
        self.master.destroy()
        workingPage()



class Window2:
    def __init__(self,master):
        pass

if __name__=='__main__':
    main()
