from tkinter import *
window=Tk()
window.title("1ST GUI")
window.geometry("300x200")
label=Label(window,text="hii,i am TAPS",fg="red",bg="yellow")
label.pack(side=TOP)
button=Button(window,text="click button",fg="red",bg="gray")
button.pack()
window.mainloop()