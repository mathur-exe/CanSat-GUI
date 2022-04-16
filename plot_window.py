import threading
from time import sleep
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

from window_utilities import window_utils


class PLOT_SCREEN:
    def __init__(self, PREVIOUS_SCREEN):
        def change_screen(event):
            print(event.widget.get())
            pass
        
        plt_screen = Toplevel(PREVIOUS_SCREEN)
        plt_screen.protocol('WM_DELETE_WINDOW',lambda:window_utils.close_btn_clicked(PREVIOUS_SCREEN=PREVIOUS_SCREEN,CURRENT_SCREEN=plt_screen))
        # plt_screen.grab_set()
        PREVIOUS_SCREEN.withdraw()
        window_utils.bring_screen_to_center(plt_screen)
        window_utils.set_heading(plt_screen)
        drop_down = window_utils.create_drop_down(
            plt_screen, ('HOME', 'SATELLITE', 'GPS'))
        drop_down.bind('<<ComboboxSelected>>', change_screen)
        data, temperature_c, temperature_f, humidity, heat_index_c, heat_index_f = window_utils.read_data()
        figure = plt.figure(figsize=(25, 9))
        fig1 = figure.add_subplot(331)
        fig1.plot(temperature_c)
        fig1.set_xlabel('Time', fontsize=int(
            plt_screen.winfo_screenheight()/80))
        fig1.set_ylabel('Temperature C', fontsize=int(
            plt_screen.winfo_screenheight()/80))
        xlim_start = len(temperature_c)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(temperature_c))
        ylim_start = 0
        ylim_end = temperature_c.max()
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+5)

        fig1 = figure.add_subplot(332)
        fig1.plot(humidity)
        fig1.set_xlabel('Time', fontsize=int(
            plt_screen.winfo_screenheight()/80))
        fig1.set_ylabel('Humidity %', fontsize=int(
            plt_screen.winfo_screenheight()/80))
        xlim_start = len(humidity)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(humidity))
        ylim_start = 0
        ylim_end = humidity.max()
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+5)

        fig1 = figure.add_subplot(333)
        fig1.plot(heat_index_c)
        fig1.set_xlabel('Time', fontsize=int(
            plt_screen.winfo_screenheight()/80))
        fig1.set_ylabel('Heat Index C', fontsize=int(
            plt_screen.winfo_screenheight()/80))
        xlim_start = len(heat_index_c)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(heat_index_c))
        ylim_start = 0
        ylim_end = heat_index_c.max()
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+5)

        fig1 = figure.add_subplot(334)
        fig1.plot(temperature_f)
        fig1.set_xlabel('Time', fontsize=int(
            plt_screen.winfo_screenheight()/80))
        fig1.set_ylabel('Temperature F', fontsize=int(
            plt_screen.winfo_screenheight()/80))
        xlim_start = len(temperature_f)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(temperature_f))
        ylim_start = 0
        ylim_end = temperature_f.max()
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+10)

        fig1 = figure.add_subplot(336)
        fig1.plot(heat_index_f)
        fig1.set_xlabel('Time', fontsize=int(
            plt_screen.winfo_screenheight()/80))
        fig1.set_ylabel('Heat Index F', fontsize=int(
            plt_screen.winfo_screenheight()/80))
        xlim_start = len(heat_index_f)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(heat_index_f))
        ylim_start = 0
        ylim_end = heat_index_f.max()
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+5)

        canvas1 = FigureCanvasTkAgg(figure, master=plt_screen)
        canvas1.draw()
        canvas1.get_tk_widget().pack()
        canvas1._tkcanvas.pack()
        toolbar = NavigationToolbar2Tk(canvas1, plt_screen)
        toolbar.config(bg='')
        toolbar.update()


def plot_screen():
    plot_sc = PLOT_SCREEN(root)
    pass


root = Tk()
root_width, root_height = window_utils.bring_screen_to_center(root)
options = ['Home', 'Payload', 'GPS', 'Plot']
window_utils.set_heading(root)
plot_btn = Button(root, text='PLOT', command=plot_screen)
plot_btn.pack()
root.mainloop()
