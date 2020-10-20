#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess
import platform


class Application(Frame):
    """
        Canvas with a top configuration
        to place widgets label and
        buttons.
    """
    def __init__(self, boss=None):
        Frame.__init__(self, borderwidth=5, bg='DodgerBlue4', padx=20, pady=20, relief=GROOVE)
        self.master.title('CLIMATE BOARD - Developed by ko@l@tr33 - 2020')

        # ScrollCanvas limite de la zone à parcourir avec la barre
        self.can = Canvas(self, width=1250, height=800, bg='aquamarine')
        self.frame = Frame(self.can)

        self.can.pack(side=LEFT, fill=BOTH, expand=YES)
        self.can.create_window((4,4), window=self.frame, anchor=NW, tags="self.frame")
        # Insertion of picture
        self.photo = PhotoImage(file='./picgif/bg.png')
        self.item = self.can.create_image(625, 400, image=self.photo)
        self.can.pack(side=LEFT, fill=BOTH, expand=YES)

        self.top = Frame(self.can, bg='turquoise3')
        self.top2 = Frame(self.can, bg='turquoise3')
        self.top3 = Frame(self.can, bg='aquamarine')
        self.top4 = Frame(self.can, bg='aquamarine')
        self.top5 = Frame(self.can, bg='turquoise3')
        self.top6 = Frame(self.can, bg='aquamarine')
        self.bottom = Frame(self.can)
        self.top.pack(side=TOP, pady=2)
        self.top2.pack(side=TOP, pady=2)
        self.top3.pack(side=TOP, pady=2)
        self.top4.pack(side=TOP, pady=2)
        self.top5.pack(side=TOP, pady=2)
        self.top6.pack(side=TOP, pady=2)
        self.bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

        # Label title
        self.label=Label(self.can, text="CLIMATE BOARD", font='Times 22 bold',
            fg='navy', bg='turquoise3')
        self.label.pack(in_=self.top, side=LEFT, padx=5, pady=10)

        def tempJanuary():
            try:
                if os.path.getsize('./01-january/plot_january.py'):
                    subprocess.run('./01-january/plot_january.py', check=True)
            except FileNotFoundError as no_file:
                print("+ January file doesn't exist !", no_file)
                messagebox.showwarning("WARNING", "January file doesn't exist !")

        def tempFebruary():
            try:
                if os.path.getsize('./02-february/plot_feb.py'):
                    subprocess.run('./02-february/plot_feb.py', check=True)
            except FileNotFoundError as no_file2:
                print("+ February file doesn't exist !", no_file2)
                messagebox.showwarning("WARNING", "February file doesn't exist !")

        def tempMarch():
            try:
                if os.path.getsize('./03-march/plot_mar.py'):
                    subprocess.run('./03-march/plot_mar.py', check=True)
            except FileNotFoundError as no_file3:
                print("+ March file doesn't exist !", no_file3)
                messagebox.showwarning("WARNING", "March file doesn't exist !")

        def tempApril():
            try:
                if os.path.getsize('./04-april/plot_april.py'):
                    subprocess.run('./04-april/plot_april.py', check=True)
            except FileNotFoundError as no_file4:
                print("+ April file doesn't exist !", no_file4)
                messagebox.showwarning("WARNING", "April file doesn't exist !")

        def tempMay():
            try:
                if os.path.getsize('./05-may/plot_may.py'):
                    subprocess.run('./05-may/plot_may.py', check=True)
            except FileNotFoundError as no_file:
                print("+ May file doesn't exist !", no_file)
                messagebox.showwarning("WARNING", "May file doesn't exist !")

        def tempJune():
            try:
                if os.path.getsize('./06-june/plot_june.py'):
                    subprocess.run('./06-june/plot_june.py', check=True)
            except FileNotFoundError as no_file5:
                print("+ June file doesn't exist !", no_file5)
                messagebox.showwarning("WARNING", "June file doesn't exist !")

        def tempJuly():
            try:
                if os.path.getsize('./07-july/plot_july.py'):
                    subprocess.run('./07-july/plot_july.py', check=True)
            except FileNotFoundError as no_file6:
                print("+ July file doesn't exist !", no_file6)
                messagebox.showwarning("WARNING", "July file doesn't exist !")

        def tempAugust():
            try:
                if os.path.getsize('./08-august/plot_august.py'):
                    subprocess.run('./08-august/plot_august.py', check=True)
            except FileNotFoundError as no_file7:
                print("+ August file doesn't exist !", no_file7)
                messagebox.showwarning("WARNING", "August file doesn't exist !")

        def tempSeptember():
            try:
                if os.path.getsize('./09-september/plot_sept.py'):
                    subprocess.run('./09-september/plot_sept.py', check=True)
            except FileNotFoundError as no_file8:
                print("+ September file doesn't exist !", no_file8)
                messagebox.showwarning("WARNING", "September file doesn't exist !")

        def tempOctober():
            try:
                if os.path.getsize(''):
                    subprocess.run('', check=True)
            except FileNotFoundError as no_file9:
                print("+ October file doesn't exist !", no_file9)
                messagebox.showwarning("WARNING", "October file doesn't exist !")

        def tempNovember():
            try:
                if os.path.getsize(''):
                    subprocess.run('', check=True)
            except FileNotFoundError as no_file10:
                print("+ November file doesn't exist !", no_file10)
                messagebox.showwarning("WARNING", "November file doesn't exist !")

        def tempDecember():
            try:
                if os.path.getsize(''):
                    subprocess.run('', check=True)
            except FileNotFoundError as no_file11:
                print("+ December file doesn't exist !", no_file11)
                messagebox.showwarning("WARNING", "December file doesn't exist !")

        # Label temp
        self.labelbot=Label(self.can, text="Temperatures for 2011-2016-2020", font='Times 18 bold',
            fg='RoyalBlue3', bg='aquamarine')
        self.labelbot.pack(in_=self.top2, side=LEFT, pady=10)

        # Button for January
        self.buttonJan = Button(self.can, text='January', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempJanuary)
        self.buttonJan.pack(in_=self.top3, side=LEFT, padx=10, pady=10)

        # Button for February
        self.buttonFeb = Button(self.can, text='February', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempFebruary)
        self.buttonFeb.pack(in_=self.top3, side=LEFT, padx=10, pady=10)

        # Button for March
        self.buttonMar = Button(self.can, text='March', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempMarch)
        self.buttonMar.pack(in_=self.top3, side=LEFT, padx=10, pady=10)

        # Button for April
        self.buttonApr = Button(self.can, text='April', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempApril)
        self.buttonApr.pack(in_=self.top3, side=LEFT, padx=10, pady=10)

        # Button for May
        self.buttonMay = Button(self.can, text='May', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempMay)
        self.buttonMay.pack(in_=self.top3, side=LEFT, padx=10, pady=10)

        # Button for June
        self.buttonJun = Button(self.can, text='June', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempJune)
        self.buttonJun.pack(in_=self.top3, side=LEFT, padx=10, pady=10)

        # Button for July
        self.buttonJuly = Button(self.can, text='July', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempJuly)
        self.buttonJuly.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        # Button for August
        self.buttonAug = Button(self.can, text='August', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempAugust)
        self.buttonAug.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        # Button for September
        self.buttonSept = Button(self.can, text='September', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempSeptember)
        self.buttonSept.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        # Button for October
        self.buttonOct = Button(self.can, text='October', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempOctober)
        self.buttonOct.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        # Button for November
        self.buttonNov = Button(self.can, text='November', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempNovember)
        self.buttonNov.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        # Button for October
        self.buttonDecember = Button(self.can, text='December', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempDecember)
        self.buttonDecember.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        # Label temp
        self.labelbot2=Label(self.can, text="Temperatures and precipitations 2011-2016-2020", 
            font='Times 18 bold', fg='RoyalBlue3', bg='aquamarine')
        self.labelbot2.pack(in_=self.top5, side=LEFT, pady=10)

        def tempPrecipit():
            """
                For openning file at pdf 
                format with a bit prog-sys code.
                For Linux, Windows and MAC.
            """
            becall = platform.system()
            print(platform.system())
            
            if becall == 'Linux':
                os.system('gio open "./average_temp/av_tempreci.png"') # Linux
            elif becall =='Darwin':
                subprocess.call('open', './average_temp/av_tempreci.png' ) # Mac
            else:
                os.startfile('./average_temp/av_tempreci.png') # Windows

        def temperAverTemper():
            """
                To display average of temperatures 2011-2016-2020
            """
            try:
                if os.path.getsize('./average_temp/ws_avty.py'):
                    subprocess.run('./average_temp/ws_avty.py', check=True)
            except FileNotFoundError as no_fileAT:
                print("+ December file doesn't exist !", no_fileAT)
                messagebox.showwarning("WARNING", "December file doesn't exist !")

        def temperAverPrecipit():
            """
                To display average of precipitations 2011-2016-2020
            """
            try:
                if os.path.getsize('./average_temp/ws_totalprecipit.py'):
                    subprocess.run('./average_temp/ws_totalprecipit.py', check=True)
            except FileNotFoundError as no_fileAP:
                print("+ File doesn't exist !", no_fileAP)
                messagebox.showwarning("WARNING", "File doesn't exist !")

        # Button for temprecipit
        self.buttonTemp = Button(self.can, text='6-tabs', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempPrecipit)
        self.buttonTemp.pack(in_=self.top6, side=LEFT, padx=10, pady=10)

        # Button to compare temperatures
        self.buttonAvTemp = Button(self.can, text='Av-Temp.', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=temperAverTemper)
        self.buttonAvTemp.pack(in_=self.top6, side=LEFT, padx=10, pady=10)

        # Button to compare precipit
        self.buttonAvPreci = Button(self.can, text='Av-Preci.', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=temperAverPrecipit)
        self.buttonAvPreci.pack(in_=self.top6, side=LEFT, padx=10, pady=10)

        # Button to quit
        self.buttonQuit = Button(self.can, text='Quit', width=8, bd=3,
            fg='white', bg='DodgerBlue2', highlightbackground='darkblue',
            activeforeground='red',
            activebackground='light blue', command=quit)
        self.buttonQuit.pack(side=RIGHT, padx=10, pady=10)
        self.pack()

if __name__=='__main__':
    app = Application()
    app.mainloop()
