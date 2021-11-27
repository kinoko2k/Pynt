import tkinter
from tkinter import StringVar
from tkinter import Tk
from tkinter import filedialog
from tkinter import ttk

class Scribble:

    def on_pressed(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y,
                                outline = self.color.get(),
                                width = self.width.get())


    def on_dragged(self, event):
        self.canvas.create_line(self.sx, self.sy, event.x, event.y,
                            fill = self.color.get(),
                            width = self.width.get())
        self.sx = event.x
        self.sy = event.y

    def click1(self,event):
        self.canvas.create_oval(self.sx-20,self.sy-20,self.sx+20,self.sy+20,
                            fill = self.color.get(),
                            width = self.width.get())

    def click2(self,event):
        self.canvas.create_oval(self.sx-40,self.sy-30,self.sx+40,self.sy+30,
                           fill = self.color.get(),
                           width = self.width.get())



    def create_window(self):
        window = tkinter.Tk()
        window.title("Kinoko's Paint!!")
        self.canvas = tkinter.Canvas(window, bg = "white", 
                                 width = 800, height = 600)                             
        self.canvas.pack()
        quit_button = tkinter.Button(window, text = "終了",
                                 command = window.quit)
        quit_button.pack(side = tkinter.RIGHT)

        self.button = tkinter.Button(window, text = "save",
                                 command = self.show_save_dialog)
        self.button.pack(side = tkinter.RIGHT)
        
        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        self.canvas.bind("<B1-Motion>", self.on_dragged)
        self.canvas.bind("<ButtonPress-2>",self.click1)
        #self.canvas.bind("<ButtonPress-3>",self.click2)



        COLORS = ["red", "white", "blue", "skyblue", "pink", "green", "black", "purple", "gold", "orange", "yellow", "yellowgreen", "grey"]
        self.color = tkinter.StringVar()                    
        self.color.set(COLORS[2])                             
        b = tkinter.OptionMenu(window, self.color, *COLORS) 
        b.pack(side = tkinter.LEFT)
        
        self.width = tkinter.Scale(window, from_ = 1, to = 100,
                               orient = tkinter.HORIZONTAL) 
        self.width.set(5)                                       
        self.width.pack(side = tkinter.BOTTOM)

        return window;

    def show_save_dialog(self):
        ftypes = [("PNG Image Files", ".png"),
                  ("SVG Image Files", ".svg .xml"),
                  ("All Files", ".*")]
        ini_fname = "paint"
        fname = filedialog.asksaveasfilename(filetypes=ftypes,
                                             initialfile=ini_fname)
        if fname:
            self.entry1_var.set(fname)
        else:
            print("保存ボタンを押したよ！")
    
    def clear_canvas(self):
        self.test_canvas.delete(tkinter.ALL)

    def __init__(self):
        self.window = self.create_window();  

    def run(self):
        self.window.mainloop()
Scribble().run()
