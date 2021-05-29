#CREATING A LANGUAGE TRANSLATER USING PYTHON googletrans MODULE:

import googletrans
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel,showinfo, showerror
import sys
import httpcore

class translater:

    def __init__(self,master):
        def enter(event):
            self.translate.config(bg='white',fg='black')

        def leave(event):
            self.translate.config(bg='green',fg='red')

        def translate1():

            english = self.text1.get('1.0',END)
            if len(english)<2:
                showerror('M-lANGTRANS','Please enter some text for translation!')
            else:
                if self.combobox.get()=='English to ASCII':
                    self.lang2.config(text='ASCII VALUE')
                    self.text2.delete('1.0', END)
                    for i in self.text1.get(1.0,END):
                        string = ord(i)
                        final = str(string)
                        if final[-2:]=='10':
                            new = final[:-2]
                            print(new,end='')
                        else:
                           self.text2.insert(END,final)

                elif self.combobox.get()=='English to Urdu':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english ,dest='ur')
                        self.lang2.config(text='URDU')
                        self.text2.delete('1.0',END)
                        self.text2.insert('1.0',result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS",'Please check your internet connection!')

                elif self.combobox.get()=='English to German':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english, dest='german')
                        self.lang2.config(text='GERMAN')
                        self.text2.delete('1.0', END)
                        self.text2.insert('1.0', result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS", 'Please check your internet connection!')

                elif self.combobox.get()=='English to Turkish':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english, dest='turkish')
                        self.lang2.config(text='TURKISH')
                        self.text2.delete('1.0', END)
                        self.text2.insert('1.0', result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS", 'Please check your internet connection!')

                elif self.combobox.get()=='English to Spanish':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english, dest='spanish')
                        self.lang2.config(text='SPANISH')
                        self.text2.delete('1.0', END)
                        self.text2.insert('1.0', result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS", 'Please check your internet connection!')

                elif self.combobox.get()=='English to Russian':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english, dest='ru')
                        self.lang2.config(text='RUSSIAN')
                        self.text2.delete('1.0', END)
                        self.text2.insert('1.0', result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS", 'Please check your internet connection!')

                elif self.combobox.get()=='English to Persian':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english, dest='persian')
                        self.lang2.config(text='PERSIAN')
                        self.text2.delete('1.0', END)
                        self.text2.insert('1.0', result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS", 'Please check your internet connection!')

                elif self.combobox.get()=='English to Arabic':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english, dest='ar')
                        self.lang2.config(text='ARABIC')
                        self.text2.delete('1.0', END)
                        self.text2.insert('1.0', result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS", 'Please check your internet connection!')

                elif self.combobox.get()=='English to Sindhi':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english, dest='sindhi')
                        self.lang2.config(text='SINDHI')
                        self.text2.delete('1.0', END)
                        self.text2.insert('1.0', result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS", 'Please check your internet connection!')

                elif self.combobox.get()=='English to Japanese':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english, dest='japanese')
                        self.lang2.config(text='Japanese')
                        self.text2.delete('1.0', END)
                        self.text2.insert('1.0', result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS", 'Please check your internet connection!')

                elif self.combobox.get()=='English to Chinese':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english, dest='zh-tw')
                        self.lang2.config(text='Chinese')
                        self.text2.delete('1.0', END)
                        self.text2.insert('1.0', result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS", 'Please check your internet connection!')

                elif self.combobox.get()=='English to Korean':
                    try:
                        translator = googletrans.Translator()
                        result = translator.translate(english, dest='Korean')
                        self.lang2.config(text='Korean')
                        self.text2.delete('1.0', END)
                        self.text2.insert('1.0', result.text)
                    except httpcore._exceptions.ConnectError:
                        showerror("M-LANGTRANS", 'Please check your internet connection!')

                else:
                    showerror('M-LANGTRANS','Please choose a valid language!')

        def exit():
            question = askokcancel('Translator','Do you want to exit?')
            if question:
                sys.exit()
            else:
                pass

        def credits():
            showinfo('Translator','Language Translator Created By Muhammad Muzammil')

        self.master = master
        self.geometry = master.geometry('800x500')
        self.master.protocol('WM_DELETE_WINDOW',exit)
        self.resizable = master.resizable(0,0)
        self.title = master.title('LANGUAGE TRANSLATOR')
        self.background = master.config(background='black')
        self.label_head = Label(master,text='Welcome To The Language Translator',font='cursive 20 bold italic', bg='black',fg='yellow').pack()
        self.translate = Button(master,text='TRANSLATE',font='cursive 15 bold italic',bg='green',fg='red',activeforeground='yellow',activebackground='red',command=translate1,cursor='hand2')
        self.translate.pack(side=BOTTOM)
        self.translate.bind('<Enter>',enter)
        self.translate.bind('<Leave>',leave)
        self.lang1 = Label(master,text='ENGLISH',bg='black',font='cursive 12 bold italic',fg='white')
        self.lang1.place(x=120,y=120)
        self.text1 = Text(master,width=40,height=20)
        self.text1.place(y=150)
        self.lang2 = Label(master,text='',bg='black',font='cursive 12 bold italic',fg='white')
        self.lang2.place(x=600,y=120)
        self.text2 = Text(master,width=40,height=20)
        self.text2.place(x=475,y=150)
        self.labellanuage = Label(master,text='Select Language: ',font='cursive 10 bold italic',fg='yellow',bg='black').place(x=345,y=150)
        self.combobox = ttk.Combobox(master,font='curisve 8 ',width=17)
        self.combobox.place(x=340,y=170)
        self.combobox['values'] = [
            'English to ASCII',
            'English to Urdu',
            'English to German',
            'English to Turkish',
            'English to Spanish',
            'English to Russian',
            'English to Arabic',
            'English to Persian',
            'English to Sindhi',
            'English to Japanese',
            'English to Chinese',
            'English to Korean',
        ]
        self.combobox.current(0)
        self.menubar = Menu(master)
        self.help = Menu(self.menubar,tearoff=0)
        self.help.add_command(label='Credits', command=credits)
        self.menubar.add_cascade(label='Help',menu=self.help)
        self.master.config(menu=self.menubar)

window = Tk()
translater(window)
window.mainloop()
