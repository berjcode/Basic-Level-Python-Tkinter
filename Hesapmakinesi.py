
import math
from tkinter import *
from tkinter import messagebox
from math import *


#İstediğiniz İşlemi  = label - button-fonksiyon sırası ile  düzenli bir şekilde oluşturabilirsiniz.

  #-----------------------Sınıf  Oluşturma ---------------
class HesapMakinesi:
    def __init__(self, win):
    #-----------------------Labeller ve Konumları ---------------
        self.LabelNumber1=Label(window, text='İlk Sayı',font='Times 10 italic')
        self.LabelNumber1.place(x=100, y=50)
        self.LabelNumber2=Label(win, text='İkinci Sayı',font='Times 10 italic')
        self.LabelNumber2.place(x=100, y=75)
        self.LabelResult=Label(win, text='Sonuç',font='Times 10 italic')
        self.LabelResult.place(x=100, y=200)
        self.LabelSingle=Label(win, text='Tekli İşlemler',font='Times 10 italic')
        self.LabelSingle.place(x=100, y=100)
        self.LabelSingle=Label(win, text='Örnek:Sin,Cos,Tanj,karekök,üs alma ',font='Times 10 italic')
        self.LabelSingle.place(x=100, y=120)

        
    #-----------------------Entry'ler---------------------------
        self.t1=Entry()
        self.t1.place(x=200, y=50)
        self.t2=Entry()
        self.t2.place(x=200, y=75)
        self.t3=Entry()
        self.t3.place(x=200, y=200)
        self.LabelSingle=Entry()
        self.LabelSingle.place(x=200, y=100)
    #-----------------------Butonlar ---------------------------
        self.b1=Button(win, text='Topla',  width=4, height=2,bg="#FFDEAD",fg="black",command=self.ToplamaIslemi)
        self.b2=Button(win, text='Çıkart', width=6,height=2,bg="#CD7F32",fg="black",command=self.CikarmaIslemi)
        self.b3=Button(win, text='Çarp',  width=3,height=2,bg="#F5DEB3",fg="black",command=self.CarpmaIslemi)
        self.b4=Button(win, text='Bölme', width=5,height=2,bg="#D8BFD8",fg="black",command=self.BolmeIslemi)
        self.b5=Button(win, text='Kılavuz', width=6,height=2,bg="#FFDB58",fg="black",command=self.KılavuzMesaji)
        self.b6=Button(win, text='karekök', width=6,height=2,bg="#FBCEB1",fg="black",command=self.KarekokIslemi)
        self.b7=Button(win, text='Karesini Al', width=8,height=2,bg="#BDB76B",fg="black",command=self.UsAlmaIslemi)
        self.b8=Button(win, text='Sin', width=3,height=2,bg="#F0DC82",fg="black",command=self.SinIslemi)
        self.b9=Button(win, text='Cos', width=3,height=2,bg="#FBAED2",fg="black",command=self.CosIslemi)
        self.b11=Button(win, text='Tanj', width=3,height=3,bg="#FFFACD",fg="black",command=self.TanjIslemi)
        

     #----------------Butonları Kapatma ve Konum-------------------------------
        self.b1.place(x=50, y=150)#topla butonu 
        self.b2.place(x=88, y=150)#çıkart butonu 
        self.b3.place(x=140, y=150)#çarp butonu
        self.b4.place(x=170, y=150)#bölme butonu
        self.b5.place(x=350, y=250)# Kılavuz Butonu
        self.b6.place(x=210, y=150) #karekök Butonu
        self.b7.place(x=260, y=150)#karesini Alma
    #----------------cossin-------------------------------
        self.b8.place(x=20, y=20)#Sin
        self.b9.place(x=20, y=60)#Cos
        self.b11.place(x=20, y=100)#Tan
    #-----------------Fonksiyonlar Matematiksel İşlemler---------------------------
    def ToplamaIslemi(self):   
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def CikarmaIslemi(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))
    
    def CarpmaIslemi(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1*num2
        self.t3.insert(END, str(result))

    def BolmeIslemi(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1 / num2
        self.t3.insert(END, str(result))

    
    
    def KarekokIslemi(self):
        self.t3.delete(0, 'end')
        num1=float(self.LabelSingle.get())     
        result=sqrt(num1)
        self.t3.insert(END, str(result))

    def UsAlmaIslemi(self):
        self.t3.delete(0, 'end')
        num1=int(self.LabelSingle.get())     
        result=pow(num1,2)
        self.t3.insert(END, str(result))

    def SinIslemi(self):
        self.t3.delete(0, 'end')
        num1=int(self.LabelSingle.get())     
        result=math.sin(num1)
        self.t3.insert(END, str(result))

    def CosIslemi(self):
        self.t3.delete(0, 'end')
        num1=int(self.LabelSingle.get())     
        result=math.cos(num1)
        self.t3.insert(END, str(result))

    
    def TanjIslemi(self):
        self.t3.delete(0, 'end')
        num1=int(self.LabelSingle.get())     
        result=math.tan(num1)
        self.t3.insert(END, str(result))


    #----------------------Diğer Kodlar Kılavuz Uyarı Mesajı -----------------------------------
    def KılavuzMesaji(self):
       res = messagebox.askquestion('Kullanım Kılavuzu ','İlk önce  sayıları giriniz. Girdikten sonra hangi işlemi yapacaksanız(+,-,)  işleme tıklamanız yeterli.\n Tek Girişlik işlemlerinizi Tekli işlemlere girerek yapınız.(Örnek:Sin,Cos,Tanj,karekök,üs alma )\n \n Pencere Kapansın mı? ')
        
    
    
   
#-------------------------- Temel  Başlangıç Kodları --------------------------------

window=Tk()
mywin=HesapMakinesi(window)
window.title(' Basit  Python GUI Hesap Makinesi ')
Etiket = Label(text = "berJ Code \n Teknoloji Yolcusu",fg='black',bg='#ADD8E6',font='Times 15 italic')
Etiket.pack()
window.geometry("400x300+500+100")
window.mainloop()