import tkinter as tk
ekran = tk.Tk()
ekran.title("Hipotenüs Calculate Program")
ekran.resizable(height = False , width = False)
ekran.geometry("500x500")
font=("Comic Sans MS",16)
yazı = tk.Label(text = "Hypotenuse Calculate",font=font)
yazı.pack()

akare = tk.Label(text = "Edge A",font=font)
akare.place(x = "20",y="80")

a = tk.Entry(font=font)
a.place(x = "20",y="120")

bekare = tk.Label(text = "Edge B",font=font)
bekare.place(x = "20",y="180")

b = tk.Entry(font=font)
b.place(x = "20",y="220")


def hesapla ():
    w = float(a.get())
    x = float(b.get())
    endeks = (w**2 + x**2 ) **0.5
    yazı.configure(text = "Hypotenuse: {}".format(endeks))


bul = tk.Button(text = "Calculate",font=font,command=hesapla)
bul.place(x = "20",y="290")
ekran.mainloop()
