from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox


def acction():
    link = video_url.get()
    video = YouTube(link)
    stream = video.streams.filter(res="1080p", fps=60).first()

    if stream:
        stream.download()
    else:
        MessageBox.showerror("Error", "Not found video 1080p y 60 FPS.")
        video = YouTube(link)
        download = video.streams.get_highest_resolution()
        download.download()
def popup():
    MessageBox.showinfo("about me", "")


root = Tk()
root.config(bd=15)
root.title("video downloader")

image = PhotoImage(file="yt.png")
foto = Label(root, image=image, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="more info", menu=helpmenu)
helpmenu.add_command(label="author infor", command=popup)
# Usa root.quit en lugar de root.destroy
menubar.add_command(label="salir", command=root.quit)

instructions = Label(root, text="  py program")
instructions.grid(row=0, column=1)

# Cambia el nombre del campo de entrada de texto a video_url
video_url = Entry(root)
video_url.grid(row=1, column=1)

boton = Button(root, text="Download button", command=acction)
boton.grid(row=2, column=1)

root.mainloop()
