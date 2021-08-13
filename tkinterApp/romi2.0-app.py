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
        print("Hello Terminal")

    def create_widgets(self): 
        root.configure(background='white')
        self.configure(background='white')
        root.geometry("1000x900")
        root.title('Romi-2.0 Controller Camera')

        # CREATE SUB FUNCS FOR EACH WIDGET AND THEN RUN ALL FROM HERE
        
        # Cam label
        self.camLabel = tk.Label(self, width = 100, height=1, 
                                bg='white', bd = '0', 
                                text='Romi-2.0 Camera')
        self.camLabel.pack(side=TOP)

        # camera image input as np array
        self.canvas = tk.Canvas(self,width=600,height=400, bg='white')
        array = np.random.randint(0, 255, (400, 600))*1.
        self.img =  ImageTk.PhotoImage(image=Image.fromarray(array))
        self.canvas.create_image(300,0, anchor="n", image=self.img)
        self.canvas.pack(side=TOP)

        # keypads
        # insert image from file & resize
        self.keypadCan = tk.Canvas(self, width=260, height=160, bg='white', bd=0)
        self.keypad_img = Image.open("images/kita/keypad symbols.png")
        self.keypad_img = self.keypad_img.resize((260, 160), Image.ANTIALIAS)
        self.keypad_img = ImageTk.PhotoImage(self.keypad_img)
        self.keypadCan.create_image(130, 0, anchor=N, image=self.keypad_img)
        self.keypadCan.pack(side=TOP)

        # print to terminal button
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Send Hello to Terminal"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side=TOP)
       
        # quit menu
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side=TOP)


root = tk.Tk()
app = Application(master=root)
app.mainloop()