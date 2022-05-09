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
    def __init__(self, SCREEN):        
        data, temperature_c, temperature_f, humidity, heat_index_c, heat_index_f = window_utils.read_data()
        
        START_STOP_BTN_FRAME=window_utils.create_frame(SCREEN)
        start_plotting_btn_img=PhotoImage(file='./button_images/plot_button.png')
        start_plotting_btn=Button(START_STOP_BTN_FRAME,image=start_plotting_btn_img,borderwidth=0)
        start_plotting_btn.pack(side=LEFT,anchor=CENTER,padx=10)
        stop_plotting_btn=Button(START_STOP_BTN_FRAME,text='STOP PLOTTING')
        stop_plotting_btn.pack(side=LEFT,anchor=CENTER,padx=10)

        figure = plt.figure(figsize=(20,8))
        fig1 = figure.add_subplot(331)
        fig1.plot(temperature_c)
        fig1.set_xlabel('Time', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Temperature C', fontsize=int(
            SCREEN.winfo_screenheight()/80))
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
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Humidity %', fontsize=int(
            SCREEN.winfo_screenheight()/80))
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
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Heat Index C', fontsize=int(
            SCREEN.winfo_screenheight()/80))
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
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Temperature F', fontsize=int(
            SCREEN.winfo_screenheight()/80))
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
            SCREEN.winfo_screenheight()/80))
        fig1.set_ylabel('Heat Index F', fontsize=int(
            SCREEN.winfo_screenheight()/80))
        xlim_start = len(heat_index_f)-100
        if xlim_start < 0:
            xlim_start = 0
        xlim_end = int(len(heat_index_f))
        ylim_start = 0
        ylim_end = heat_index_f.max()
        fig1.set_xlim(xlim_start, xlim_end)
        fig1.set_ylim(ylim_start, ylim_end+5)
        figure.tight_layout()

        canvas1 = FigureCanvasTkAgg(figure, master=SCREEN)
        canvas1.draw()
        canvas1.get_tk_widget().pack(anchor=CENTER,side=TOP)
        canvas1._tkcanvas.pack()
        toolbar = NavigationToolbar2Tk(canvas1, SCREEN)
        toolbar.config(bg='')
        toolbar.update()
        


# def plot_screen():
#     plot_sc = PLOT_SCREEN(root)
#     pass

