from tkinter import *
from tkinter import messagebox
import pytube
import time
import os
import pyglet
#Fonts
pyglet.font.add_file('UnifrakturCook-Bold.ttf')
#Functions
def handle_focus_in(_):
    e2.delete(0, END)
    e2.config(fg='black')

def handle_focus_out(_):
    e2.delete(0,END)
    e2.config(fg='gray')
    e2.insert(0, "Author - title")

def handle_enter(txt):
    print(e2.get())
    handle_focus_out('dummy')

def downloadAudio():
    video_url = url.get()
    video_name = nazwapliku.get()
    sciezkaNowa = sciezkaUserInput.get()
    if not sciezkaUserInput.get():
        with open('path.txt', 'r') as file:
            path = file.read()
    else:
        with open('path.txt','w') as file:
            file.write(sciezkaNowa)
            file.close()
        with open('path.txt', 'r') as file:
            path = file.read()
    a,b = video_name.split('-')
    a = " ".join(a.split())
    sciezka = os.path.join(path,a)
    if not os.path.exists(sciezka):
        os.mkdir(sciezka)
    try:
        print(sciezka)
        youtube = pytube.YouTube(video_url)
        video =  youtube.streams.filter(only_audio=True).all()
        video[0].download(output_path=sciezka,filename=video_name)
        msg = my_canvas.create_text(250,440,fill="green",text='Download complete',font=("Calibri",12))
        master.after(2000, my_canvas.delete, msg)
    except Exception as f:
        print(f)
        msg = my_canvas.create_text(250,440,fill="red",text='Video could not be downloaded',font=("Calibri",12))
        master.after(2000, my_canvas.delete, msg)


def downloadLow():
    video_url = url.get()
    video_name = nazwapliku.get()
    sciezkaNowa = sciezkaUserInput.get()
    if not sciezkaUserInput.get():
        with open('path.txt', 'r') as file:
            path = file.read()
    else:
        with open('path.txt','w') as file:
            file.write(sciezkaNowa)
            file.close()
        with open('path.txt', 'r') as file:
            path = file.read()
    a,b = video_name.split('-')
    a = " ".join(a.split())
    sciezka = os.path.join(path,a)
    if not os.path.exists(sciezka):
        os.mkdir(sciezka)
    try:
        print(sciezka)
        youtube = pytube.YouTube(video_url)
        video =  youtube.streams.first()
        video.download(output_path=sciezka,filename=video_name)
        msg = my_canvas.create_text(250,440,fill="green",text='Download complete',font=("Calibri",12))
        master.after(2000, my_canvas.delete, msg)
    except Exception as f:
        print(f)
        msg = my_canvas.create_text(250,440,fill="red",text='Video could not be downloaded',font=("Calibri",12))
        master.after(2000, my_canvas.delete, msg)

def downloadHigh():
    video_url = url.get()
    video_name = nazwapliku.get()
    sciezkaNowa = sciezkaUserInput.get()
    if not sciezkaUserInput.get():
        with open('path.txt', 'r') as file:
            path = file.read()
    else:
        with open('path.txt','w') as file:
            file.write(sciezkaNowa)
            file.close()
        with open('path.txt', 'r') as file:
            path = file.read()
    a,b = video_name.split('-')
    a = " ".join(a.split())
    sciezka = os.path.join(path,a)
    if not os.path.exists(sciezka):
        os.mkdir(sciezka)
    try:
        print(sciezka)
        youtube = pytube.YouTube(video_url)
        video =  youtube.streams.get_highest_resolution()
        video.download(output_path=sciezka,filename=video_name)
        msg = my_canvas.create_text(250,440,fill="green",text='Download complete',font=("Calibri",12))
        master.after(2000, my_canvas.delete, msg)
    except Exception as f:
        print(f)
        msg = my_canvas.create_text(250,440,fill="red",text='Video could not be downloaded',font=("Calibri",12))
        master.after(2000, my_canvas.delete, msg)

#Main Screen
master = Tk()
master.title("Youtube Video Downloader")


#background_image
bg= PhotoImage(file='grafika2.png')

#create a Canvas
my_canvas = Canvas(master, width=500, height=500)
my_canvas.grid(sticky=NSEW)

#Set image in Canvas
my_canvas.create_image(0,0,image=bg,anchor="nw")


#Label
my_canvas.create_text(250,20,text="Youtube Video Converter",font=("UnifrakturCook-Bold",15),fill="Green")
my_canvas.create_text(250,60,text="Please enter your youtube video link below:",font=("Calibri",12),fill="white")
my_canvas.create_text(250,140,text="Please enter name of the saved video:",font=("Calibri",12),fill="white")
my_canvas.create_text(250,220,text="Please path where you want to store your music (only once):",font=("Calibri",12),fill="white")


#Var
url = StringVar()
nazwapliku = StringVar()
sciezkaUserInput = StringVar()

#Entry
e1=Entry(master,width=50,textvariable=url)
my_canvas.create_window(250,100,window=e1)

e2=Entry(textvariable=nazwapliku,width=50 ,bg='white',fg='black')
my_canvas.create_window(250,180,window=e2)

e3 = Entry(master,width=50,textvariable=sciezkaUserInput)
my_canvas.create_window(250,260,window=e3)

#Button
b1 = Button(master,width=30,text="Download only audio",bg="#03fce8",font=("Calibri",12),command=downloadAudio)
my_canvas.create_window(250,300,window=b1)

b2 = Button(master,width=30,text="Download in low resolution",bg="green",font=("Calibri",12),command=downloadLow)
my_canvas.create_window(250,350,window=b2)

b3 = Button(master,width=30,text="Download in high resolution",bg="orange",font=("Calibri",12),command=downloadHigh)
my_canvas.create_window(250,400,window=b3)


master.mainloop()
