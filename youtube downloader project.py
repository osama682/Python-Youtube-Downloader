from tkinter import *
from pytube import YouTube
from tkinter import messagebox
window = Tk()
window.title("Youtube downloader")
window.geometry("450x230")

def link():
    video = YouTube(flinkvalue.get()).streams.first().download()
    messagebox.showinfo("Done","Successfully Download")
    video.download("C:/Users/Osis/PycharmProjects/firstproject")

Label(window, text="Welcome to youtube video downloader", fg = "Brown", font = "lucida 15 bold").grid(row = 0, pady = 10,padx = 20)
f1 = Label(window,text = "Enter your link below : ",font = "lucida 13 bold")
f1.grid(row = 1,pady = 15)

flinkvalue = StringVar()
linkentry = Entry(window,textvariable = flinkvalue,width = 60,)
linkentry.grid(row = 2,padx = 30)

Button(window,text = "Click here to download",command = link,bg = "lightgrey").grid(row = 3,pady = 15)

window.mainloop()
