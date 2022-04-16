from tkinter import *
from click import command
import pandas as pd
from tkinter import ttk


class window_utils:
    def set_heading(window):
        label = Label(window, text="CANSAT FLIGHT SOFTWARE", font=(
            "Arial", int(int(window.winfo_screenheight())/30), "bold"), bg='white').pack(pady=5)

    def set_window_background(window):
        bg = PhotoImage(file='./images/bg.jpg')
        canvas = Canvas(window, width=int(window.winfo_screenwidth()),
                        height=int(window.winfo_screenheight()))
        canvas.pack(fill="both", expand=True, padx=10, pady=10)
        canvas.create_image(0, 0, image=bg, anchor='nw')
        pass

    def insert_logo(window):
        img = PhotoImage(file='./images/mit_logo.png')
        lbl = Label(window, image=img, text='')
        lbl.pack()

    def bring_screen_to_center(window):
        window_width = int(window.winfo_screenwidth())
        window_height = int(window.winfo_screenheight())
        center_x = int((window.winfo_screenwidth()-window_width)/2)
        center_y = int((window.winfo_screenheight()-window_height)/2)
        window.geometry(
            f'{window_width}x{window_height}+{center_x}+{center_y}')
        window.state('zoomed')
        window.resizable(False, False)
        window.config(background='white')
        return window_width, window_height

    def read_data():
        data = pd.DataFrame(pd.read_csv('./CanSat_DHT11.csv')).dropna()
        temperature_c = data['Temp C']
        temperature_f = data['Temp F']
        humidity = data['Humidity %']
        heat_index_c = data['HeatIndex C']
        heat_index_f = data['HeatIndex F']
        return data, temperature_c, temperature_f, humidity, heat_index_c, heat_index_f

    def create_drop_down(window, options):
        drop_val = StringVar()
        dropdown = ttk.Combobox(window, width=27,height=5, textvariable=drop_val)
        dropdown['values'] = options
        dropdown.current(0)
        dropdown.pack()
        return dropdown
    
    def close_btn_clicked(CURRENT_SCREEN,PREVIOUS_SCREEN):
            CURRENT_SCREEN.destroy()
            PREVIOUS_SCREEN.deiconify()
            window_utils.bring_screen_to_center(PREVIOUS_SCREEN)
            pass
    def create_frame(window):
        frame = Frame(window, background='white')
        frame.pack(side=TOP)
        frame.config(width=int(window.winfo_screenwidth()), height=int(window.winfo_screenheight())/10)
        return frame
    def add_image(window,image):
        img_lbl=Label(window,image=image)
        img_lbl.pack(padx=5,pady=5)
        img_lbl.config(bg="white")
