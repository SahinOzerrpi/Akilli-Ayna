from tkinter import *
import time
import locale
import requests
import traceback
import feedparser
import random
from PIL import Image, ImageTk

class Acilis(Toplevel):
    def __init__(self, parent):
        # print("Here")
        Toplevel.__init__(self, parent)
        self.title("AKILLI AYNA")
        self.configure(background='black')
        self.geometry("600x600")
        resim = Image.open("gorseller/akıllıayna.png")
        resim = resim.resize((600, 600), Image.ANTIALIAS)
        resim = resim.convert('RGB')
        fotograf = ImageTk.PhotoImage(resim)

        self.resimLbl = Label(self, bg='black', image=fotograf)
        self.resimLbl.image = fotograf
        self.resimLbl.pack(side=TOP, anchor=CENTER)
        # self.topFrame = Frame(self.tk, background='black')

        ## required to make window show before the program gets to the mainloop
        self.update()

class Selamlama(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,bg='black')
        iltifatlar = ['Bugün Çok Harikasın','Mükemmel Görünüyorsun','Harikasın','Mükemmelsin']
        self.text1 = Label(self, compound = CENTER, text= "", font=("Calibri", 45), fg="white", background="black")
        self.text1.pack()
        #function to choose random verse to display
        def on_after():
            randomverse=random.choice(iltifatlar)
            self.text1.configure(text=randomverse)
            self.text1.after(8000,on_after)
        #updates text every 5 seconds
        self.text1.after(8000,on_after)

class Saat(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='black')
        self.saat3 = ''
        self.saat3Lbl = Label(self,font=("Times", 35),bg="black",fg="grey")
        self.saat3Lbl.pack(side=RIGHT, anchor=NE)
        self.saat1 = ''
        self.saatLbl = Label(self,font=("Times", 55),bg="black",fg="white")
        self.saatLbl.pack(side=LEFT, anchor=N)
        self.saat_parametre()

    def saat_parametre(self):
            saat2 = time.strftime('%H:%M')
            saat3 = time.strftime('%S')
            if saat2 != self.saat1:
                self.saat1 = saat2
                self.saatLbl.config(text=saat2)
            if saat3 != self.saat3:
                self.saat3 = saat3
                self.saat3Lbl.config(text=saat3)          
            self.saatLbl.after(200, self.saat_parametre)

class Tarih(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='black')
        self.tarih1 = ''
        self.tarihLbl = Label(self, text=self.tarih1,font=("Times", 35),bg="black",fg="grey")
        self.tarihLbl.pack(side=TOP, anchor=W)
        self.tarih_parametre()

    def tarih_parametre(self):
        locales = ['tr']
        for loc in locales:
            locale.setlocale(locale.LC_ALL, loc)
            tarih2 = time.strftime('%A, %d %B %Y')     
            if tarih2 != self.tarih1:
                self.tarih1 = tarih2
                self.tarihLbl.config(text=tarih2)
            self.tarihLbl.after(60000, self.tarih_parametre)


class Hava_Durumu(Frame):
    def __init__(self, root):
        Frame.__init__(self, bg='black')
        self.root=root
        self.arama_resim=Image.open("gorseller/arama.png")
        self.arama_resim=self.arama_resim.resize((20,20),Image.ANTIALIAS)
        self.arama_resim=ImageTk.PhotoImage(self.arama_resim)
        self.var_arama=StringVar()  
        baslik=Label(self.root,text="Hava Durumu",font=("Calibri", 25),bg="black",fg="gray").place(x=680,y=5,relwidth=0.2,height=60)
        lbl_sehir=Label(self.root,text="Şehir Ara :",font=("Calibri", 15),bg="black",fg="gray",anchor="w",padx=5).place(x=600,y=50,relwidth=1,height=40)
        txt_sehir=Entry(self.root,textvariable=self.var_arama,font=("Calibri"),bg="black",fg="white",bd=2).place(x=700,y=58,width=150,height=25)
        btn_arama=Button(self.root,cursor="hand2",image=self.arama_resim,bg="black",activebackground="#033958",bd=0,command=self.get_weather).place(x=870,y=55,width=25,height=30)


        self.lbl_sehir=Label(self.root,text="Konum",font=("Calibri"),bg="black",fg="white")
        self.lbl_sehir.place(x=270,y=110,relwidth=1,height=20)

        self.lbl_havadurumu=Label(self.root,text="Hava Durumu",font=("Calibri"),bg="black",fg="white")
        self.lbl_havadurumu.place(x=765,y=110,width=88,height=20)

        self.lbl_resim=Label(self.root,text="Resim",font=("Calibri"),bg="black",fg="white")
        self.lbl_resim.place(x=630,y=135,width=115,height=100)

        self.lbl_derece=Label(self.root,text="Derece",font=("Calibri", 35),bg="black",fg="white")
        self.lbl_derece.place(x=750,y=135,width=150,height=100)

        self.lbl_hata=Label(self.root,text="Hata",font=("Calibri"),bg="black",fg="red")
        self.lbl_hata.place(x=320,y=245,relwidth=1,height=20)

    def get_weather(self):
        api_key="15f25de1f110b27b1185dc7a0ffc60e4"
        complete_url=f"http://api.openweathermap.org/data/2.5/weather?q={self.var_arama.get()}&appid={api_key}"     
        if self.var_arama.get()=="":
            self.lbl_hata.config(text="Şehir Adı Girmelisiniz")
        else:     
            result=requests.get(complete_url)
            if result:
                json=result.json()
                sehir_name=json["name"]
                ülke=json["sys"]["country"]
                resim=json["weather"][0]["icon"]
                derece_c=json["main"]["temp"]-273.15

                self.lbl_sehir.config(text=sehir_name+" , "+ülke)

                self.arama_resim2=Image.open(f"gorseller/{resim}.png")
                self.arama_resim2=self.arama_resim2.resize((80,80),Image.ANTIALIAS)
                self.arama_resim2=ImageTk.PhotoImage(self.arama_resim2)

                self.lbl_resim.config(image=self.arama_resim2)
                deg=u"\N{DEGREE SIGN}"
                self.lbl_derece.config(text=str(round(derece_c,2))+deg+"C")
                self.lbl_hata.config(text="")

            else:
                self.lbl_sehir.config(text="")
                self.lbl_resim.config(image="")
                self.lbl_resim.config(text="")
                self.lbl_derece.config(text="")
                self.lbl_hata.config(text="Şehir İsmi Bulunamadı")

            self.after(600000, self.get_weather)

class Haberler(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.config(bg='black')
        self.baslik = 'Haberler'
        self.haberLbl = Label(self, text=self.baslik, font=("Calibri", 35),bg="black",fg="white")
        self.haberLbl.pack(side=TOP, anchor=W)
        self.mansetler = Frame(self, bg="black")
        self.mansetler.pack(side=TOP)
        self.get_headlines()

    def get_headlines(self):
        news_country_code = 'TR_tr'
        try:
            for widget in self.mansetler.winfo_children():
                widget.destroy()
            if news_country_code == None:
                haber_url = "https://news.google.com/news?ned=us&output=rss"
            else:
                haber_url = "https://news.google.com/news?ned=%s&output=rss" % news_country_code

            feed = feedparser.parse(haber_url)

            for post in feed.entries[0:5]:
                haber = HManset(self.mansetler, post.title)
                haber.pack(side=TOP, anchor=W)
        except Exception as e:
            traceback.print_exc()
            print ("Hata: %s. Haberlere ulaşılamıyor." % e)

        self.after(600000, self.get_headlines)


class HManset(Frame):
    def __init__(self, parent, Habery=""):
        Frame.__init__(self, parent, bg='black')

        resim = Image.open("gorseller/haber.png")
        resim = resim.resize((25, 25), Image.ANTIALIAS)
        resim = resim.convert('RGB')
        fotograf = ImageTk.PhotoImage(resim)

        self.resimLbl = Label(self, bg='black', image=fotograf)
        self.resimLbl.image = fotograf
        self.resimLbl.pack(side=LEFT, anchor=N)

        self.Habery = Habery
        self.HaberyLbl = Label(self, text=self.Habery, font=("Calibri", 16),bg="black",fg="white")
        self.HaberyLbl.pack(side=LEFT, anchor=N)

class FullscreenWindow:
    def __init__(self):
        self.tk = Tk() 
        self.tk.title("Akıllı Ayna")
        self.tk.configure(background="black")
        self.topFrame = Frame(self.tk, background="black")
        self.bottomFrame = Frame(self.tk, background="black")
        self.rightFrame = Frame(self.tk, background="black")
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)
        self.rightFrame.pack(side=RIGHT, fill=BOTH, expand=YES, anchor=N)
        self.topFrame.pack(side=TOP, fill=BOTH, expand=YES)
        self.state = True
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.config(cursor='none')
        self.start = Selamlama(self.bottomFrame)
        self.start.pack(side=TOP, anchor=N, padx=0, pady=0) 
        self.tarih = Tarih(self.topFrame)
        self.tarih.pack(side=TOP, anchor=NW, padx=0, pady=0)
        self.saat = Saat(self.topFrame)
        self.saat.pack(side=TOP, anchor=NW, padx=0, pady=0)
        self.havadurumu = Hava_Durumu(self.rightFrame)
        self.havadurumu.pack(side=TOP, anchor=W, padx=0, pady=0)
        self.haberler = Haberler(self.bottomFrame)
        self.haberler.pack(side=LEFT, anchor=S, padx=0, pady=0)
        self.tk.withdraw()
        acilis = Acilis(self.tk)
        #simulate a delay while loading
        time.sleep(6)
        acilis.destroy()
        self.tk.deiconify()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.tk.attributes("-fullscreen", self.state)
        return "break"

if __name__ == '__main__':
    w = FullscreenWindow()
    w.tk.mainloop()