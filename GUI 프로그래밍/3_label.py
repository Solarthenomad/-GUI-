from tkinter import *

root= Tk()
root.title("Solarthenomad의 GUI")
root.geometry("640X480")

label1 = Label(root, text="안녕하세용")
label1.pack()

photo = PhotoImage(file = "GUI프로그래밍/img.png" )
label2 = Label(root, image= photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    
    global photo2
    photo2 = PhotoImage(file = "GUI프로그래밍/img.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command = change)

root.mainloop()