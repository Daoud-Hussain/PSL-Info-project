from tkinter import *
from tkinter import ttk
from typing import Pattern, Sized
# from typing_extensions import ParamSpec
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
from tkinter import messagebox
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
import pymysql
list = [2,3,4,5,8,12,15,16,18,20,22,25,27]
class Login_page:
    def __init__(self,root):
        self.root=root 
        self.root.title("Pakistan Super League")
        self.root.geometry('1550x800+0+0')
        

        load=Image.open("2.jpg")
        load=load.resize((1350,720),Image.ANTIALIAS)
        self.render=ImageTk.PhotoImage(load)
        img=Label(self.root,image=self.render)
        img.place(x=0,y=0)
        total_price_entry = Entry(self.root, font="Conolas", 
                                    width=15).place(x=350,y=600)
        self.root=Label(self.root,text="Username",font=('Montserrat Semibold',12),bg="#1C170C",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=350,y=575)
        total_price_entry = Entry(self.root, font="Conolas",show="*",
                                    width=15).place(x=800,y=600)
        self.root=Label(self.root,text="Password",font=('Montserrat Semibold',12),bg="#1C170C",border=0,fg="white",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=800,y=575)
        login_1=Button(self.root,text="LOG IN",command=self.main_win,font=('Consolas',13,"bold"),bg="#F4E147",border=0,fg="black",cursor="hand2",activebackground="#F4E147",activeforeground="#F4E147").place(x=600,y=670,width="150")
    def main_win(self):
        self.root2=Toplevel()
        self.root2.geometry("1500x800+0+0")
        self.root2.configure(bg="#016F35")
        self.bg = PhotoImage(file="3.png")
        lbl_1 = Label(self.root2, image=self.bg)
        lbl_1.place(x=0, y=0)
        # self.psl=Label(self.root2,text="WELCOME TO PSL INFO DSEK",font=('Montserrat bold',32),bg="#F4E147",border=0,fg="black",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=420,y=100)
        # self.psldash=Label(self.root2,text="WELCOME TO PSL INFO DSEK",font=('Montserrat bold',32),bg="#F4E147",border=0,fg="black",cursor="hand2",activebackground="#39065D",activeforeground="#39065D").place(x=420,y=100)

        Players=Button(self.root2,text="1.PLAYERS",command=self.player_win,font=('Montserrat',17,"bold"),bg="white",border=0,fg="black",cursor="hand2",activebackground="white",activeforeground="white").place(x=313,y=280,width="150")
        Teams=Button(self.root2,text="2.TEAMS",command=self.teams,font=('Montserrat',17,"bold"),bg="white",border=0,fg="black",cursor="hand2",activebackground="white",activeforeground="white").place(x=300,y=320,width="150")
        staff=Button(self.root2,text="3.STAFF DETAILS",command=self.team_staff,font=('Montserrat',17,"bold"),bg="white",border=0,fg="black",cursor="hand2",activebackground="white",activeforeground="#F4E147").place(x=300,y=365,width="250")
        ticket=Button(self.root2,command=self.booking,text="4.TICKET",font=('Montserrat',17,"bold"),bg="white",border=0,fg="black",cursor="hand2",activebackground="white",activeforeground="#F4E147").place(x=300,y=405,width="150")
        exist=Button(self.root2,text="5.EXIST",command=self.exist,font=('Montserrat',17,"bold"),bg="white",border=0,fg="black",cursor="hand2",activebackground="#F4E147",activeforeground="#F4E147").place(x=290,y=450,width="150")

    def player_win(self):
        self.root3=Toplevel()
        self.root3.geometry("750x400+300+150")
        self.root3.configure(bg="green")
        self.psl=Label(self.root3,text="SELECT A TEAM",font=('Montserrat',20),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=290,y=40)
        isl=Button(self.root3,text="ISLAMABAD UNITED",command=self.islamabad,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="white").place(x=300,y=100)
        lhr=Button(self.root3,text="LAHORE QALANDER",command=self.lahore,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=140)
        qetta=Button(self.root3,command=self.quetta,text="QUETTA GLADIATOR",font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=180)
        peshwar=Button(self.root3,text="PESHAWAR ZALMI",command=self.peshawar,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=220)
        krachi=Button(self.root3,command=self.karachi,text="KARACHI KING",font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=300,y=260)
        mltn=Button(self.root3,command=self.multan,text="KARACHI KING",font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=300,y=260)

    def islamabad(self):
        self.root4=Toplevel()
        self.root4.geometry("750x550+300+150")
        self.root4.configure(bg="orange")

        shahdab=Button(self.root4,text="1. Shadab Khan (C)",command=self.shadab,font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=100)
        hasan=Button(self.root4,command=self.hasan,text="2. Hasan Ali (VC)",font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=140)
        rohail=Button(self.root4,command=self.rohail,text="3. Rohail Nazeer (WK)",font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=180)
        faheem=Button(self.root4,command=self.faheem,text="4. Faheem Ashraf",font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=220)
        asif=Button(self.root4,command=self.asif,text="5. Asif Ali",font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=260)
        hussain=Button(self.root4,text="6. Hussain Talat",command=self.hussain,font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=290)
        jana=Button(self.root4,command=self.jana,text="7. Janeman Malan",font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=320)
        fawad=Button(self.root4,command=self.fawad,text="8. Fawad Ahmed",font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=350)
        musa=Button(self.root4,command=self.musa,text="9. Musa Khan",font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=380)
        akif=Button(self.root4,command=self.akif,text="10.Akif Javed",font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=410)
        ander=Button(self.root4,command=self.andre,text="11.Andre Fletcher",font=('Montserrat',12),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=440)
    def shadab(self):
        self.root7=Toplevel()
        self.root7.geometry("400x250+300+150")
        self.root7.configure(bg="green")
        self.psl=Label(self.root7,text=''' 
         Name: Shadab Khan
        Country: Pakistan
        Age: 24
        Specification: Bowling All-rounder
        Batsman: Right-Handed Batsman
        Bowler: Right Arm Orthodax
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def hasan(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Hasan Ali
        Country: Pakistan
        Age: 25
        Specification: Bowler
        Style: Right-Arm Fast
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def rohail(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Rohail Nazeer
        Country: Pakistan
        Age: 22
        Specification: Wicketkeeper Batsman
        Batting style: Right-Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=15,y=25)
    def faheem(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Faheem Ashraf
        Country: Pakistan
        Age: 26
        Specification: Batting All Rounder
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def asif(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Asif Ali
        Country: Pakistan
        Age: 29
        Specification: Batsaman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def hussain(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Hussain Talat
        Country: Pakistan
        Age: 23
        Specification: Batting All-Rounder
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def jana(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Janeman Malan
        Country: South Africa
        Age: 27
        Specification: Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def fawad(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Fawad Ahmed
        Country: Australia
        Age: 29
        Specification: Spin Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def musa(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Musa Khan
        Country: Pakistan
        Age: 20
        Specification: Fast Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def akif(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Akif Javed
        Country: Pakistan
        Age: 24
        Specification: Fast Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def andre(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Andre Fletcher
        Country: West Indies
        Age: 29
        Specification: Batsaman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)


    def quetta(self):
        self.root5=Toplevel()
        self.root5.geometry("750x550+300+150")
        self.root5.configure(bg="darkred")

        sarfraz=Button(self.root5,text="1. Sarfraz Ahmed (C) (WK)",command=self.sarfraz,font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=100)
        nawaz=Button(self.root5,command=self.nawaz,text="2. Mohammad Nawaz (VC)",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=140)
        azam=Button(self.root5,command=self.azam,text="3. Azam Khan",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=180)
        gayle=Button(self.root5,command=self.gayle,text="4. Chris Gayle",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=220)
        cutting=Button(self.root5,command=self.cutting,text="5. Ben Cutting",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=260)
        russel=Button(self.root5,text="6. Andre Russel",command=self.russel,font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=290)
        zahid=Button(self.root5,command=self.zahid,text="7. Zahid Mehmood",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=320)
        hasnain=Button(self.root5,command=self.hasnain,text="8. Mohammad Hasnain",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=350)
        naseem=Button(self.root5,command=self.naseem,text="9. Naseem Shah",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=380)
        usman=Button(self.root5,command=self.usman,text="10. Usman Khan",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=410)
        steyn=Button(self.root5,command=self.steyn,text="11.Dale Styen",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=440)
    def sarfraz(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Sarfraz Ahmed
        Country: Pakistan
        Age: 32
        Specification: WicketKeeper Batsman
        Batsman: Right-Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def nawaz(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Mohammad Nawaz
        Country: Pakistan
        Age: 30
        Specification: Left Arm Spin Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def azam(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Azam Khan
        Country: Pakistan
        Age: 24
        Specification: Batsman
        Batting style: Right-Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=15,y=25)
    def gayle(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Christopher Henry Gayle
        Country: West Indies
        Age: 42
        Specification: Batsman 
        Batting Style: Left HAnded Batsman
        Bowling Style: Left Arm Spin
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def cutting(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Ben Cutting
        Country: Australia
        Age: 34
        Specification: Fast Bowling All-Rounder
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def russel(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Andre Russel
        Country: West Indies
        Age: 33
        Specification: Bowling All-Rounder
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def zahid(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Zahid Mehmood
        Country: Pakistan
        Age: 24
        Specification: Spin Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def hasnain(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: M HAsnain
        Country: Pakistan
        Age: 20
        Specification: FAst Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=18,y=25)
    def naseem(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Naseem Shah
        Country: Pakistan
        Age: 20
        Specification: Fast Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def usman(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Usman Khan
        Country: Pakistan
        Age: 28
        Specification: Right Handed BAtsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def steyn(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Dale Steyn
        Country: South Africa
        Age: 36
        Specification: Fast Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def lahore(self):
        self.root5=Toplevel()
        self.root5.geometry("750x550+300+150")
        self.root5.configure(bg="darkred")

        sohail=Button(self.root5,text="1. Sohail Akhtar (C)",command=self.sohail,font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=100)
        shaheen=Button(self.root5,command=self.shaheen,text="2. Shaheen Afridi (VC)",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=140)
        dunk=Button(self.root5,command=self.dunk,text="3. Ben Dunk (WK)",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=180)
        ahmed=Button(self.root5,command=self.ahmed,text="4. Ahmed Danial",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=220)
        maaz=Button(self.root5,command=self.maaz,text="5. Maaz Khan",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=260)
        rashid=Button(self.root5,text="6. Rashid Khan",command=self.rashid,font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=290)
        rauf=Button(self.root5,command=self.rauf,text="7. Haris Rauf",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=320)
        samit=Button(self.root5,command=self.samit,text="8. Samit Patel",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=350)
        hafeez=Button(self.root5,command=self.hafeez,text="9. Muhammad Hafeez",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=380)
        fakhar=Button(self.root5,command=self.fakhar,text="10.Fakhar Zaman",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=410)
        wiese=Button(self.root5,command=self.wiese,text="11.David Wiese",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=440)
    def sohail(self):
        self.root7=Toplevel()
        self.root7.geometry("400x250+300+150")
        self.root7.configure(bg="green")
        self.psl=Label(self.root7,text=''' 
        Name: Sohail Akhtar
        Country: Pakistan
        Age: 24
        Specification: Batsman
        Batsman: Right-Handed Batsman

        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def shaheen(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Shaheen Afridi
        Country: Pakistan
        Age: 24
        Specification: Bowler
        Style: Left-Arm Fast
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def dunk(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Ben Dunk
        Country: Austalia
        Age: 29
        Specification: Wicketkeeper Batsman
        Batting style: Left-Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=15,y=25)
    def ahmed(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Ahmed Danial
        Country: Pakistan
        Age: 21
        Specification: FAst Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def maaz(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Maaz Khan
        Country: Pakistan
        Age: 23
        Specification: Spin Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def rashid(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Rashid Khan
        Country: Afghanistan
        Age: 23
        Specification: Spin Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def rauf(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Haris Rauf
        Country: Pakistan
        Age: 27
        Specification: Fast Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def samit(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Samit Patel
        Country: England
        Age: 32
        Specification: Bowling All-Rounder
        Category: Right-Arm Spin
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=18,y=25)
    def hafeez(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Muhammad Hafeez
        Country: Pakistan
        Age: 40
        Specification: Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def fakhar(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Fakhar Zaman
        Country: Pakistan
        Age: 29
        Specification: Left Handed BAtsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def wiese(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: David Wiese
        Country: South Africa
        Age: 35
        Specification: Bowling All-Rounder
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def multan(self):
        self.root5=Toplevel()
        self.root5.geometry("750x550+300+150")
        self.root5.configure(bg="darkred")

        rizwan=Button(self.root5,text="1. Sarfraz Ahmed (C) (WK)",command=self.rizwan,font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=100)
        shan=Button(self.root5,command=self.shan,text="2. Mohammad Nawaz (VC)",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=140)
        afridi=Button(self.root5,command=self.afridi,text="3. Azam Khan",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=180)
        qadir=Button(self.root5,command=self.qadir,text="4. Chris Gayle",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=220)
        hetmyer=Button(self.root5,command=self.hetmyer,text="5. Ben Cutting",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=260)
        tahir=Button(self.root5,text="6. Andre Russel",command=self.tahir,font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=290)
        maqsood=Button(self.root5,command=self.maqsood,text="7. Zahid Mehmood",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=320)
        sohail=Button(self.root5,command=self.sohail,text="8. Mohammad Hasnain",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=350)
        tanvir=Button(self.root5,command=self.tanvir,text="9. Naseem Shah",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=380)
        dhani=Button(self.root5,command=self.dhani,text="10. Usman Khan",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=410)
        roussow=Button(self.root5,command=self.roussow,text="11.Dale Styen",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=440)
    def rizwan(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Sarfraz Ahmed
        Country: Pakistan
        Age: 32
        Specification: WicketKeeper Batsman
        Batsman: Right-Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def shan(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Mohammad Nawaz
        Country: Pakistan
        Age: 30
        Specification: Left Arm Spin Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def afridi(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Azam Khan
        Country: Pakistan
        Age: 24
        Specification: Batsman
        Batting style: Right-Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=15,y=25)
    def qadir(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Christopher Henry Gayle
        Country: West Indies
        Age: 42
        Specification: Batsman 
        Batting Style: Left HAnded Batsman
        Bowling Style: Left Arm Spin
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def hetmyer(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Ben Cutting
        Country: Australia
        Age: 34
        Specification: Fast Bowling All-Rounder
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def maqsood(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Andre Russel
        Country: West Indies
        Age: 33
        Specification: Bowling All-Rounder
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def sohail(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Zahid Mehmood
        Country: Pakistan
        Age: 24
        Specification: Spin Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def tanvir(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: M HAsnain
        Country: Pakistan
        Age: 20
        Specification: Fast Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=18,y=25)
    def dhani(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Naseem Shah
        Country: Pakistan
        Age: 20
        Specification: Fast Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def roussow(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Usman Khan
        Country: Pakistan
        Age: 28
        Specification: Right Handed BAtsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def tahir(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Dale Steyn
        Country: South Africa
        Age: 36
        Specification: Fast Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)

    def karachi(self):
        self.root5=Toplevel()
        self.root5.geometry("750x550+300+150")
        self.root5.configure(bg="darkred")

        imad=Button(self.root5,text="1. Imad Waseem (C)",command=self.imad,font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=100)
        babar=Button(self.root5,command=self.babar,text="2. Babar Azam (VC)",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=140)
        walton=Button(self.root5,command=self.walton,text="3. Chadwick Walton",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=180)
        sharjeel=Button(self.root5,command=self.sharjeel,text="4. Sharjeel Khan",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=220)
        guptil=Button(self.root5,command=self.guptil,text="5. Martin Guptil",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=260)
        amir=Button(self.root5,text="6. Mohammad Amir",command=self.amir,font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=290)
        arshad=Button(self.root5,command=self.arshad,text="7. Arshad Iqbal",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=320)
        waqas=Button(self.root5,command=self.waqas,text="8. Waqas Maqsood",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=350)
        aamir=Button(self.root5,command=self.aamir,text="9. Aamir Yamin",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=380)
        danish=Button(self.root5,command=self.danish,text="10. Danish Aziz",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=410)
        qasim=Button(self.root5,command=self.qasim,text="11. Qasim Akram",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=440)
    def imad(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Imad Waseem
        Country: Pakistan
        Age: 27
        Specification: Bowling All-rounder
        Batsman: Left-Handed Batsman
        Bowler: Left Arm Offspin
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def babar(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Babar Azam
        Country: Pakistan
        Age: 25
        Specification: Batsman
        Batting Style: Right-Handed
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def walton(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Chadwick Walton
        Country: West Indies
        Age: 27
        Specification: Wicketkeeper Batsman
        Batting style: Right-Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=15,y=25)
    def sharjeel(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Sharjeel Khan
        Country: Pakistan
        Age: 28
        Specification: Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def guptil(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Martin Guptil
        Country: New Zealand
        Age: 29
        Specification: Batsaman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def amir(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Mohammad Amir
        Country: Pakistan
        Age: 29
        Specification: Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def arshad(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Arshad Iqbal
        Country: Pakistan
        Age: 21
        Specification: Bowlwer
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def waqas(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Waqas MAqssod
        Country: Pakistan
        Age: 23
        Specification: FAst Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=18,y=25)
    def aamir(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Amir Yamin
        Country: Pakistan
        Age: 24
        Specification: Fast Bowler All-rounder
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def danish(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Danish Aziz
        Country: Pakistan
        Age: 22
        Specification: Bowling All-rounder
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def qasim(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Qasim Akram
        Country: Pakistan
        Age: 21
        Specification: Batting All-rounder
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def peshawar(self):
        self.root5=Toplevel()
        self.root5.geometry("750x550+300+150")
        self.root5.configure(bg="darkred")

        wahab=Button(self.root5,text="1. Wahab Riaz (C) ",command=self.wahab,font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=100)
        shoaib=Button(self.root5,command=self.shoaib,text="2. Shoaib Malik (VC)",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=140)
        kamran=Button(self.root5,command=self.kamran,text="3. Kamran Akmal (WK)",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=180)
        imam=Button(self.root5,command=self.imam,text="4. Imam Ul Haq",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=220)
        zazai=Button(self.root5,command=self.zazai,text="5. Hazrat Ullah Zazai",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=260)
        imran=Button(self.root5,text="6. Mohammad Imran",command=self.imran,font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=290)
        irfan=Button(self.root5,command=self.irfan,text="7. Mohammad Irfan",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=320)
        miller=Button(self.root5,command=self.miller,text="8. David Miller",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=350)
        kohler=Button(self.root5,command=self.kohler,text="9. Tom Kohler Cadmore",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=380)
        saqib=Button(self.root5,command=self.saqib,text="10. Saqib Mehmood",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="#F4E147").place(x=300,y=410)
        haider=Button(self.root5,command=self.haider,text="11. Haider Ali",font=('Montserrat',12),bg="darkred",border=0,fg="white",cursor="hand2",activebackground="darkred",activeforeground="white").place(x=300,y=440)
    def wahab(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Wahab Riaz
        Country: Pakistan
        Age: 34
        Specification: Bowling All_Rounder
        Batsman: Right-Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def shoaib(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Shoaib Malik
        Country: Pakistan
        Age: 41
        Specification: Right Handed Batsman
        Bowling Style: Right Arm Offspin
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def kamran(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Kamran Akmal
        Country: Pakistan
        Age: 37
        Specification: WicketKeeper BAtsman
        Batting style: Right-Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=15,y=25)
    def zazai(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: HazratUllah Zazai
        Country: Afghanistan
        Age: 34
        Specification: Batsman 
        Batting Style: Left HAnded Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def imam(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Imam Ul Haq
        Country: Pakistan
        Age: 27
        Specification: Left Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def saqib(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Saqib Mehmood
        Country: England
        Age: 35
        Specification: FAst Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def imran(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: M Imran
        Country: Pakistan
        Age: 22
        Specification: FAst Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def irfan(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: M Irfan
        Country: Pakistan
        Age: 35
        Specification: FAst Bowler
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=18,y=25)
    def miller(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: David Miller
        Country: South Africa
        Age: 32
        Specification: Left Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def kohler(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Tom Kohler Cadmore
        Country: Australia
        Age: 23
        Specification: Right Handed Batsman
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)
    def haider(self):
        self.root10=Toplevel()
        self.root10.geometry("400x250+300+150")
        self.root10.configure(bg="green")
        self.psl=Label(self.root10,text=''' 
        Name: Haider Ali
        Country: Pakistan
        Age: 22
        Specification: Right HAnded Batsaman ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=25,y=25)

    #team function 
    def teams(self):
        self.root3=Toplevel()
        self.root3.geometry("750x400+300+150")
        self.root3.configure(bg="green")
        self.psl=Label(self.root3,text="SELECT A TEAM",font=('Montserrat',20),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=290,y=40)
        isl=Button(self.root3,text="ISLAMABAD UNITED",command=self.islamabad_info,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="white").place(x=300,y=100)
        lhr=Button(self.root3,command=self.lahore_info,text="LAHORE QALANDER",font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=140)
        qetta=Button(self.root3,text="QUETTA GLADIATOR",command=self.quetta_info,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=180)
        peshwar=Button(self.root3,text="PESHAWAR ZALMI",command=self.peshawar_info,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=220)
        krachi=Button(self.root3,text="KARACHI KING",command=self.karachi_info,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=300,y=260)
        mltn=Button(self.root3,text="MULTAN SULTANS",command=self.multan_info,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=300,y=300)

    def islamabad_info(self):
        self.root6=Toplevel()
        self.root6.geometry("700x300+250+100")
        self.root6.configure(bg="orange")
        self.psl=Label(self.root6,text=''' 
        Islamabad is the most fortunate side of
        the PSL who stood on the winning floor
        twice. It Represents the Capital city of
        Pakistan. This squad played the centalizing
        cricket brand in HBL PSL. They stood on the
        winning floor in PSL 2016 and 2018.
        ''',font=('Montserrat',15),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="green",activeforeground="green").place(x=100,y=40)
    def lahore_info(self):
        self.root7=Toplevel()
        self.root7.geometry("700x300+250+100")
        self.root7.configure(bg="green")
        self.psl=Label(self.root7,text=''' 
        Qalandars is admitted as one of the fantastic  
        and brilliant t20 squad in PSL. This lineup is
        also famous for its passion and played exciting
        and thrilling matches oer the last five years.
        They are the runner-up in PSL 5.  
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=100,y=40)
    def karachi_info(self):
        self.root7=Toplevel()
        self.root7.geometry("700x300+250+100")
        self.root7.configure(bg="blue")
        self.psl=Label(self.root7,text=''' 
        Karachi Kings is the defending Champion of PSL
        2020. It is one of the aggressive and brilliant
        side for Pakistan Cricket that personifies one 
        of the biggest city of PAkistan 'Karachi'. The 
        frenchise is known for Epic cricket in PSL. 
        ''',font=('Montserrat',15),bg="blue",border=0,fg="red",cursor="hand2",activebackground="green",activeforeground="green").place(x=100,y=40)
    
    def peshawar_info(self):
        self.root7=Toplevel()
        self.root7.geometry("700x300+250+100")
        self.root7.configure(bg="yellow")
        self.psl=Label(self.root7,text=''' 
        Peshawar Zalmi is one of the epic team of the
        domestic cricket that peronifies the city of 
        Peshawar. A PAkistani Business tycon JAved Khan
        Afridi is the properiter of the frenchise. Zalmi
        stood on the winning floor in PSL 2017 under the
        captaincy of a Legendry Cricketer Daren Sammy. 
        Wahab Riaz is the current Skipper of the team.
        ''',font=('Montserrat',15),bg="yellow",border=0,fg="black",cursor="hand2",activebackground="green",activeforeground="green").place(x=100,y=40)
    def quetta_info(self):
        self.root7=Toplevel()
        self.root7.geometry("700x300+250+100")
        self.root7.configure(bg="purple")
        self.psl=Label(self.root7,text=''' 
        Quetta Gladiators is consider as one of the most
        successful team of HBL PSL. They Played awesomwe 
        cricket throughout the league. Gladiators were 
        the runnerup of 2016 and 2017 HBL PSL. They stood
        on the winning floor in PSL 2019. Gladiators is 
        lead by one of the successful captain of Pakistan.
        ''',font=('Montserrat',15),bg="purple",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=100,y=40)
    def multan_info(self):
        self.root7=Toplevel()
        self.root7.geometry("700x300+250+100")
        self.root7.configure(bg="green")
        self.psl=Label(self.root7,text=''' 
        Multan Sultans is a brilliant domestic t20 side   
        in Pakistan Super League. It was on the top of 
        the points table after the first round of HBL 
        Pakistan Super League. They play gorgeous cricket
        and has a great combination of seniors and juniors
        overseas and local cricketers. 
        ''',font=('Montserrat',15),bg="green",border=0,fg="blue",cursor="hand2",activebackground="green",activeforeground="green").place(x=100,y=40)

    def team_staff(self):
        self.root3=Toplevel()
        self.root3.geometry("750x400+300+150")
        self.root3.configure(bg="green")
        self.psl=Label(self.root3,text="SELECT A TEAM",font=('Montserrat',20),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=290,y=40)
        isl=Button(self.root3,text="ISLAMABAD UNITED",command=self.islamabad_staff,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="white").place(x=300,y=100)
        lhr=Button(self.root3,text="LAHORE QALANDER",command=self.lahore_staff,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=140)
        qetta=Button(self.root3,text="QUETTA GLADIATOR",command=self.quetta_staff,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=180)
        peshwar=Button(self.root3,text="PESHAWAR ZALMI",command=self.peshawar_staff,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=220)
        krachi=Button(self.root3,text="KARACHI KING",command=self.karachi_staff,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=300,y=260)
        mltn=Button(self.root3,text="MULTAN SULTANS",command=self.multan_staff,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=300,y=300)
    def islamabad_staff(self):
        self.root5=Toplevel()
        self.root5.geometry("550x250+150+50")
        self.root5.configure(bg="orange")
        self.psl=Label(self.root5,text=''' 
        Team: Islamabad United
        Head Coach: Johan Botha
        Assitant Coach: Saeed Ajmal
        Fielding and Fitness Trainer: Corey Rutgers
        Owner: Ali Naqvi
        Home GRound: RAwalpindi Cricket Stadium
        ''',font=('Montserrat',15),bg="orange",border=0,fg="darkred",cursor="hand2",activebackground="green",activeforeground="green").place(x=80,y=40)
    def lahore_staff(self):
        self.root5=Toplevel()
        self.root5.geometry("550x250+150+50")
        self.root5.configure(bg="green")
        self.psl=Label(self.root5,text=''' 
        Team: Lahore Qalandars
        Head Coach: Aaqib Javed
        Batting Coach: Mansoor Rana 
        Fitness Trainer: Shehzad Butt
        Owner: Sameen Rana
        Home GRound: Gaddafi Stadium Lahore
        ''',font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=80,y=40)
    def quetta_staff(self):
        self.root5=Toplevel()
        self.root5.geometry("550x250+150+50")
        self.root5.configure(bg="purple")
        self.psl=Label(self.root5,text=''' 
        Team: Quetta Gladiators
        Head Coach: Moin Khan
        BAtting Coach: Sir Vivian Richard
        Bowling Coach: Umar Gul
        Owner: Nadeem Umar
        Home GRound: Buggti Cricket Stadium
        ''',font=('Montserrat',15),bg="purple",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=80,y=40)
    def peshawar_staff(self):
        self.root5=Toplevel()
        self.root5.geometry("550x250+150+50")
        self.root5.configure(bg="yellow")
        self.psl=Label(self.root5,text=''' 
        Head Coach: Daren Sammy
        Batting Coach: HAshim Amla
        Owner: Javed Khan Afridi
        Home GRound: Arbab Niaz Stadium
        ''',font=('Montserrat',15),bg="yellow",border=0,fg="black",cursor="hand2",activebackground="green",activeforeground="green").place(x=80,y=40)
    def multan_staff(self):
        self.root5=Toplevel()
        self.root5.geometry("550x250+150+50")
        self.root5.configure(bg="green")
        self.psl=Label(self.root5,text=''' 
        Team: Multan Sultans
        Head Coach: Andy Flowers
        Bowling Coach: Azhar Mehmood
        spin Bowling Coach: Mushtaq Ahmed
        Owner: Ali Khan Tareen
        Home GRound: Multan Cricket Stadium
        ''',font=('Montserrat',15),bg="green",border=0,fg="blue",cursor="hand2",activebackground="green",activeforeground="green").place(x=80,y=40)
    def karachi_staff(self):
        self.root5=Toplevel()
        self.root5.geometry("750x400+300+150")
        self.root5.configure(bg="blue")
        self.psl=Label(self.root5,text=''' 
        Team: Karachi Kings
        Head Coach: Harschelle Gibbs
        Bowling Coach: Waseem Akram 
        Batting Coach: Faisal Iqbal
        Owner: Salman Iqbal
        Home GRound: National Stadium Karachi
        ''',font=('Montserrat',15),bg="blue",border=0,fg="darkred",cursor="hand2",activebackground="green",activeforeground="green").place(x=80,y=40)
    
    # def booking_system(self):
    #     self.root10=Toplevel()
    #     self.root10.geometry("750x400+300+150")
    #     self.root10.configure(bg="green")
    #     self.psl=Label(self.root10,text="TICKET RESERVATION SYSTEM",font=('Montserrat',20),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=290,y=40)
    #     res_tick=Button(self.root10,text="Reserve Ticket",command=self.res_tick,font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="white").place(x=300,y=100)
    #     ret=Button(self.root10,text="Return Ticket",font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=140)
    #     check=Button(self.root10,text="Check status",font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=180)
    #     exit=Button(self.root10,text="Exit",font=('Montserrat',12),bg="green",border=0,fg="white",cursor="hand2",activebackground="white",activeforeground="green").place(x=300,y=220)
    def res_tick(self):
        self.root11=Toplevel()
        self.root11.geometry("750x400+300+150")
        tick_choice = Entry(self.root11, font="Conolas",width=35).place(x=100,y=40)
        self.root11.configure(bg="green")
        self.root11=Label(self.root11,text="Enter number of tickets you want" ,font=('Montserrat',15),bg="green",border=0,fg="white",cursor="hand2",activebackground="green",activeforeground="green").place(x=100,y=40)

    def exist(self):
        self.root2.destroy()
    def booking(self):
        self.root11= Toplevel()
        self.root11.geometry("1000x400")
        self.root11.title("Python + Database")
        self.root11.configure(bg="#483D4B")
        s=Label(self.root11, text = "WELCOME TO PSL TICKET BOOKING SYSTEM",  background = '#483D4B', foreground ="white",  
        font = ("Montserrat bold", 15))
        s.place(x = 270, y = 10) 
        a=Label(self.root11, text='Ticket No.', font=('bold', 10),background = '#483D4B',fg="white")
        a.place(x=20,y=60);
        b=Label(self.root11, text='Name', font=('bold', 10),background = '#483D4B',fg="white")
        b.place(x=20,y=90);
        c=Label(self.root11, text='Age', font=('bold', 10),background = '#483D4B',fg="white")
        c.place(x=20,y=120);
        d=Label(self.root11, text='Nationality', font=('bold', 10),background = '#483D4B',fg="white")
        d.place(x=20,y=150);

        self.e_a = Entry(self.root11)
        self.e_a.place(x=150,y=60)

        self.e_b = Entry(self.root11)
        self.e_b.place(x=150,y=90)
        self.e_c = Entry(self.root11)
        self.e_c.place(x=150,y=120)

        self.e_d = Entry(self.root11)
        self.e_d.place(x=150,y=150)

        book = Button(self.root11, text="Book Ticket", font=("bold",10),bg="white", command=self.book)
        book.place(x=20,y=190)

        cancel = Button(self.root11, text="Cancel Ticket", font=("bold",10),bg="white", command=self.cancel)
        cancel.place(x=120,y=190)

        seat = Button(self.root11, text="Refresh List", font=("bold",10),bg="white", command=self.fetch_data2)
        seat.place(x=220,y=190)

        self.frame1 = Frame(self.root11,)
        self.frame1.place(x=350, y=65, width=600, height=250)
        self.scroll_x=Scrollbar(self.frame1,orient=HORIZONTAL)
        self.scroll_y=Scrollbar(self.frame1,orient=VERTICAL)
        self.details_1=ttk.Treeview(self.frame1,column=("ref","dau","ali","pak"),xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.details_1.xview)
        self.scroll_y.config(command=self.details_1.yview)

        self.details_1.heading("ref",text="SEAT NO")
        self.details_1.heading("dau",text="NAME")
        self.details_1.heading("ali",text="AGE")
        self.details_1.heading("pak",text="NATIONALITY")
        self.details_1["show"]="headings"
        self.details_1.pack(fill=BOTH,expand=1)
        self.fetch_data2()

        # list= Listbox(self.root11,width=35)
        # list.place(x=350, y=60)
    def book(self):
        a=self.e_a.get();
        b=self.e_b.get();
        c=self.e_c.get();
        d=self.e_d.get();

        if (a=="" or b=="" or c=="" or d==''):
            MessageBox.showinfo("staus", "all fielsds required ")
        else:
            con_1= pymysql.connect(host="localhost", user="root", password="daoud123", database="ticket")
            my_cur=con_1.cursor()
            my_cur.execute("insert into booking(no,name,age,country)values(%s,%s,%s,%s)",(self.e_a.get(),
                                                                                    self.e_b.get(),
                                                                                    self.e_c.get(),
                                                                                    self.e_d.get()))
            messagebox.showinfo("book status", "booked succesfully",parent=self.root11);
            con_1.commit()
            con_1.close()

    def cancel(self):
        del_my=messagebox.askyesno("Hotel Mangement system","Do you want to delete this Entry!",parent=self.root11)
        if del_my>0:
            con_1= pymysql.connect(host="localhost", user="root", password="daoud123", database="ticket")
            cur_1=con_1.cursor()
            query="delete from booking where no=%s"
            value=(self.e_a.get(),)
            cur_1.execute(query,value)
        else:
            if not del_my:
                return
        messagebox.showinfo("Succes","Ticket has been cancelled successfully",parent=self.root11)
        con_1.commit()
        con_1.close()
    def clear1(self):
        list.delete(0,'end')

    def seat(self):
        con_1= pymysql.connect(host="localhost", user="root", password="daoud123", database="ticket")
        my_cur=con_1.cursor()
        my_cur.execute("select * from booking")
        rows=my_cur.fetchall()
        for row in rows:
            insertdata= str(row[0])+' '+str(row[1])+' '+ row[2]+' '+ row[3]
            messagebox.showinfo(f'info',insertdata,parent=self.root11)
            list.insert(list.size()+12, insertdata)
        con_1.commit()  
        con_1.close()
    def fetch_data2(self):
        con_1= pymysql.connect(host="localhost", user="root", password="daoud123", database="ticket")
        my_cur=con_1.cursor()
        my_cur.execute("select * from booking")
        row_2=my_cur.fetchall()
        if len(row_2)!=0:
            self.details_1.delete(*self.details_1.get_children())
            for i in row_2:
                self.details_1.insert("",END,values=i)
            con_1.commit()
        con_1.close()
       

        


if __name__ == "__main__":
    root=Tk()
    app=Login_page(root)
    root.mainloop()