# conda install pillow

import tkinter as tk
from tkinter import *
import numpy as np
import PIL
from PIL import Image, ImageTk

# array = np.ones((40,40))*150
# img =  ImageTk.PhotoImage(image=Image.fromarray(array))

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def say_hi(self):
        print("hi there, everyone!")

    def create_widgets(self):
        root.configure(background='white')
        root.geometry("800x600")

        
        # hello
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Welcome to the Romi 2.0 Controller UI"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        # camera image input
        array = np.random.rand(500,500)
        img =  ImageTk.PhotoImage(image=Image.fromarray(array))
        self.canvas = tk.Canvas(root,width=600,height=400)
        self.canvas.pack()
        self.canvas.create_image(20,20, anchor="nw", image=img)
        # self.canvas.configure(background='green')

        # keypads
        # insert image from file & resize
        self.keypadCan = tk.Canvas(root, width=265, height=165) # ,width=200
        self.keypadCan.pack()

        self.keypad_img = Image.open("images/kita/keypad symbols.png")
        self.keypad_img = self.keypad_img.resize((260, 160), Image.ANTIALIAS)
        # self.keypad_img = ImageTk.PhotoImage(Image.open("images/kita/keypad symbols.png"))  
        
        self.keypad_img = ImageTk.PhotoImage(self.keypad_img)
        self.keypadCan.create_image(130, 0, anchor=N, image=self.keypad_img) # (20,20, anchor=NW, image=img, , disabledimage=)
        self.keypadCan.configure(background='white')

        # quit menu
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
app = Application(master=root)
app.mainloop()