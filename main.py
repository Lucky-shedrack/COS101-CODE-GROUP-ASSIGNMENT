from tkinter import ttk
import tkinter

m = []

def chocks():
    d = ['; ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','p','q','r',' s','t','u','v','w','x','y','z']
    k = ['EMPTY SPACE','Har Tomdoo Paradise', 'Tyavzua Joy Iember', 'Ulaga Benedict Ulaga', 'Gabriel Flourish', 'David Samuel Ngbede',
         'Iorchivir Mark Tavershima', 'Sunday Divine', 'Anderson Wisdom Chinemerem', 'Akoso Pelumi David',
         'Onah Love Ene', 'Adoga Gideon', 'Desmond', 'Akoso David Keghtor']



    code = input('Enter Your Code: ')

    for d, k in zip(d, k):

        if code in m:
            root = tkinter.Tk()
            l1 = ttk.Label(text='already entered', style="BW.TLabel", font='bobo 100', background="red")
            l1.pack()
            root.maxsize(1000, 300)
            root.minsize(1000, 300)
            root.mainloop()

            break

        if code in d:
            root = tkinter.Tk()
            l1 = ttk.Label(text=k, style="BW.TLabel", font='bobo 70', background="green")
            l1.pack()

            root.maxsize(1000, 100)
            root.minsize(1000, 100)
            root.mainloop()
            break

    for k, d in zip(k, d):
        if code in m:
            root = tkinter.Tk()
            l1 = ttk.Label(text='already entered', style="BW.TLabel", font='bobo 70', background="red")
            l1.pack()
            root.maxsize(1000, 100)
            root.minsize(1000, 100)
            root.mainloop()

            break
        if code not in d:
            root = tkinter.Tk()
            l1 = ttk.Label(text='Not in existence', style="BW.TLabel", font='bobo 100', background="red")
            l1.pack()
            root.maxsize(1000, 200)
            root.minsize(1000, 200)
            root.mainloop()
            break
    m.append(code)


while True:
    chocks()

