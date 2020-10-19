#!/usr/bin/python3
# -*- encoding:utf-8 -*-


from tkinter import *
from tkinter import messagebox
import os
import subprocess


class Application(Frame):
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
        self.top4 = Frame(self.can, bg='turquoise3')
        self.bottom = Frame(self.can)
        self.top.pack(side=TOP, pady=2)
        self.top2.pack(side=TOP, pady=2)
        self.top3.pack(side=TOP, pady=2)
        self.top4.pack(side=TOP, pady=2)
        self.bottom.pack(side=BOTTOM, fill=BOTH, expand=YES)

        def tempJanuary():
            try:
                if os.path.getsize(''):
                    subprocess.run('', check=True)
            except FileNotFoundError as no_file:
                print("+ January file doesn't exist !")
                messagebox.showinfo("INFO", "January file doesn't exist")

        # Label title
        self.label=Label(self.can, text="CLIMATE BOARD", font='Times 22 bold',
            fg='navy', bg='turquoise3')
        self.label.pack(in_=self.top, side=LEFT, padx=5, pady=10)

        # Label temp
        self.labelbot=Label(self.can, text="Temperatures for 2011-2016-2020", font='Times 18 bold',
            fg='red', bg='aquamarine')
        self.labelbot.pack(in_=self.top2, side=LEFT, pady=10)

        # Label temp
        self.labelbot2=Label(self.can, text="Precipitations for month 2011-2016-2020", font='Times 18 bold',
            fg='red', bg='aquamarine')
        self.labelbot2.pack(in_=self.top2, side=LEFT, pady=10)

        # Label temp precipit
        self.labelbot3=Label(self.can, text="Temperatures and precipitations per year", 
            font='Times 18 bold', fg='red', bg='aquamarine')
        self.labelbot3.pack(in_=self.top3, side=LEFT, pady=10)

        # Label temp precipit
        self.labelbot4=Label(self.can, text="Temperatures and precipitations per year", 
            font='Times 18 bold', fg='red', bg='aquamarine')
        self.labelbot4.pack(in_=self.top3, side=LEFT, pady=10)

        # Button for January
        self.buttonSearch = Button(self.can, text='January', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=tempJanuary)
        self.buttonSearch.pack(in_=self.top4, side=LEFT, padx=10, pady=10)

        """
        # Button for January
        self.buttonSearch = Button(self.can, text='February', width=8, bd=3,
            fg='navy', bg='aquamarine', highlightbackground='darkblue',
            activeforeground='white', activebackground='light blue',
            command=)
        self.buttonSearch.pack(in_=self.top4, side=LEFT, padx=10, pady=10)
        """

        # Button to quit
        self.buttonQuit = Button(self.can, text='Quit', width=8, bd=3,
            fg='white', bg='DodgerBlue2', highlightbackground='darkblue',
            activeforeground='red',
            activebackground='light blue', command=quit)
        self.buttonQuit.pack(in_=self.top4, side=LEFT, padx=10, pady=10)
        self.pack()

if __name__=='__main__':
    app = Application()
    app.mainloop()
