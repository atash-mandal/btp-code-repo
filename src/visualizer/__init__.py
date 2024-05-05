import tkinter as tk
from functools import partial
import colorsys
import threading
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import keyboard
from .utility import get_collection
from .positions import *
from .plots import *
from .script import create_py_script



class Visualizer:
    def __init__(self, master,structures):
        self.master = master
        self.master.geometry(f"{WIDTH}x{HEIGHT}+{win_x}+{win_y}")
         
        # frames
        self.frame_1 = tk.Frame(self.master, width=frame1_w, height=frame1_h)
        self.frame_1.place(x=frame1_x,y=frame1_y)

        self.frame_2 = tk.Frame(self.master, width=frame2_w, height=frame2_h)
        self.frame_2.place(x=frame2_x,y=frame2_y)

        self.frame_3 = tk.Frame(self.master, width=frame3_w, height=frame3_h)
        self.frame_3.place(x=frame3_x,y=frame3_y)

        self.frame_4 = tk.Frame(self.master, width=frame4_w, height=frame4_h)
        self.frame_4.place(x=frame4_x,y=frame4_y)

        self.frame_details = tk.Frame(self.frame_2, width=frame_details_w, height=frame_details_h)
        self.frame_details.place(x=frame_details_x,y=frame_details_y)

        self.thickness_frame = tk.Frame(self.frame_1, width=thickness_w, height=thickness_h)
        self.thickness_frame.place(x=thickness_x,y=thickness_y)

        self.button_frame = tk.Frame(self.frame_1, width=button_w, height=button_h)
        self.button_frame.place(x=button_x,y=button_y)

        label = tk.Label(self.frame_details, text="Hover over the structures\n to view details",font=("Helvetica", 14, "bold"))
        label.grid(row=0,column=0,pady=95)
        label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
        
        # metal_thickness
        self.metal_thickness = tk.DoubleVar()
        self.metal_thickness.set(17.5)
        self.thickness_label = tk.Label(self.thickness_frame, text="Select a metal (strip) thickness",font=("Helvetica", 12, "bold"))
        self.thickness_label.grid(row=0,column=0,columnspan=3,pady=3)

        radio_button1 = tk.Radiobutton(self.thickness_frame, text="17.5", variable=self.metal_thickness, value=17.5, font=("Helvetica", 12, "bold"))
        radio_button1.grid(row=1,column=0)

        radio_button2 = tk.Radiobutton(self.thickness_frame, text="35.5", variable=self.metal_thickness, value=35.5, font=("Helvetica", 12, "bold"))
        radio_button2.grid(row=1,column=1)


        # buttons
        self.button_abcd = tk.Button(self.button_frame, text="ABCD Params", width=button1_w, height=button1_h,command=self.handle_abcd,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 10, "bold"))
        self.button_abcd.grid(row=0,column=0,padx=5)
        bind_hover_effect(self.button_abcd)

        self.button_s = tk.Button(self.button_frame, text="S Params", width=button1_w, height=button1_h,command=self.handle_s,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 10, "bold"))
        self.button_s.grid(row=1,column=0,padx=5,pady=5)
        bind_hover_effect(self.button_s)

        self.button_a = tk.Button(self.button_frame, text="A", width=button2_w, height=button2_h,command=self.handle_a,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 10, "bold"))
        self.button_a.grid(row=0,column=1)
        bind_hover_effect(self.button_a)

        self.button_b = tk.Button(self.button_frame, text="B", width=button2_w, height=button2_h,command=self.handle_b,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 10, "bold"))
        self.button_b.grid(row=0,column=2,padx=5)
        bind_hover_effect(self.button_b)

        self.button_c = tk.Button(self.button_frame, text="C", width=button2_w, height=button2_h,command=self.handle_c,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 10, "bold"))
        self.button_c.grid(row=0,column=3)
        bind_hover_effect(self.button_c)

        self.button_d = tk.Button(self.button_frame, text="D", width=button2_w, height=button2_h,command=self.handle_d,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 10, "bold"))
        self.button_d.grid(row=0,column=4,padx=5)
        bind_hover_effect(self.button_d)

        self.button_s11 = tk.Button(self.button_frame, text="S11", width=button2_w, height=button2_h,command=self.handle_s11,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 10, "bold"))
        self.button_s11.grid(row=1,column=1,pady=5)
        bind_hover_effect(self.button_s11)

        self.button_s12 = tk.Button(self.button_frame, text="S12", width=button2_w, height=button2_h,command=self.handle_s12,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 10, "bold"))
        self.button_s12.grid(row=1,column=2,padx=5,pady=5)
        bind_hover_effect(self.button_s12)

        self.button_s21 = tk.Button(self.button_frame, text="S21", width=button2_w, height=button2_h,command=self.handle_s21,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 10, "bold"))
        self.button_s21.grid(row=1,column=3,pady=5)
        bind_hover_effect(self.button_s21)

        self.button_s22 = tk.Button(self.button_frame, text="S22", width=button2_w, height=button2_h,command=self.handle_s22,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 10, "bold"))
        self.button_s22.grid(row=1,column=4,padx=5,pady=5)
        bind_hover_effect(self.button_s22)

        self.button_generate = tk.Button(self.frame_1, text="Generate Script", width=generate_w, height=generate_h,command=self.handle_generate,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 12, "bold"))
        self.button_generate.place(x=generate_x,y=generate_y)
        bind_hover_effect(self.button_generate)

        self.button_select = tk.Button(self.frame_1, text="Select All", width=select_w, height=select_h,command=self.handle_select,relief="ridge",bg="lightgrey",cursor="hand2",font=("Helvetica", 12, "bold"))
        self.button_select.place(x=select_x,y=select_y)
        bind_hover_effect(self.button_select)


        var = tk.StringVar()
        var.set("Magnitude")
        # Create radio buttons
        lbl = tk.Label(self.frame_1,text="S parameter",font=("Helvetica", 12, "bold"))
        lbl.place(x=700, y=380)

        radio_button_s_db = tk.Radiobutton(self.frame_1, text="dB", variable=var, value="dB", command=self.handle_s_dB, font=("Helvetica", 11))
        radio_button_s_db.place(x=700,y=400)

        radio_button_s = tk.Radiobutton(self.frame_1, text="Mag", variable=var, value="Magnitude", command=self.handle_s, font=("Helvetica", 11))
        radio_button_s.place(x=750,y=400)


        plt.rcParams['font.size'] = 10

        self.fig = plt.figure(figsize=(5, 5))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        self.fig_abcd = plt.figure(figsize=(6,4))

        self.fig_s = plt.figure(figsize=(6,4))

        # ax = fig.gca(projection='3d')
        # ax.set_aspect('equal')

        [x_lim, y_lim, z_lim, pc] = get_collection(structures=structures,thickness=17.5)
        self.ax.add_collection3d(pc)

        self.ax.set_xlim([-x_lim,x_lim])
        self.ax.set_ylim([0,y_lim])
        self.ax.set_zlim([0,z_lim])
        self.ax.grid(False)
        self.ax.axis('off')


        self.canvas_3d = FigureCanvasTkAgg(self.fig, master=self.frame_2)
        self.canvas_3d.draw()
        self.canvas_3d.get_tk_widget().place(x=-10, y=-80)

        self.canvas_abcd = FigureCanvasTkAgg(self.fig_abcd, master=self.frame_3)
        self.canvas_abcd.draw()
        self.canvas_abcd.get_tk_widget().place(x=0, y=0)

        self.canvas_s = FigureCanvasTkAgg(self.fig_s, master=self.frame_4)
        self.canvas_s.draw()
        self.canvas_s.get_tk_widget().place(x=0, y=0)


        self.plot_set = set()
        for i in range(len(structures)):
            self.plot_set.add(i)

        self.structures = structures
        self.map_rectangles = {}
        self.rectangles = []
        self.is_selected = False
        self.plot_abcd = []
        self.plot_s = []
        self.handle_abcd()
        for i in range(len(structures)):
            self.plot_set.add(i)
        self.handle_s()
        self.plot_set.clear()
        self.create_rectangles()


    def create_rectangles(self):
        n = len(self.structures)
        if n==0:
            return
        rect_width = (rect_w)//n
        rect_height = rect_h
        x = rect_x
        for structure in self.structures:
            rect_outer_frame = tk.Frame(self.frame_1, width=rect_width, height=rect_height)
            rect_outer_frame.place(x=x,y=rect_y)
            if str(type(structure)) == "<class 'skmd.structure.Microstripline'>":
                rect_outer_frame.config(bg = orange)
            elif str(type(structure)) == "<class 'skmd.structure.MSL_gap'>":
                rect_outer_frame.config(bg = green)
            elif str(type(structure)) == "<class 'visualizer.network.Stub'>":
                rect_outer_frame.config(bg = red)
            elif str(type(structure)) == "<class 'skmd.network.Network'>":
                rect_outer_frame.config(bg = purple)

            rect_inner_frame = tk.Frame(rect_outer_frame, width=rect_width-10, height=rect_height-10,bg=white)
            rect_inner_frame.place(x=5,y=5)
            x = x + rect_width
            self.map_rectangles[rect_outer_frame] = structure
            self.rectangles.append(rect_outer_frame)
            bind_hover_details(rect_outer_frame, self.map_rectangles, self.rectangles, self.plot_set ,self.frame_details)
            rect_outer_frame.bind("<Button-1>", self.handle_click)
            rect_inner_frame.bind("<Button-1>", self.handle_click)

    
    def handle_click(self, event):
        idx = 0
        try:
            idx = self.rectangles.index(event.widget)
        except:
            parent_id = event.widget.winfo_parent()
            parent_widget = event.widget._nametowidget(parent_id)
            idx = self.rectangles.index(parent_widget)
        if idx in self.plot_set and keyboard.is_pressed('ctrl'):
            self.rectangles[idx].winfo_children()[0].config(bg=white)
            self.plot_set.remove(idx)
        elif idx not in self.plot_set and keyboard.is_pressed('ctrl'):
            bg_color = reduce_shade(self.rectangles[idx].cget("bg"))
            self.rectangles[idx].winfo_children()[0].config(bg=bg_color)
            self.plot_set.add(idx)
        print(self.plot_set)

    def remove_abcd_plots(self):
        self.fig_abcd.clear()
        self.canvas_abcd.draw()

    def remove_s_plots(self):
        self.fig_s.clear()
        self.canvas_s.draw()
    
    def handle_abcd(self):
        if len(self.plot_set) == 0:
            return
        self.remove_abcd_plots()
        pts_freq = 1000
        freq = np.linspace(0.1e9,10e9,pts_freq)
        net = get_network(sorted(self.plot_set), self.structures)
        ax1 = self.fig_abcd.add_subplot(221)
        ax2 = self.fig_abcd.add_subplot(222)
        ax3 = self.fig_abcd.add_subplot(223)
        ax4 = self.fig_abcd.add_subplot(224)
        try:
            ax1.plot(freq/1e9,np.abs(net.A),label='$A$') 
            ax2.plot(freq/1e9,np.abs(net.B),label='$B$') 
            ax3.plot(freq/1e9,np.abs(net.C),label='$C$') 
            ax4.plot(freq/1e9,np.abs(net.D),label='$D$')  
        except:
            ax1.plot(freq/1e9,np.abs(net.NW.A),label='$A$')  
            ax2.plot(freq/1e9,np.abs(net.NW.B),label='$B$')  
            ax3.plot(freq/1e9,np.abs(net.NW.C),label='$C$')  
            ax4.plot(freq/1e9,np.abs(net.NW.D),label='$D$') 
        # self.ax_abcd.legend()
        ax1.legend()
        ax2.legend()
        ax3.legend()
        ax4.legend()
        self.canvas_abcd.draw() 
        
        
    def handle_s(self):
        if len(self.plot_set) == 0:
            return
        self.remove_s_plots()
        pts_freq = 1000
        freq = np.linspace(0.1e9,10e9,pts_freq)
        net = get_network(sorted(self.plot_set), self.structures)
        ax1 = self.fig_s.add_subplot(221)
        ax2 = self.fig_s.add_subplot(222)
        ax3 = self.fig_s.add_subplot(223)
        ax4 = self.fig_s.add_subplot(224)
        try:
            ax1.plot(freq/1e9,np.abs(net.S11),label='$S11$') 
            ax2.plot(freq/1e9,np.abs(net.S12),label='$S12$')
            ax3.plot(freq/1e9,np.abs(net.S21),label='$S21$') 
            ax4.plot(freq/1e9,np.abs(net.S22),label='$S22$') 
        except:
            ax1.plot(freq/1e9,np.abs(net.NW.S11),label='$S11$') 
            ax2.plot(freq/1e9,np.abs(net.NW.S12),label='$S12$') 
            ax3.plot(freq/1e9,np.abs(net.NW.S21),label='$S21$') 
            ax4.plot(freq/1e9,np.abs(net.NW.S22),label='$S22$') 
        ax1.legend()
        ax2.legend()
        ax3.legend()
        ax4.legend()
        self.canvas_s.draw()

    def handle_s_dB(self):
        if len(self.plot_set) == 0:
            return
        self.remove_s_plots()
        pts_freq = 1000
        freq = np.linspace(0.1e9,10e9,pts_freq)
        net = get_network(sorted(self.plot_set), self.structures)
        ax1 = self.fig_s.add_subplot(221)
        ax2 = self.fig_s.add_subplot(222)
        ax3 = self.fig_s.add_subplot(223)
        ax4 = self.fig_s.add_subplot(224)
        try:
            ax1.plot(freq/1e9,20*np.log10(np.abs(net.S11)),label='$S11$') 
            ax2.plot(freq/1e9,20*np.log10(np.abs(net.S12)),label='$S12$')
            ax3.plot(freq/1e9,20*np.log10(np.abs(net.S21)),label='$S21$') 
            ax4.plot(freq/1e9,20*np.log10(np.abs(net.S22)),label='$S22$') 
        except:
            ax1.plot(freq/1e9,20*np.log10(np.abs(net.NW.S11)),label='$S11$') 
            ax2.plot(freq/1e9,20*np.log10(np.abs(net.NW.S12)),label='$S12$') 
            ax3.plot(freq/1e9,20*np.log10(np.abs(net.NW.S21)),label='$S21$') 
            ax4.plot(freq/1e9,20*np.log10(np.abs(net.NW.S22)),label='$S22$') 
        ax1.legend()
        ax2.legend()
        ax3.legend()
        ax4.legend()
        self.canvas_s.draw()

    def handle_a(self):
        if len(self.plot_set) == 0:
            return
        self.remove_abcd_plots()
        pts_freq = 1000
        freq = np.linspace(0.1e9,10e9,pts_freq)
        net = get_network(sorted(self.plot_set), self.structures)
        ax = self.fig_abcd.add_subplot(111)
        try:
            ax.plot(freq/1e9,np.abs(net.A),label='$A$') 
        except:
            ax.plot(freq/1e9,np.abs(net.NW.A),label='$A$') 
        ax.legend()
        self.canvas_abcd.draw() 


    def handle_b(self):
        if len(self.plot_set) == 0:
            return
        self.remove_abcd_plots()
        pts_freq = 1000
        freq = np.linspace(0.1e9,10e9,pts_freq)
        net = get_network(sorted(self.plot_set), self.structures)
        ax = self.fig_abcd.add_subplot(111)
        try:
            ax.plot(freq/1e9,np.abs(net.B),label='$B$') 
        except:
            ax.plot(freq/1e9,np.abs(net.NW.B),label='$B$') 
        ax.legend()
        self.canvas_abcd.draw() 

    def handle_c(self):
        if len(self.plot_set) == 0:
            return
        self.remove_abcd_plots()
        pts_freq = 1000
        freq = np.linspace(0.1e9,10e9,pts_freq)
        net = get_network(sorted(self.plot_set), self.structures)
        ax = self.fig_abcd.add_subplot(111)
        try:
            ax.plot(freq/1e9,np.abs(net.C),label='$C$') 
        except:
            ax.plot(freq/1e9,np.abs(net.NW.C),label='$C$') 
        ax.legend()
        self.canvas_abcd.draw() 

    def handle_d(self):
        if len(self.plot_set) == 0:
            return
        self.remove_abcd_plots()
        pts_freq = 1000
        freq = np.linspace(0.1e9,10e9,pts_freq)
        net = get_network(sorted(self.plot_set), self.structures)
        ax = self.fig_abcd.add_subplot(111)
        try:
            ax.plot(freq/1e9,np.abs(net.D),label='$D$') 
        except:
            ax.plot(freq/1e9,np.abs(net.NW.D),label='$D$') 
        ax.legend()
        self.canvas_abcd.draw() 

    def handle_s11(self):
        if len(self.plot_set) == 0:
            return
        self.remove_s_plots()
        pts_freq = 1000
        freq = np.linspace(0.1e9,10e9,pts_freq)
        net = get_network(sorted(self.plot_set), self.structures)
        ax = self.fig_s.add_subplot(111)
        try:
            ax.plot(freq/1e9,np.abs(net.S11),label='$S11$') 
        except:
            ax.plot(freq/1e9,np.abs(net.NW.S11),label='$S11$') 
        ax.legend()
        self.canvas_s.draw() 

    def handle_s12(self):
        if len(self.plot_set) == 0:
            return
        self.remove_s_plots()
        pts_freq = 1000
        freq = np.linspace(0.1e9,10e9,pts_freq)
        net = get_network(sorted(self.plot_set), self.structures)
        ax = self.fig_s.add_subplot(111)
        try:
            ax.plot(freq/1e9,np.abs(net.S12),label='$S12$') 
        except:
            ax.plot(freq/1e9,np.abs(net.NW.S12),label='$S12$') 
        ax.legend()
        self.canvas_s.draw() 

    def handle_s21(self):
        if len(self.plot_set) == 0:
            return
        self.remove_s_plots()
        pts_freq = 1000
        freq = np.linspace(0.1e9,10e9,pts_freq)
        net = get_network(sorted(self.plot_set), self.structures)
        ax = self.fig_s.add_subplot(111)
        try:
            ax.plot(freq/1e9,np.abs(net.S21),label='$S21$') 
        except:
            ax.plot(freq/1e9,np.abs(net.NW.S21),label='$S21$') 
        ax.legend()
        self.canvas_s.draw() 

    def handle_s22(self):
        if len(self.plot_set) == 0:
            return
        self.remove_s_plots()
        
        net = get_network(sorted(self.plot_set), self.structures)
        ax = self.fig_s.add_subplot(111)
        try:
            ax.plot(freq/1e9,np.abs(net.S22),label='$S22$') 
        except:
            ax.plot(freq/1e9,np.abs(net.NW.S22),label='$S22$') 
        ax.legend()
        self.canvas_s.draw() 

    def handle_generate(self):
        threading.Thread(target=self.generate_script).start()
    def generate_script(self):
        print("created")
        create_py_script(self.structures, "script")

    def handle_select(self):
        i = 0
        for rectangle in self.rectangles:
            bg_color = rectangle.cget("bg")
            if self.is_selected == False:
                rectangle.winfo_children()[0].config(bg=reduce_shade(bg_color))
                self.plot_set.add(i)
            else:
                self.deselect_rectangles()
                break
            i = i + 1
        self.is_selected = ~(self.is_selected)
        print(self.plot_set)
    
    def deselect_rectangles(self):
        for rectangle in self.rectangles:
            rectangle.winfo_children()[0].config(bg=white)
        self.plot_set.clear()

def bind_hover_details(widget, map_rectangles, rectangles, plot_set, display_frame):
    widget.bind("<Enter>", partial(show_details, map_rectangles = map_rectangles, rectangles = rectangles, plot_set=plot_set, display_frame = display_frame))
    widget.bind("<Leave>", partial(remove_details, rectangles=rectangles, plot_set=plot_set, display_frame = display_frame))

def remove_details(event, rectangles, plot_set, display_frame):
    destroy_widgets(display_frame)
    label = tk.Label(display_frame, text="Hover over the structures\n to view details",font=("Helvetica", 14, "bold"))
    label.grid(row=0,column=0,pady=95)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    idx = rectangles.index(event.widget)
    if idx not in plot_set:
        event.widget.winfo_children()[0].config(bg=white)

def show_details(event, map_rectangles, rectangles, plot_set, display_frame):
    destroy_widgets(display_frame)
    bg_color = reduce_shade(event.widget.cget("bg"))
    idx = rectangles.index(event.widget)
    if idx not in plot_set:
        event.widget.winfo_children()[0].config(bg=bg_color)

    if event.widget.cget("bg") == orange:
        line_details(map_rectangles[event.widget],display_frame)
    elif event.widget.cget("bg") == green:
        gap_details(map_rectangles[event.widget],display_frame)
    elif event.widget.cget("bg") == red:
        stub_details(map_rectangles[event.widget],display_frame)
    elif event.widget.cget("bg") == purple:
        network_details(map_rectangles[event.widget],display_frame)

def line_details(structure,display_frame):
    label = tk.Label(display_frame, text="MICROSTRIP LINE",font=("Helvetica", 12, "bold"),bg=orange)
    label.grid(row=0,column=0,pady=10)
    label = tk.Label(display_frame, text=f"Length: {structure.l}",font=("Helvetica", 12, "bold"))
    label.grid(row=1,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Width: {structure.w}",font=("Helvetica", 12, "bold"))
    label.grid(row=2,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Substrate Thickness: {structure.h}",font=("Helvetica", 12, "bold"))
    label.grid(row=3,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Epsilon_r: {structure.er}",font=("Helvetica", 12, "bold"))
    label.grid(row=4,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Effective er: {structure.er_eff}",font=("Helvetica", 12, "bold"))
    label.grid(row=5,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Characteristic Impedence: {structure.Z0}",font=("Helvetica", 12, "bold"))
    label.grid(row=6,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Frequency defined? {str(structure.omega is not None)}",font=("Helvetica", 12, "bold"))
    label.grid(row=7,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))

def stub_details(structure,display_frame):
    label = tk.Label(display_frame, text="STUB",font=("Helvetica", 12, "bold"), bg=red)
    label.grid(row=0,column=0,pady=10)
    label = tk.Label(display_frame, text=f"Transmission Line Length: {structure.l1 + structure.l2 + structure.w0}",font=("Helvetica", 12, "bold"))
    label.grid(row=1,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Transmission Line Width: {structure.w}",font=("Helvetica", 12, "bold"))
    label.grid(row=2,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Stub Length: {structure.l0}",font=("Helvetica", 12, "bold"))
    label.grid(row=3,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Stub Width: {structure.w0}",font=("Helvetica", 12, "bold"))
    label.grid(row=4,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Substrate Thickness: {structure.h}",font=("Helvetica", 12, "bold"))
    label.grid(row=5,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Epsilon_r: {structure.er}",font=("Helvetica", 12, "bold"))
    label.grid(row=6,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Frequency defined? {str(structure.omega is not None)}",font=("Helvetica", 12, "bold"))
    label.grid(row=7,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))

def gap_details(structure,display_frame):
    label = tk.Label(display_frame, text="GAP",font=("Helvetica", 12, "bold"), bg=green)
    label.grid(row=0,column=0,pady=10)
    label = tk.Label(display_frame, text=f"Length: {structure.d}",font=("Helvetica", 12, "bold"))
    label.grid(row=1,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Width: {structure.w}",font=("Helvetica", 12, "bold"))
    label.grid(row=2,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Substrate Thickness: {structure.h}",font=("Helvetica", 12, "bold"))
    label.grid(row=3,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Epsilon_r: {structure.er}",font=("Helvetica", 12, "bold"))
    label.grid(row=4,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Capacitance: {structure.Cg}",font=("Helvetica", 12, "bold"))
    label.grid(row=5,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))
    label = tk.Label(display_frame, text=f"Frequency defined? {str(structure.omega is not None)}",font=("Helvetica", 12, "bold"))
    label.grid(row=7,column=0,pady=2)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))

def network_details(structure,display_frame):
    label = tk.Label(display_frame, text="This is a Network",font=("Helvetica", 12, "bold"))
    label.grid(row=0,column=0,pady=100)
    label.config(padx=((frame_details_w-label.winfo_reqwidth())//2))

def destroy_widgets(frame):
    children = frame.winfo_children()
    for child in children:
        child.destroy()

def reduce_shade(current_bg):
    r, g, b = colorsys.rgb_to_hsv(*tuple(int(current_bg[i:i+2], 16) for i in (1, 3, 5)))
    r, g, b = colorsys.hsv_to_rgb(r, g, max(0, min(1, b - 0.1)))  # reduce brightness by 0.1
    new_bg = f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    return new_bg

def bind_hover_effect(widget):
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)
def on_enter(event):
    event.widget.config(bg='gray') 
def on_leave(event):
    event.widget.config(bg='lightgray')

def on_closing(root):
    plt.close('all')
    root.destroy() 

def visualizer(structures):
    if len(structures) == 0:
        return
    root = tk.Tk()
    app = Visualizer(root, structures)
    root.protocol("WM_DELETE_WINDOW", partial(on_closing, root))
    root.mainloop()

