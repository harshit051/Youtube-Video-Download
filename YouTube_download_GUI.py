from pytube import YouTube
import os
from tkinter import *
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Harshit Srivastava YouTube Video Downloader")
Label(root,text = "YouTube Video Downloader",font = 'arial 20 bold').pack()
link = StringVar()
Label(root,text = 'Enter your link ' ,font = 'arial 15').place(x = 150,y = 50)
link_entry = Entry(root,width = 50,textvariable = link).place(x = 30,y = 90)
print(os.path.join(os.environ["HOMEPATH"],"Downloads"))
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download(os.path.join(os.environ["HOMEPATH"], "Downloads"))
    Label(root,text = 'Downloaded!! ' ,font = 'arial 20 bold').place(x = 180,y = 210)
Button(root,text = 'Download',font ='arial 20 bold',bg = 'pale violet red',padx = 2,command = Downloader).place(x = 180,y = 150)
root.mainloop()
