from tkinter import *
import socket
from tkinter import filedialog
import os

root = Tk()
root.title("Share it")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)


#icon
image_icon = PhotoImage(file="fileimages/icon.png")
root.iconphoto(False, image_icon)

Label(root, text="File Transfer",font=("Acumin Variable Concept", 20,'bold'),bg="#f4fdfe").place(x=20,y=30)

Frame(root, width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image = PhotoImage(file="fileimages/send.png")
send = Button(root, image=send_image, bg="#f4fdfe",bd=0)
send.place(x=50, y=100)

receive_image = PhotoImage(file="fileimages/receive.png")
receive = Button(root, image=receive_image, bg="#f4fdfe",bd=0)
receive.place(x=300, y=100)

#Label

Label(root, text="Send", font=("Acumin Variable Concept", 17, 'bold'), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=("Acumin Variable Concept", 17, 'bold'), bg="#f4fdfe").place(x=300, y=200)


background = PhotoImage(file="fileimages/background.png")
Label(root,image=background).place(x=-2,y=323)


root.mainloop()