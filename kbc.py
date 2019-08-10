from kbc2 import *
from tkinter import *
from tkinter import ttk
from pygame import mixer
from ttkthemes import themed_tk as tk


class kbc:
        def start(self):
            self.progress1["value"] = 0
            self.maxbytes = 100
            self.progress1["maximum"] = 100
            self.read_bytes()

        def read_bytes(self):
            '''simulate reading 500 bytes; update progress bar'''
            self.bytes += 1
            abc = "Loading.... (" + str(self.bytes) + "%)"
            self.lb_blank.config(text=abc)
            self.progress1["value"] = self.bytes
            if self.bytes < self.maxbytes:
                # read more bytes after 100 ms
                self.root.after(250, self.read_bytes)
            else:
                mixer.music.stop()
                self.root.destroy()
                kbc2()
        def __init__(self):
            #self.root = Tk()
            self.root = tk.ThemedTk()
            self.root.get_themes()
            # self.root.set_theme('clam')
            self.root.set_theme('radiance')
            # self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
            # self.root.resizable(0, 0)
            self.root.attributes('-fullscreen', True)
            mixer.init()
            mixer.music.load('song/Kbc.mp3')
            mixer.music.play()
            self.root.config(background="#090035")
            dp = PhotoImage(file="img/kbc_frontlook.png")
            Label(self.root, image=dp, bg='#090035').pack()
            self.lb_blank = Label(self.root, text="", bg="white")
            self.progress1 = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
            self.lb_blank.pack()
            self.progress1.pack()
            self.bytes = 0
            self.start()
            self.root.mainloop()
if __name__ == '__main__':
    kbc()
