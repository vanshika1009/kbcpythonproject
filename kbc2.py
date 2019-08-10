from finalform import *
from tkinter import *
from tkinter.messagebox import *
from ttkthemes import themed_tk as tk
from tkinter import ttk
class kbc2:
    def play_game(self):
        # self.root.destroy()
        self.fw_kbc = kbc3(self.root)
    def exit(self):
        msgbox = askquestion('Exit application', 'Are you sure you want to exit')
        if msgbox=='yes':
            self.root.destroy()

    def __init__(self):
        # root = Tk()
        self.root=tk.ThemedTk()
        self.root.get_themes()
        # self.root.set_theme('clam')
        self.root.set_theme('radiance')
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        # self.root.attributes('-fullscreen', True)
        self.root.config(background="#090035")
        self.pannel1 = PanedWindow(self.root, bg='#090035')
        self.pannel2 = PanedWindow(self.root, bg='#090035')
        self.pannel1.pack()
        self.pannel2.pack()
        dp_logo = PhotoImage(file="img/que.png")
        Label(self.pannel1, image=dp_logo, bg='#090035').grid(row= 0, column=0)

        dp_rules = PhotoImage(file="img/rules.png")
        Label(self.pannel1, image=dp_rules, bg='#090035').grid(row=0, column= 1, padx =50)

        pic_play = PhotoImage(file="img/play1.png")
        pic_quit = PhotoImage(file="img/quit1.png")
        bt_logo = ttk.Button(self.pannel2, image=pic_play, width=60,command=self.play_game)
        bt_rules = ttk.Button(self.pannel2, image=pic_quit, command=self.exit,  width=60)


        bt_logo.pack(pady=10)
        bt_rules.pack(pady=10)


        self.root.mainloop()
#-----------------------------------------------------------
# obj = kbc2()
if __name__ == '__main__':
    kbc2()
