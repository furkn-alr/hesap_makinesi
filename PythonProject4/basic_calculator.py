import tkinter as tk

form = tk.Tk()
form.title("Basic Calculator")
form.geometry("450x445+450+150")
form.resizable(False, False)
etk1 = tk.Label(form, text="     ", bg="black", fg="white", font="italic 30 bold")
etk1.pack()
etk1.place(x= 0, y = 0, width= 450, height= 150)
islem = ""

def bir():
    global islem
    islem += str(1)
    etk1.config(text=islem)
but1= tk.Button(form, text="1", bg="grey", fg="white", font="italic 20 bold", command=bir)
but1.pack()
but1.place(x= 15, y = 160, width= 70, height= 80)

def iki():
    global islem
    islem += str(2)
    etk1.config(text=islem)
but2= tk.Button(form, text="2", bg="grey", fg="white", font="italic 20 bold", command=iki)
but2.pack()
but2.place(x= 100, y = 160, width= 70, height= 80)

def uc():
    global islem
    islem += str(3)
    etk1.config(text=islem)
but3= tk.Button(form, text="3", bg="grey", fg="white", font="italic 20 bold", command=uc)
but3.pack()
but3.place(x= 185, y = 160, width= 70, height= 80)

def dort():
    global islem
    islem += str(4)
    etk1.config(text=islem)
but1= tk.Button(form, text="4", bg="grey", fg="white", font="italic 20 bold", command=dort)
but1.pack()
but1.place(x= 15, y = 255, width= 70, height= 80)

def bes():
    global islem
    islem += str(5)
    etk1.config(text=islem)
but5= tk.Button(form, text="5", bg="grey", fg="white", font="italic 20 bold", command=bes)
but5.pack()
but5.place(x= 100, y = 255, width= 70, height= 80)

def alti():
    global islem
    islem += str(6)
    etk1.config(text=islem)
but6= tk.Button(form, text="6", bg="grey", fg="white", font="italic 20 bold", command=alti)
but6.pack()
but6.place(x= 185, y = 255, width= 70, height= 80)

def yedi():
    global islem
    islem += str(7)
    etk1.config(text=islem)
but7= tk.Button(form, text="7", bg="grey", fg="white", font="italic 20 bold", command=yedi)
but7.pack()
but7.place(x= 15, y = 350, width= 70, height= 80)

def sekiz():
    global islem
    islem += str(8)
    etk1.config(text=islem)
but8= tk.Button(form, text="8", bg="grey", fg="white", font="italic 20 bold", command=sekiz)
but8.pack()
but8.place(x= 100, y = 350, width= 70, height= 80)

def dokuz():
    global islem
    islem += str(9)
    etk1.config(text=islem)
but9= tk.Button(form, text="9", bg="grey", fg="white", font="italic 20 bold", command=dokuz)
but9.pack()
but9.place(x= 185, y = 350, width= 70, height= 80)

def sifir():
    global islem
    islem += str(0)
    etk1.config(text=islem)
but0 = tk.Button(form, text="0", bg="grey", fg="white", font="italic 20 bold", command=sifir)
but0.pack()
but0.place(x= 270, y = 350, width= 70, height= 80)

def esit():
        global islem
        try:
            sonuc = eval(islem)
            etk1.config(text=str(sonuc))
            islem = str(sonuc)  # Sonucu sonraki işlemlerde kullanmak istersen
        except Exception as e:
            etk1.config(text="Hata")
            islem = ""
but10 = tk.Button(form, text="=", bg="orange", fg="white", font="italic 20 bold", command=esit)
but10.pack()
but10.place(x= 355, y = 350, width= 70, height= 80)

def arti():
    global islem
    islem += "+"
    etk1.config(text=islem)
isl1 = tk.Button(form, text="+", bg="orange", fg="white", font="italic 20 bold", command=arti)
isl1.pack()
isl1.place(x= 270, y = 160, width= 70, height= 80)

def eksi():
    global islem
    islem += "-"
    etk1.config(text=islem)
isl2 = tk.Button(form, text="-", bg="orange", fg="white", font="italic 20 bold", command=eksi)
isl2.pack()
isl2.place(x= 355, y = 160, width= 70, height= 80)

def bolme():
    global islem
    islem += "/"
    etk1.config(text=islem)
isl3 = tk.Button(form, text="/", bg="orange", fg="white", font="italic 20 bold", command=bolme)
isl3.pack()
isl3.place(x= 270, y = 255, width= 70, height= 80)

def carpma():
    global islem
    islem += "*"
    etk1.config(text=islem)
isl4 = tk.Button(form, text="*", bg="orange", fg="white", font="italic 20 bold", command=carpma)
isl4.pack()
isl4.place(x= 355, y = 255, width= 70, height= 80)

def sil():
    global islem
    islem = ""
    etk1.config(text=islem)
isl5 = tk.Button(form, text="C", bg="pink", fg="white", font="italic 20 bold", command=sil)
isl5.pack()
isl5.place(x= 35, y = 38, width= 70, height= 80)

def sil2():
    global islem
    islem = islem[:-1]
    etk1.config(text=islem)
isl6 = tk.Button(form, text="D", bg="pink", fg="white", font="italic 20 bold", command=sil2)
isl6.pack()
isl6.place(x= 355, y = 38, width= 70, height= 80)
form.mainloop()
