#Author:YZW
import sqlite3
from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

class workingPage:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Restaurant Management System')
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='Cadet Blue')


        self.Tops=Frame(self.root,bg='Cadet Blue',bd=18,pady=5,relief=RIDGE)
        self.Tops.pack(side=TOP)
        self.lblTtile = Label(self.Tops, font=('arial', 60, 'bold'), text='Restaurant Management System', bd=21,
                              bg='Cadet Blue', fg='cornsilk', justify='center')
        self.lblTtile.grid(row=0, column=0)


        self.ReceiptCal_F = Frame(self.root, bg='powder Blue', bd=10, relief=RIDGE)
        self.ReceiptCal_F.pack(side=RIGHT)

        self.Button_F=Frame(self.ReceiptCal_F, bg='powder Blue', bd=3, relief=RIDGE)
        self.Button_F.pack(side=BOTTOM)
        self.Cal_F = Frame(self.ReceiptCal_F, bg='powder Blue', bd=6, relief=RIDGE)
        self.Cal_F.pack(side=TOP)
        self.Receipt_F = Frame(self.ReceiptCal_F, bg='powder Blue', bd=4, relief=RIDGE)
        self.Receipt_F.pack(side=BOTTOM)


        self.MenuFrame = Frame(self.root, bg='Cadet Blue', bd=10, relief=RIDGE)
        self.MenuFrame.pack(side=LEFT)

        self.Cost_F = Frame(self.MenuFrame, bg='powder Blue', bd=4)
        self.Cost_F.pack(side=BOTTOM)
        self.Drinks_F = Frame(self.MenuFrame, bg='Cadet Blue', bd=10)
        self.Drinks_F.pack(side=TOP)

        self.Drinks_F = Frame(self.MenuFrame, bg='powder Blue', bd=10, relief=RIDGE)
        self.Drinks_F.pack(side=LEFT)
        self.Cake_F = Frame(self.MenuFrame, bg='powder Blue', bd=10, relief=RIDGE)
        self.Cake_F.pack(side=RIGHT)

        var1=IntVar()
        var2=IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()

        DateofOrder=StringVar()
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()
        CostofCakes=StringVar()
        CostofDrinks=StringVar()
        ServiceCharge=StringVar()

        #text_Input = StringVar()
        #global operator
        #operator=''
        E_Latta=StringVar()
        E_Espresso=StringVar()
        E_Iced_Latta=StringVar()
        E_Vale_Coffee=StringVar()
        E_Cappuccino=StringVar()
        E_African_Coffee=StringVar()
        E_Iced_Cappuccino=StringVar()
        E_American_Coffee=StringVar()


        E_SchoolCake=StringVar()
        E_Sunny_AO_Cake=StringVar()
        E_Jonathan_YO_Cake=StringVar()
        E_West_African_Cake=StringVar()
        E_Lagos_Chocolate_Cake=StringVar()
        E_Kilburn_Chocolate_Cake=StringVar()
        E_Carlton_Hill_Cake=StringVar()
        E_Queen_Park_Cake=StringVar()

        E_Latta.set('0')
        E_Espresso.set('0')
        E_Iced_Latta.set('0')
        E_Vale_Coffee.set('0')
        E_Cappuccino.set('0')
        E_African_Coffee.set('0')
        E_Iced_Cappuccino.set('0')
        E_American_Coffee.set('0')

        E_SchoolCake.set('0')
        E_Sunny_AO_Cake.set('0')
        E_Jonathan_YO_Cake.set('0')
        E_West_African_Cake.set('0')
        E_Lagos_Chocolate_Cake.set('0')
        E_Kilburn_Chocolate_Cake.set('0')
        E_Carlton_Hill_Cake.set('0')
        E_Queen_Park_Cake.set('0')

        DateofOrder.set(time.strftime('%d/%m/%Y'))


# ================================checkbox function=====================================================================
        def chkLatta():
            if (var1.get() == 1):
                self.txtLatta.configure(state=NORMAL)
                self.txtLatta.focus()
                self.txtLatta.delete('0', END)
                E_Latta.set('')
            elif (var1.get() == 0):
                self.txtLatta.configure(state=DISABLED)
                E_Latta.set('')

        def Espresso():
            if (var2.get() == 1):
                self.txtEspresso.configure(state=NORMAL)
                self.txtEspresso.focus()
                self.txtEspresso.delete('0', END)
                E_Espresso.set('')
            elif (var2.get() == 0):
                self.txtEspresso.configure(state=DISABLED)
                E_Espresso.set('')

        def Iced_Latta():
            if (var3.get() == 1):
                self.txtIced_Latta.configure(state=NORMAL)
                self.txtIced_Latta.focus()
                self.txtIced_Latta.delete('0', END)
                E_Iced_Latta.set('')
            elif (var3.get() == 0):
                self.txtIced_Latta.configure(state=DISABLED)
                E_Iced_Latta.set('')

        def Vale_Coffee():
            if (var4.get() == 1):
                self.txtVale_Coffee.configure(state=NORMAL)
                self.txtVale_Coffee.focus()
                self.txtVale_Coffee.delete('0', END)
                E_Vale_Coffee.set('')
            elif (var4.get() == 0):
                self.txtLatta.configure(state=DISABLED)
                E_Vale_Coffee.set('')

        def Cappuccino():
            if (var5.get() == 1):
                self.txtCappuccino.configure(state=NORMAL)
                self.txtCappuccino.focus()
                self.txtCappuccino.delete('0', END)
                E_Cappuccino.set('')
            elif (var5.get() == 0):
                self.txtCappuccino.configure(state=DISABLED)
                E_Cappuccino.set('')

        def African_Coffee():
            if (var6.get() == 1):
                self.txtAfrican_Coffee.configure(state=NORMAL)
                self.txtAfrican_Coffee.focus()
                self.txtAfrican_Coffee.delete('0', END)
                E_African_Coffee.set('')
            elif (var6.get() == 0):
                self.txtAfrican_Coffee.configure(state=DISABLED)
                E_African_Coffee.set('')

        def American_Coffee():
            if (var7.get() == 1):
                self.txtAmerican_Coffee.configure(state=NORMAL)
                self.txtAmerican_Coffee.focus()
                self.txtAmerican_Coffee.delete('0', END)
                E_American_Coffee.set('')
            elif (var7.get() == 0):
                self.txtAmerican_Coffee.configure(state=DISABLED)
                E_American_Coffee.set('')

        def Iced_Cappuccino():
            if (var8.get() == 1):
                self.txtIced_Cappuccino.configure(state=NORMAL)
                self.txtIced_Cappuccino.focus()
                self.txtIced_Cappuccino.delete('0', END)
                E_Iced_Cappuccino.set('')
            elif (var8.get() == 0):
                self.txtIced_Cappuccino.configure(state=DISABLED)
                E_Iced_Cappuccino.set('')

#================================drinks=====================================================================
        self.Latta=Checkbutton(self.Drinks_F,text='Latta',variable=var1,onvalue=1,offvalue=0,command=chkLatta,
                               font=('arial', 16, 'bold'),bg='powder Blue').grid(row=0,sticky=W)
        self.Espresso = Checkbutton(self.Drinks_F, text='Espresso', variable=var2, onvalue=1, offvalue=0,command=Espresso,
                                 font=('arial', 16, 'bold'), bg='powder Blue').grid(row=1, sticky=W)
        self.Iced_Latta = Checkbutton(self.Drinks_F, text='Iced_Latta', variable=var3, onvalue=1, offvalue=0,command=Iced_Latta,
                                 font=('arial', 16, 'bold'), bg='powder Blue').grid(row=2, sticky=W)
        self.Vale_Coffee = Checkbutton(self.Drinks_F, text='Vale_Coffee', variable=var4, onvalue=1, offvalue=0,command=Vale_Coffee,
                                 font=('arial', 16, 'bold'), bg='powder Blue').grid(row=3, sticky=W)
        self.Cappuccino = Checkbutton(self.Drinks_F, text='Cappuccino', variable=var5, onvalue=1, offvalue=0,command=Cappuccino,
                                 font=('arial', 16, 'bold'), bg='powder Blue').grid(row=4, sticky=W)
        self.African_Coffee = Checkbutton(self.Drinks_F, text='African_Coffee', variable=var6, onvalue=1, offvalue=0,command=African_Coffee,
                                 font=('arial', 16, 'bold'), bg='powder Blue').grid(row=5, sticky=W)
        self.American_Coffee = Checkbutton(self.Drinks_F, text='American_Coffee', variable=var7, onvalue=1, offvalue=0,command=American_Coffee,
                                 font=('arial', 16, 'bold'), bg='powder Blue').grid(row=6, sticky=W)
        self.Iced_Cappuccino = Checkbutton(self.Drinks_F, text='Iced_Cappuccino', variable=var8, onvalue=1, offvalue=0,command=E_Iced_Cappuccino,
                                 font=('arial', 16, 'bold'), bg='powder Blue').grid(row=7, sticky=W)
#================================Entry Box for Drinks=====================================================================
        self.txtLatta=Entry(self.Drinks_F,font=('arial', 16, 'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Latta)
        self.txtLatta.grid(row=0,column=1)
        self.txtEspresso = Entry(self.Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', state='disabled',textvariable=E_Espresso)
        self.txtEspresso.grid(row=1, column=1)
        self.txtIced_Latta = Entry(self.Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', state='disabled',textvariable=E_Iced_Latta)
        self.txtIced_Latta.grid(row=2, column=1)
        self.txtVale_Coffee = Entry(self.Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', state='disabled',textvariable=E_Vale_Coffee)
        self.txtVale_Coffee.grid(row=3, column=1)
        self.txtCappuccino = Entry(self.Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', state='disabled',textvariable=E_Cappuccino)
        self.txtCappuccino.grid(row=4, column=1)
        self.txtAfrican_Coffee = Entry(self.Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', state='disabled',textvariable=E_African_Coffee)
        self.txtAfrican_Coffee.grid(row=5, column=1)
        self.txtAmerican_Coffee = Entry(self.Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', state='disabled',textvariable=E_American_Coffee)
        self.txtAmerican_Coffee.grid(row=6, column=1)
        self.txtIced_Cappuccino = Entry(self.Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', state='disabled',textvariable=E_Iced_Cappuccino)
        self.txtIced_Cappuccino.grid(row=7, column=1)

#================================checkbox function=====================================================================
        def SchoolCake():
            if (var9.get() == 1):
                self.txtSchoolCake.configure(state=NORMAL)
                self.txtSchoolCake.focus()
                self.txtSchoolCake.delete('0', END)
                E_SchoolCake.set('')
            elif (var9.get() == 0):
                self.txtSchoolCake.configure(state=DISABLED)
                E_SchoolCake.set('')

        def Sunny_AO_Cake():
            if (var10.get() == 1):
                self.txtSunny_AO_Cake.configure(state=NORMAL)
                self.txtSunny_AO_Cake.focus()
                self.txtSunny_AO_Cake.delete('0', END)
                E_Sunny_AO_Cake.set('')
            elif (var10.get() == 0):
                self.txtSunny_AO_Cake.configure(state=DISABLED)
                E_Sunny_AO_Cake.set('')

        def Jonathan_YO_Cake():
            if (var11.get() == 1):
                self.txtJonathan_YO_Cake.configure(state=NORMAL)
                self.txtJonathan_YO_Cake.focus()
                self.txtJonathan_YO_Cake.delete('0', END)
                E_Jonathan_YO_Cake.set('')
            elif (var11.get() == 0):
                self.txtJonathan_YO_Cake.configure(state=DISABLED)
                E_Jonathan_YO_Cake.set('')

        def West_African_Cake():
            if (var12.get() == 1):
                self.txtWest_African_Cake.configure(state=NORMAL)
                self.txtWest_African_Cake.focus()
                self.txtWest_African_Cake.delete('0', END)
                E_West_African_Cake.set('')
            elif (var12.get() == 0):
                self.txtWest_African_Cake.configure(state=DISABLED)
                E_West_African_Cake.set('')

        def Lagos_Chocolate_Cake():
            if (var13.get() == 1):
                self.txtLagos_Chocolate_Cake.configure(state=NORMAL)
                self.txtLagos_Chocolate_Cake.focus()
                self.txtLagos_Chocolate_Cake.delete('0', END)
                E_Lagos_Chocolate_Cake.set('')
            elif (var13.get() == 0):
                self.txtLagos_Chocolate_Cake.configure(state=DISABLED)
                E_Lagos_Chocolate_Cake.set('')

        def Kilburn_Chocolate_Cake():
            if (var14.get() == 1):
                self.txtKilburn_Chocolate_Cake.configure(state=NORMAL)
                self.txtKilburn_Chocolate_Cake.focus()
                self.txtKilburn_Chocolate_Cake.delete('0', END)
                E_Kilburn_Chocolate_Cake.set('')
            elif (var14.get() == 0):
                self.txtKilburn_Chocolate_Cake.configure(state=DISABLED)
                E_Kilburn_Chocolate_Cake.set('')
        def Carlton_Hill_Cake():
            if (var15.get() == 1):
                self.txtCarlton_Hill_Cake.configure(state=NORMAL)
                self.txtCarlton_Hill_Cake.focus()
                self.txtCarlton_Hill_Cake.delete('0', END)
                E_Carlton_Hill_Cake.set('')
            elif (var15.get() == 0):
                self.txtCarlton_Hill_Cake.configure(state=DISABLED)
                E_Carlton_Hill_Cake.set('')
        def Queen_Park_Cake():
            if (var16.get() == 1):
                self.txtQueen_Park_Cake.configure(state=NORMAL)
                self.txtQueen_Park_Cake.focus()
                self.txtQueen_Park_Cake.delete('0', END)
                E_Queen_Park_Cake.set('')
            elif (var16.get() == 0):
                self.txtLatta.configure(state=DISABLED)
                E_Queen_Park_Cake.set('')
#================================Cakes=====================================================================
        self.SchoolCake = Checkbutton(self.Cake_F, text='SchoolCake', variable=var9, onvalue=1, offvalue=0,command=SchoolCake,
                                 font=('arial', 16, 'bold'), bg='powder Blue').grid(row=0, sticky=W)
        self.Sunny_AO_Cake = Checkbutton(self.Cake_F, text='Sunny_AO_Cake', variable=var10, onvalue=1, offvalue=0,command=Sunny_AO_Cake,
                                    font=('arial', 16, 'bold'), bg='powder Blue').grid(row=1, sticky=W)
        self.Jonathan_YO_Cake = Checkbutton(self.Cake_F, text='Jonathan_YO_Cake', variable=var11, onvalue=1, offvalue=0,command=Jonathan_YO_Cake,
                                      font=('arial', 16, 'bold'), bg='powder Blue').grid(row=2, sticky=W)
        self.West_African_Cake = Checkbutton(self.Cake_F, text='West_African_Cake', variable=var12, onvalue=1, offvalue=0,command=West_African_Cake,
                                       font=('arial', 16, 'bold'), bg='powder Blue').grid(row=3, sticky=W)
        self.Lagos_Chocolate_Cake = Checkbutton(self.Cake_F, text='Lagos_Chocolate_Cake', variable=var13, onvalue=1, offvalue=0,command=Lagos_Chocolate_Cake,
                                      font=('arial', 16, 'bold'), bg='powder Blue').grid(row=4, sticky=W)
        self.Kilburn_Chocolate_Cake = Checkbutton(self.Cake_F, text='Kilburn_Chocolate_Cake', variable=var14, onvalue=1, offvalue=0,command=Kilburn_Chocolate_Cake,
                                          font=('arial', 16, 'bold'), bg='powder Blue').grid(row=5, sticky=W)
        self.Carlton_Hill_Cake = Checkbutton(self.Cake_F, text='Carlton_Hill_Cake', variable=var15, onvalue=1, offvalue=0,command=Carlton_Hill_Cake,
                                           font=('arial', 16, 'bold'), bg='powder Blue').grid(row=6, sticky=W)
        self.Queen_Park_Cake = Checkbutton(self.Cake_F, text='Queen_Park_Cake', variable=var16, onvalue=1, offvalue=0,command=Queen_Park_Cake,
                                           font=('arial', 16, 'bold'), bg='powder Blue').grid(row=7, sticky=W)
#================================Entry Box for Cakes=====================================================================
        self.txtSchoolCake = Entry(self.Cake_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_SchoolCake,state='disabled')
        self.txtSchoolCake.grid(row=0, column=1)
        self.txtSunny_AO_Cake = Entry(self.Cake_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Sunny_AO_Cake,
                                 state='disabled')
        self.txtSunny_AO_Cake.grid(row=1, column=1)
        self.txtJonathan_YO_Cake = Entry(self.Cake_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Jonathan_YO_Cake,
                                   state='disabled')
        self.txtJonathan_YO_Cake.grid(row=2, column=1)
        self.txtWest_African_Cake = Entry(self.Cake_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_African_Coffee,
                                    state='disabled')
        self.txtWest_African_Cake.grid(row=3, column=1)
        self.txtLagos_Chocolate_Cake = Entry(self.Cake_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Lagos_Chocolate_Cake,
                                   state='disabled')
        self.txtLagos_Chocolate_Cake.grid(row=4, column=1)
        self.txtKilburn_Chocolate_Cake = Entry(self.Cake_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Kilburn_Chocolate_Cake,
                                       state='disabled')
        self.txtKilburn_Chocolate_Cake.grid(row=5, column=1)
        self.txtCarlton_Hill_Cake = Entry(self.Cake_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Carlton_Hill_Cake,
                                        state='disabled')
        self.txtCarlton_Hill_Cake.grid(row=6, column=1)
        self.txtQueen_Park_Cake = Entry(self.Cake_F, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',textvariable=E_Queen_Park_Cake,
                                        state='disabled')
        self.txtQueen_Park_Cake.grid(row=7, column=1)

#================================Total Cost=====================================================================
        self.lblCostofDrinks = Label(self.Cost_F, font=('arial', 14, 'bold'), text='Cost of Drinks',
                                     bg='powder Blue', fg='black')
        self.lblCostofDrinks.grid(row=0, column=0, sticky=W)
        self.txtCostofDrinks = Entry(self.Cost_F, font=('arial', 14, 'bold'), bg='white', bd=7, insertwidth=2,textvariable=CostofDrinks,
                                     justify='right')
        self.txtCostofDrinks.grid(row=0, column=1)


        self.lblCostofCakes = Label(self.Cost_F, font=('arial', 14, 'bold'), text='Cost of Cakes',
                                     bg='powder Blue', fg='black')
        self.lblCostofCakes.grid(row=1, column=0, sticky=W)
        self.txtCostofCakes = Entry(self.Cost_F, font=('arial', 14, 'bold'), bg='white', bd=7, insertwidth=2,justify='right',textvariable=CostofCakes)
        self.txtCostofCakes.grid(row=1, column=1)


        self.ServiceCharge = Label(self.Cost_F, font=('arial', 14, 'bold'), text='Service Charge',
                                    bg='powder Blue', fg='black')
        self.ServiceCharge.grid(row=2, column=0, sticky=W)
        self.txtServiceCharge = Entry(self.Cost_F, font=('arial', 14, 'bold'), bg='white', bd=7, insertwidth=2,justify='right',textvariable=ServiceCharge)
        self.txtServiceCharge.grid(row=2, column=1)


# ================================Payment=====================================================================
        self.lblPaidTax = Label(self.Cost_F, font=('arial', 14, 'bold'), text='\tPaid Tax\t', bd=7,
                                     bg='powder Blue', fg='black')
        self.lblPaidTax.grid(row=0, column=2, sticky=W)
        self.txtPaidTax = Entry(self.Cost_F, font=('arial', 14, 'bold'), bg='white', bd=7, insertwidth=2,
                                     justify='right',textvariable=PaidTax)
        self.txtPaidTax.grid(row=0, column=3)


        self.lblSubTotal = Label(self.Cost_F, font=('arial', 14, 'bold'), text='\tSub Total',bd=7,
                                     bg='powder Blue', fg='black')
        self.lblSubTotal.grid(row=1, column=2, sticky=W)
        self.txtSubTotal = Entry(self.Cost_F, font=('arial', 14, 'bold'), bg='white', bd=7, insertwidth=2,
                                     justify='right',textvariable=SubTotal)
        self.txtSubTotal.grid(row=1, column=3)


        self.lblTotalCost = Label(self.Cost_F, font=('arial', 14, 'bold'), text='\tTotal Cost',bd=7,
                                     bg='powder Blue', fg='black')
        self.lblTotalCost.grid(row=2, column=2, sticky=W)
        self.txtTotalCost = Entry(self.Cost_F, font=('arial', 14, 'bold'), bg='white', bd=7, insertwidth=2,
                                     justify='right',textvariable=TotalCost)
        self.txtTotalCost.grid(row=2, column=3)

#================================Receipt=====================================================================
        def Receipt():
            self.Receipt.delete('1.0',END)
            x=random.randint(10903,609235)
            randomRef=str(x)
            Receipt_Ref.set('BILL'+randomRef)

            self.Receipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get()+'\t'+DateofOrder.get()+'\n')
            self.Receipt.insert(END, 'Item Ref:\t\t\t' +'Cost of Item\n')

            self.Receipt.insert(END, 'Latta Ref:\t\t\t' + E_Latta.get()+ '\n')
            self.Receipt.insert(END, 'Espresso Ref:\t\t\t' + E_Espresso.get() + '\n')
            self.Receipt.insert(END, 'Iced_Latta Ref:\t\t\t' + E_Iced_Latta.get() + '\n')
            self.Receipt.insert(END, 'Vale_Coffee Ref:\t\t\t' + E_Vale_Coffee.get() + '\n')
            self.Receipt.insert(END, 'Cappuccino Ref:\t\t\t' + E_Cappuccino.get() + '\n')
            self.Receipt.insert(END, 'African_Coffee Ref:\t\t\t' + E_African_Coffee.get() + '\n')
            self.Receipt.insert(END, 'Iced_Cappuccino Ref:\t\t\t' + E_Iced_Cappuccino.get() + '\n')
            self.Receipt.insert(END, 'American_Coffee Ref:\t\t\t' + E_American_Coffee.get() + '\n')

            self.Receipt.insert(END, 'SchoolCake Ref:\t\t\t' + E_SchoolCake.get() + '\n')
            self.Receipt.insert(END, 'Sunny_AO_Cake Ref:\t\t\t' + E_Sunny_AO_Cake.get() + '\n')
            self.Receipt.insert(END, 'Jonathan_YO_Cake Ref:\t\t\t' + E_Jonathan_YO_Cake.get() + '\n')
            self.Receipt.insert(END, 'West_African_Cake Ref:\t\t\t' + E_West_African_Cake.get() + '\n')
            self.Receipt.insert(END, 'Lagos_Chocolate_Cake Ref:\t\t\t' + E_Lagos_Chocolate_Cake.get() + '\n')
            self.Receipt.insert(END, 'Kilburn_Chocolate_Cake Ref:\t\t\t' + E_Kilburn_Chocolate_Cake.get() + '\n')
            self.Receipt.insert(END, 'Carlton_Hill_Cake Ref:\t\t\t' + E_Carlton_Hill_Cake.get() + '\n')
            self.Receipt.insert(END, 'Queen_Park_Cake Ref:\t\t\t' + E_Queen_Park_Cake.get() + '\n')


#================================Receipt=====================================================================
        self.Receipt=Text(self.Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial', 12, 'bold'))
        self.Receipt.grid(row=0,column=0)

#================================Function=====================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno('Management System', 'confirm you want to exit')
            if iExit > 0:
                self.root.destroy()
                return

        def Reset():
            operator=''
            DateofOrder.set('')
            Receipt_Ref.set('')
            PaidTax.set('')
            SubTotal.set('')
            TotalCost.set('')
            CostofCakes.set('')
            CostofDrinks.set('')
            ServiceCharge.set('')

            E_Latta.set('0')
            E_Espresso.set('0')
            E_Iced_Latta.set('0')
            E_Vale_Coffee.set('0')
            E_Cappuccino.set('0')
            E_African_Coffee.set('0')
            E_Iced_Cappuccino.set('0')
            E_American_Coffee.set('0')

            E_SchoolCake.set('0')
            E_Sunny_AO_Cake.set('0')
            E_Jonathan_YO_Cake.set('0')
            E_West_African_Cake.set('0')
            E_Lagos_Chocolate_Cake.set('0')
            E_Kilburn_Chocolate_Cake.set('0')
            E_Carlton_Hill_Cake.set('0')
            E_Queen_Park_Cake.set('0')

            var1.set('0')
            var2.set('0')
            var3.set('0')
            var4.set('0')
            var5.set('0')
            var6.set('0')
            var7.set('0')
            var8.set('0')
            var9.set('0')
            var10.set('0')
            var11.set('0')
            var12.set('0')
            var13.set('0')
            var14.set('0')
            var15.set('0')
            var16.set('0')

            self.txtLatta.configure(state=DISABLED)
            self.txtAfrican_Coffee.configure(state=DISABLED)
            self.txtAmerican_Coffee.configure(state=DISABLED)
            self.txtCappuccino.configure(state=DISABLED)
            self.txtCarlton_Hill_Cake.configure(state=DISABLED)
            self.txtCostofCakes.configure(state=DISABLED)
            self.txtEspresso.configure(state=DISABLED)
            self.txtIced_Cappuccino.configure(state=DISABLED)
            self.txtIced_Latta.configure(state=DISABLED)
            self.txtJonathan_YO_Cake.configure(state=DISABLED)
            self.txtKilburn_Chocolate_Cake.configure(state=DISABLED)
            self.txtLagos_Chocolate_Cake.configure(state=DISABLED)
            self.txtQueen_Park_Cake.configure(state=DISABLED)
            self.txtSchoolCake.configure(state=DISABLED)
            self.txtSunny_AO_Cake.configure(state=DISABLED)
            self.txtVale_Coffee.configure(state=DISABLED)
            self.txtWest_African_Cake.configure(state=DISABLED)

        def CostofItem():
            Item1=float(E_Latta.get())
            Item2=float(E_Espresso.get())
            Item3= float(E_Iced_Latta.get())
            Item4 = float(E_Vale_Coffee.get())
            Item5 = float(E_Cappuccino.get())
            Item6 = float(E_American_Coffee.get())
            Item7 = float(E_African_Coffee.get())
            Item8 = float(E_Iced_Cappuccino.get())

            Item9 = float(E_SchoolCake.get())
            Item10 = float(E_Sunny_AO_Cake.get())
            Item11= float(E_Jonathan_YO_Cake.get())
            Item12= float(E_West_African_Cake.get())
            Item13= float(E_Lagos_Chocolate_Cake.get())
            Item14= float(E_Kilburn_Chocolate_Cake.get())
            Item15= float(E_Carlton_Hill_Cake.get())
            Item16= float(E_Queen_Park_Cake.get())

            priceofDrinks=(Item1+Item2+Item3+Item4+Item5+Item6+Item7+Item8)*3
            priceofCakes=(Item9+Item10+Item11+Item12+Item13+Item14+Item15+Item16)*2
            DrinksPrice='$'+str('%.2f'%(priceofDrinks))
            CakeskPrice = '$'+str('%.2f' % (priceofCakes))

            CostofDrinks.set(DrinksPrice)
            CostofCakes.set(CakeskPrice)

            SC='$'+str('%.2f'%(1.59))
            ServiceCharge.set(SC)
            SubTotalofItem='$'+str('%.2f'%(priceofDrinks+priceofCakes+1.59))
            SubTotal.set(SubTotalofItem)
            Tax='$'+str('%.2f'%((priceofDrinks+priceofCakes+1.59)*0.15))
            PaidTax.set(Tax)
            TT=(priceofDrinks+priceofCakes+1.59)*0.15
            TC='$'+str('%.2f'%(priceofDrinks+priceofCakes+1.59+TT))
            TotalCost.set(TC)



#================================Buttons=====================================================================
        btnTotal=Button(self.Button_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),command=CostofItem,
                        width=4,text='Total',bg='powder Blue').grid(row=0, column=0)
        btnReceipt = Button(self.Button_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),command=Receipt,
                          width=4, text='Receipt', bg='powder Blue').grid(row=0, column=1)
        btnReset = Button(self.Button_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                          width=4, text='Reset', bg='powder Blue',command=Reset).grid(row=0, column=2)
        btnExit = Button(self.Button_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                          width=4, text='Exit', bg='powder Blue',command=iExit).grid(row=0, column=3)
#================================Calculator Dispay=====================================================================

        def btnClick(numbers):
            global operator
            operator = operator + str(numbers)
            text_Input.set(operator)

        def btnClear():
            global operator
            operator = ''
            text_Input.set(operator)

        def btnEquals():
            global operator
            sumup = str(eval(operator))
            text_Input.set(sumup)
            operator = str(sumup)

        global text_Input
        text_Input= StringVar()
        global operator
        operator=''

        textDispaly = Entry(self.Cal_F, bg='white', width=45, bd=4, textvariable=text_Input,
                            font=('arial', 12, 'bold'), justify='right')
        textDispaly.grid(row=0, column=0, columnspan=4, pady=1)
        textDispaly.insert(0, '0')

        btn7 = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                      width=4, text='7', bg='powder Blue', command=lambda: btnClick(7)).grid(row=2, column=0)
        btn8 = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                      width=4, text='8', bg='powder Blue', command=lambda: btnClick(8)).grid(row=2, column=1)
        btn9 = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                      width=4, text='9', bg='powder Blue', command=lambda: btnClick(9)).grid(row=2, column=2)
        btnAdd = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                        width=4, text='+', bg='powder Blue', command=lambda: btnClick('+')).grid(row=2, column=3)

        btn4 = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                      width=4, text='4', bg='powder Blue', command=lambda: btnClick(4)).grid(row=3, column=0)
        btn5 = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                      width=4, text='5', bg='powder Blue', command=lambda: btnClick(5)).grid(row=3, column=1)
        btn6 = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                      width=4, text='6', bg='powder Blue', command=lambda: btnClick(6)).grid(row=3, column=2)
        btnSub = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                        width=4, text='-', bg='powder Blue', command=lambda: btnClick('-')).grid(row=3, column=3)

        btn1 = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                      width=4, text='1', bg='powder Blue', command=lambda: btnClick(1)).grid(row=4, column=0)
        btn2 = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                      width=4, text='2', bg='powder Blue', command=lambda: btnClick(2)).grid(row=4, column=1)
        btn3 = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                      width=4, text='3', bg='powder Blue', command=lambda: btnClick(3)).grid(row=4, column=2)
        btnMuti = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                         width=4, text='*', bg='powder Blue', command=lambda: btnClick('*')).grid(row=4, column=3)

        btn0 = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                      width=4, text='0', bg='powder Blue', command=lambda: btnClick(0)).grid(row=5, column=0)
        btnClear = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                          width=4, text='C', bg='powder Blue', command=btnClear).grid(row=5, column=1)
        btnEquals = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                           width=4, text='=', bg='powder Blue', command=btnEquals).grid(row=5, column=2)
        btnDiv = Button(self.Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial', 16, 'bold'),
                        width=4, text='/', bg='powder Blue', command=lambda: btnClick('/')).grid(row=5, column=3)




        self.root.mainloop()

if __name__=='__main__':
    workingPage()
