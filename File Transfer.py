from tkinter import *
import socket
from tkinter import filedialog
import os

root = Tk()
root.title("Share it")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)


def receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)


    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        s = socket.socket()
        port = 8081
        s.connect((ID, port))
        file = open(filename1, 'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()

        print("File has been received successfully")



    image_icon1 = PhotoImage(file="fileimages/receive.png")
    main.iconphoto(False, image_icon1)

    Hbackground = PhotoImage(file="fileimages/receiver.png")
    Label(main, image=Hbackground).place(x=-2,y=0)


    logo = PhotoImage(file="fileimages/profile.png")
    Label(main,image=logo,bg="#f4fdfe").place(x=10,y=250)

    Label(main, text="Receive", font=('arial',20),bg="#f4fdfe").place(x=20,y=340)


    SenderID = Entry(main,width=25,fg='black', border=2,bg='white', font=('arial',15))
    SenderID.place(x=20,y=370)

    SenderID.focus()

    Label(main, text="filename for the incoming file",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20, y=420)
    incoming_file = Entry(main, width=25, fg="black", border=2, bg="white", font=('arial',15))
    incoming_file.place(x=20, y=450)


    imageicon = PhotoImage(file="fileimages/arrow.png")
    rr = Button(main, text="Receive", compound=LEFT, image=imageicon, width=130, bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20, y=500)



    main.mainloop()


def send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Text file", filetypes=(("file_type","*.txt"),('all files','*.*')))


    def sender():
        s = socket.socket()
        host = socket.gethostname()
        port = 8081
        s.bind((host, port))
        s.listen(1)
        print(host)

        print("Waiting for any incoming connections....")
        conn, addr = s.accept()


        file = open(filename, 'rb')
        file_data = file.read(1024)
        conn.send(file_data)

        print("Data has been successfuly Transmitted")

    #ICON
    image_icon1 = PhotoImage(file="fileimages/send.png")
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file="fileimages/sender.png")
    Label(window, image=Sbackground).place(x=-2, y=0)

    Mbackground = PhotoImage(file="fileimages/id.png")
    Label(window, image=Mbackground,bg="#f4fdfe").place(x=100, y=260)

    host = socket.gethostname()
    Label(window, text=f"ID: {host}",bg="white",fg="black").place(x=140,y=290)

    Button(window, text="+ select file", width=10,height=1, font="arial 14 bold", bg="#fff", fg="#000", command=select_file).place(x=160, y=150)

    Button(window, text="SEND", width=8, height=1, font="arial 14 bold", bg="#fff", fg="#000",command=sender).place(x=300,y=150)


    window.mainloop()


#icon
image_icon = PhotoImage(file="fileimages/icon.png")
root.iconphoto(False, image_icon)

Label(root, text="File Transfer",font=("Acumin Variable Concept", 20,'bold'),bg="#f4fdfe").place(x=20,y=30)

Frame(root, width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image = PhotoImage(file="fileimages/send.png")
send = Button(root, image=send_image, bg="#f4fdfe",bd=0, command=send)
send.place(x=50, y=100)


receive_image = PhotoImage(file="fileimages/receive.png")
receive = Button(root, image=receive_image, bg="#f4fdfe",bd=0, command=receive)
receive.place(x=300, y=100)

#Label

Label(root, text="Send", font=("Acumin Variable Concept", 17, 'bold'), bg="#f4fdfe", fg="#000").place(x=65, y=200)
Label(root, text="Receive", font=("Acumin Variable Concept", 17, 'bold'), bg="#f4fdfe").place(x=300, y=200)


background = PhotoImage(file="fileimages/background.png")
Label(root,image=background).place(x=-2,y=323)


root.mainloop()