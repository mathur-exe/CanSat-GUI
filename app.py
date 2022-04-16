import tkinter as tk

from numpy import imag
from PIL import ImageTk, Image

window = tk.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
# getting the center point of the screen for placing window at center
x_Left = int(window.winfo_screenwidth()/2 - width/2)
y_Top = int(window.winfo_screenheight()/2 - height/2)
window.geometry(f'{width}x{height}+{x_Left}+{y_Top}')
window.resizable(False, False)
window.state('zoomed')
window.config(bg='white')
# window.configure(background='blue')
options = ['Home', 'Payload', 'GPS', 'Plot']
text_format = tk.StringVar()
text_format.set('Home')
drop = tk.OptionMenu(window, text_format, *options)
drop.pack()
drop.config(width=30,height=2,bg='white')
window.mainloop()

