from tkinter import *
from window_utilities import window_utils
from PIL import ImageTk

window = Tk()
window_utils.bring_screen_to_center(window)
window_utils.set_heading(window)
# window_utils.insert_logo(window)
img = ImageTk.PhotoImage(file='./images/mit_logo.png')
window_utils.add_image(window=window,image=img)
window_width = int(window.winfo_screenwidth())
# window_width = 640
window_height = int(window.winfo_screenheight())
# window_height = 480
options = ['Home', 'Payload', 'GPS', 'Plot']

LATITUDE_FRAME=window_utils.create_frame(window=window)

LONGITUDE_FRAME=window_utils.create_frame(window=window)

latitude_lbl = Label(LATITUDE_FRAME, text='LATITUDE', anchor=E)
latitude_lbl.config(font=('Arial', int(window_height/45)),
                    borderwidth=2, width=int(window_width/100), background='white')
latitude_lbl.pack(anchor=CENTER, side=LEFT)

latitude_lbl_VAL = Label(LATITUDE_FRAME, text='VALUE'+' LATITUDE')
latitude_lbl_VAL.config(font=('Arial', int(window_height/45)),
                        borderwidth=2, relief=GROOVE, width=int(window_width/100), background='white')
latitude_lbl_VAL.pack(anchor=CENTER, side=LEFT)
spacer = Label(LATITUDE_FRAME, width=int(window_width), background='white')
spacer.pack(anchor=CENTER, side=LEFT, pady=int(window_height/20))

longitude_lbl = Label(LONGITUDE_FRAME, text='LONGITUDE', anchor=E)
longitude_lbl.config(font=('Arial', int(window_height/45)),
                     borderwidth=2, width=int(window_width/100), background='white')
longitude_lbl.pack(anchor=CENTER, side=LEFT)

longitude_lbl_VAL = Label(LONGITUDE_FRAME, text='VALUE'+' LONGITUDE')
longitude_lbl_VAL.config(font=('Arial', int(window_height/45)),
                         borderwidth=2, relief=GROOVE, width=int(window_width/100), background='white')
longitude_lbl_VAL.pack(anchor=CENTER, side=LEFT)
spacer = Label(LONGITUDE_FRAME, width=int(window_width), background='white')
spacer.pack(anchor=CENTER, side=LEFT)


window.mainloop()
