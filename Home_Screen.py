from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from gps_window import GPS_WINDOW
from all_tabs import ALL_TABS
root = Tk()
root.title("Can-Sat Ground Station GUI")
root.geometry("600x600")
root.configure(background="black")


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class Login:
    def __init__(self, root):
        self.root = root
        frame_login = Frame(self.root, bg="#FFFADA")
        frame_login.place(x=30, y=230, height=340, width=500)
        title = Label(frame_login, text="Login Here", font=(
            "Impact", 35, "bold"), fg="#d77337", bg="#FFFADA").place(x=150, y=20)
        desc = Label(frame_login, text="Welcome to the Can-Sat Software !", font=(
            "Goudy old style", 15, "bold"), fg="#d25d17", bg="#FFFADA").place(x=100, y=100)
        lbl_user = Label(frame_login, text="Username", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="#FFFADA").place(x=80, y=140)
        self.txt_user = Entry(frame_login, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_user.place(x=80, y=170, width=350, height=35)
        lbl_pass = Label(frame_login, text="Password", font=(
            "Goudy old style", 15, "bold"), fg="gray", bg="#FFFADA").place(x=80, y=210)
        self.txt_pass = Entry(frame_login, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=80, y=240, width=350, height=35)
        login_btn = Button(self.root, command=self.login_function, text="Login", fg="white", bg="#d77337", font=(
            "times new roman", 20)).place(x=180, y=550, width=180, height=40)

    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        elif self.txt_pass.get() != "1" or self.txt_user.get() != "1":
            messagebox.showerror(
                "Error", "Invalid Username/Password", parent=self.root)
        else:
            root.withdraw()
            # gps_window = GPS_WINDOW(root)
            all_tabs=ALL_TABS(root)


class win_title:
    def __init__(self, root):
        self.root = root
        frame_title = Frame(self.root, bg="#FFFADA")
        frame_title.place(x=700, y=250, height=60, width=480)
        title = Label(frame_title, text="Can-Sat Flight Software", font=("Impact",
                      30, "bold"), fg="#d77337", bg="#FFFADA").place(x=46, y=5)
        frame_name = Frame(self.root, bg="#FFFADA")
        frame_name.place(x=750, y=350, height=60, width=300)
        title = Label(frame_name, text="School of ECE", font=(
            "Impact", 30, "bold"), fg="#d77337", bg="#FFFADA").place(x=40, y=6)
        copyright = u"\u00A9"
        font1 = ("times", 15, "normal")
        l1 = Label(self.root, text=f'{copyright} Satyam Morankar & Rohan Habu', font=font1).place(
            x=600, y=600)


e = Example(root)
e.pack(fill=BOTH, expand=YES)
set_title = win_title(root)
obj = Login(root)
root.mainloop()
