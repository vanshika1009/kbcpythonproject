import threading
from time import sleep
from tkinter import *
from tkinter.messagebox import *

import pyttsx3 as pyttsx3
from pygame import mixer
from pymysql import *
# from ttkthemes import themed_tk as tk
# from tkinter import ttk
id_data_list=[]
COUNTER=0
ANS_COUNT=0
amount_list = ["5,000", "10,000","20,000","40,000","80,000","1,60,000", "3,20,000", "6,40,000","12,50,000", "25,00,000", "50,00,000","1 Crore", "3 Crore", "5 Crore", "7 Crore"]
class kbc3(Toplevel):
    def flip(self):
        global COUNTER
        engine = pyttsx3.init()
        engine.stop()
        msgbox = askquestion('Flip', 'Are you sure you want to Flip the question?')
        if msgbox == 'yes':

            conn = connect("snlvedant.db.7623447.b14.hostedresource.net", "snlvedant", "VMMeducation@123", "snlvedant")
            query_new = "SELECT * FROM `kbc1` where q_id =" + str(id_data_list[COUNTER + 1])
            cr = conn.cursor()
            cr.execute(query_new)
            result = cr.fetchone()
            self.lb_question.config(text = result[1])
            self.bt_option_A.config(text = result[2])
            self.bt_option_B.config(text = result[3])
            self.bt_option_C.config(text = result[4])
            self.bt_option_D.config(text = result[5])
            self.flip(state = 'disable')
            COUNTER = COUNTER + 1


    def fiftyfifty(self):
        engine = pyttsx3.init()
        engine.stop()
        conn = connect("snlvedant.db.7623447.b14.hostedresource.net", "snlvedant", "VMMeducation@123", "snlvedant")
        query_new = "SELECT * FROM `kbc1` where q_id =" + str(id_data_list[COUNTER])
        cr = conn.cursor()
        cr.execute(query_new)
        result = cr.fetchone()
        if result[0][0] == 'A':
            self.bt_option_B.config(state = 'disable')
            self.bt_option_C.config(state = 'disable')
        elif result[0][0] == 'B':
            self.bt_option_A.config(state = 'disable')
            self.bt_option_C.config(state = 'disable')
        elif result[0][0] == 'C':
            self.bt_option_A.config(state='disable')
            self.bt_option_B.config(state='disable')
        elif result[0][0] == 'D':
            self.bt_option_A.config(state='disable')
            self.bt_option_B.config(state='disable')
        self.fifty.config(state = 'disable')

    def exit(self):
        engine = pyttsx3.init()
        engine.stop()
        msgbox = askquestion('Exit application', 'Are you sure you want to exit')
        if msgbox == 'yes':
            self.root.destroy()

    def confirm_ans(self, option_num):
        print(option_num)
        msgbox1 = askquestion('Confirm Answer', 'Are you sure about the answer?')
        if msgbox1 == 'yes':

            if option_num == 'A':
                self.bt_option_A.config(bg = "#e0d902")
                self.bt_option_A.config(state= 'disable')
                self.bt_option_B.config(state= 'disable')
                self.bt_option_C.config(state= 'disable')
                self.bt_option_D.config(state= 'disable')

            elif option_num == 'B':
                self.bt_option_B.config(bg="#e0d902")
                self.bt_option_A.config(state='disable')
                self.bt_option_B.config(state='disable')
                self.bt_option_C.config(state='disable')
                self.bt_option_D.config(state='disable')

            elif option_num == 'C':
                self.bt_option_C.config(bg="#e0d902")
                self.bt_option_A.config(state="disable")
                self.bt_option_B.config(state='disable')
                self.bt_option_C.config(state='disable')
                self.bt_option_D.config(state='disable')


            elif option_num == 'D':
                self.bt_option_D.config(bg="#e0d902")
                self.bt_option_A.config(state='disable')
                self.bt_option_B.config(state='disable')
                self.bt_option_C.config(state='disable')
                self.bt_option_D.config(state='disable')
        engine = pyttsx3.init()
        engine.stop()
        sleep(2)
        self.check_ans(option_num)


    def check_ans(self,ans):
        print(ans)
        global id_data_list
        global COUNTER
        global ANS_COUNT
        global amount_list
        conn = connect("snlvedant.db.7623447.b14.hostedresource.net", "snlvedant", "VMMeducation@123", "snlvedant")
        query2 = "SELECT ans FROM `kbc1` where q_id =" + str(id_data_list[COUNTER])
        cr1 = conn.cursor()
        cr1.execute(query2)
        result = cr1.fetchone()
        print(result[0])
        if ans == result[0]:
            mixer.init()
            clap = "song/sahi.mp3"
            mixer.music.set_volume(0.5)
            mixer.music.load(clap)
            mixer.music.play()
            self.bt_amount.config(text=amount_list[ANS_COUNT])
            self.bt_amount.config(bg="green")
            self.amount_bt_list[ANS_COUNT].config(bg="green", fg="white")
            correct_ans = showinfo('Answer','Right answer')
            self.bt_option_A.config(state='normal', bg="WHITE")
            self.bt_option_B.config(state='normal', bg="WHITE")
            self.bt_option_C.config(state='normal', bg="WHITE")
            self.bt_option_D.config(state='normal', bg="WHITE")

            if ANS_COUNT<14:
                COUNTER = COUNTER + 1
                try:
                    self.amount_bt_list[ANS_COUNT + 1].config(bg="#f9eb22", fg="white")
                    query_new = "SELECT * FROM `kbc1` where q_id =" + str(id_data_list[COUNTER])
                    cr1 = conn.cursor()
                    cr1.execute(query_new)
                    result = cr1.fetchone()
                    self.lb_question.config(text=result[1])
                    self.bt_option_A.config(text=result[2])
                    self.bt_option_B.config(text=result[3])
                    self.bt_option_C.config(text=result[4])
                    self.bt_option_D.config(text=result[5])
                    sleep(1)

                    def demo():
                        engine = pyttsx3.init()
                        engine.setProperty('rate',140)
                        engine.say(result[1])
                        sleep(1)
                        engine.say('option a')
                        engine.say(result[2])
                        engine.say('option b')
                        engine.say(result[3])
                        engine.say('option c')
                        engine.say(result[4])
                        engine.say('option d')
                        engine.say(result[5])
                        engine.runAndWait()
                        engine.stop()

                    def demo2():
                        t = threading.Thread(target=demo)
                        t.start()

                    self.root.after(1000,demo2)
                    ANS_COUNT = ANS_COUNT + 1

                except:
                    print("network prob")
            else:                             #if the ques exceeds 14 that means the user has given all the correct answers
                engine = pyttsx3.init()
                engine.stop()
                self.bt_option_A.config(state = 'disable')
                self.bt_option_B.config(state = 'disable')
                self.bt_option_C.config(state = 'disable')
                self.bt_option_D.config(state = 'disable')
                engine = pyttsx3.init()
                engine.setProperty('rate',140)
                engine.say("winner")
                showinfo("", "winner")
            # correct_ans  = showinfo('Answer','Wrong Answer')
        else:                                #if ans doesnt match
            sleep(2)
            engine = pyttsx3.init()
            engine.stop()
            showinfo("", 'you lose')

    def __init__(self,parent):
        # self.root=Tk()
        self.root = Toplevel(parent)
        self.root.transient(parent)
        self.root.parent = parent
        self.root.title("KBC")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.iconbitmap("img/icon.ico")
        self.root.config(background="#192E8B")
        self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.configure(background="#090035")
        #----------------Frame--------------------
        head_frame=Frame(self.root,bg="#090035")
        middle_frame=Frame(self.root,bg="#090035")
        #-----------------middle-------------------
        left_frame=Frame(middle_frame,bg="#090035")
        left_frame.grid(row=0,column=0)
        #-----------------------------------left_frame---------------------------
        logo_frame=Frame(left_frame,bg="#090035")
        option_frame=Frame(left_frame,bg="#090035")
        logo_frame.pack(pady=20)
        option_frame.pack(pady=20)
        #----------------------------------------------------------------------
        amount_frame=Frame(middle_frame,bg="#090035")
        amount_frame.grid(row=0,column=1)
        #-----------------------------------------
        body_frame=Frame(self.root,bg="#090035")
        head_frame.pack()
        middle_frame.pack()
        body_frame.pack()
        #----------------life_line------------------------

        self.fifty=Button(head_frame,width=20,text="50-50", font=('bold',12),borderwidth=5,bg="#3277e6",fg="white", command = self.fiftyfifty)
        self.fifty.grid(row=0,column=0,padx=50,pady=10)

        self.flip=Button(head_frame,width=20,text="Flip", font=('bold',12),borderwidth=5,bg="#3277e6",fg="white", command = self.flip)
        self.flip.grid(row=0,column=1,padx=50,pady=10)
        #-----------------logo---------------------
        img = PhotoImage(file="img/que.png")
        Label(logo_frame, image=img, bg='#090035').pack(pady=10)
        self.lb_question=Label(logo_frame,text="",bg="#090035",fg="white",font=("bold",12))
        self.lb_question.pack(pady=10)
        #-----------------option_frame--------------------------
        self.bt_option_A=Button(option_frame,width=40, command = lambda :self.confirm_ans('A'))
        self.bt_option_B=Button(option_frame,width=40, command = lambda :self.confirm_ans('B'))
        self.bt_option_C=Button(option_frame,width=40, command = lambda :self.confirm_ans('C'))
        self.bt_option_D=Button(option_frame,width=40, command = lambda :self.confirm_ans('D'))

        self.bt_option_A.grid(row=0,column=0,padx=10,pady=10)
        self.bt_option_B.grid(row=0,column=1,padx=10,pady=10)
        self.bt_option_C.grid(row=1,column=0,padx=10,pady=10)
        self.bt_option_D.grid(row=1,column=1,padx=10,pady=10)

        #------------------------amount_frame---------------------------------------------
        self.bt_15=Button(amount_frame,text="15   7 Crore",width="20")
        self.bt_15.pack()
        self.bt_14 = Button(amount_frame, text="14   5 Crore", width="20")
        self.bt_14.pack()
        self.bt_13 = Button(amount_frame, text="13   3 Crore", width="20")
        self.bt_13.pack()
        self.bt_12 = Button(amount_frame, text="12   1 Crore", width="20")
        self.bt_12.pack()
        self.bt_11 = Button(amount_frame, text="11   50,00,000", width="20")
        self.bt_11.pack()
        self.bt_10=Button(amount_frame,text="10  25,00,000",width="20")
        self.bt_10.pack()
        self.bt_9 = Button(amount_frame, text="9 12,50,000", width="20")
        self.bt_9.pack()
        self.bt_8 = Button(amount_frame, text="8 6,40,000", width="20")
        self.bt_8.pack()
        self.bt_7 = Button(amount_frame, text="7 3,20,000", width="20")
        self.bt_7.pack()
        self.bt_6 = Button(amount_frame, text="6  1,60,000", width="20")
        self.bt_6.pack()
        self.bt_5 = Button(amount_frame, text="5  80,000", width="20")
        self.bt_5.pack()
        self.bt_4 = Button(amount_frame, text="4  40,000", width="20")
        self.bt_4.pack()
        self.bt_3 = Button(amount_frame, text="3  20,000", width="20")
        self.bt_3.pack()
        self.bt_2 = Button(amount_frame, text="2  10,000", width="20")
        self.bt_2.pack()
        self.bt_1 = Button(amount_frame, text="1  5,000", width="20")
        self.bt_1.pack()
        self.amount_bt_list=[self.bt_1,self.bt_2,self.bt_3,self.bt_4,self.bt_5,self.bt_6,self.bt_7,self.bt_8,self.bt_9,self.bt_10,self.bt_11,self.bt_12,self.bt_13,self.bt_14,self.bt_15]
        #---------------------body frame------------------------------
        self.bt_quit=Button(body_frame,text="Quit",font=("bold",12),width=20,command=self.exit)
        self.bt_amount=Button(body_frame,font=("bold",12),width=20)
        self.bt_quit.grid(row=0,column=0,padx=30,pady=10,)
        self.bt_amount.grid(row=0,column=1,padx=30,pady=10)
        #---------------------------Database-------------------------------------------
        conn = connect("snlvedant.db.7623447.b14.hostedresource.net", "snlvedant", "VMMeducation@123", "snlvedant")
        query = "SELECT q_id FROM `kbc1` ORDER BY rand() LIMIT 0,16"
        cr=conn.cursor()
        cr.execute(query)
        result=cr.fetchall()
        print(result)
        # --------------global-----------------------------------------------------------
        global id_data_list
        id_data_list.clear()

        global COUNTER
        global ANS_COUNT
        COUNTER=0
        ANS_COUNT=0
        #--------------------------
        for i in range(0,len(result)):
            id_data_list.append(result[i][0])

        # print(id_data_list)
        query2 = "SELECT * FROM `kbc1` where q_id ="+str(id_data_list[COUNTER])
        # print(query)
        cr1=conn.cursor()
        cr1.execute(query2)
        result1=cr1.fetchone()

        def demo():
            engine = pyttsx3.init()
            engine.setProperty('rate', 140)  # setting up new voice rate
            engine.say(result1[1])
            sleep(1)
            engine.say("option A")
            engine.say(result1[2])
            engine.say("option B")
            engine.say(result1[3])
            engine.say("option C")
            engine.say(result1[4])
            engine.say("option D")
            engine.say(result1[5])
            engine.runAndWait()
            engine.stop()

        def demo2():
            t1 = threading.Thread(target=demo)
            t1.start()

        # print(result)
        # print(id_data_list)
        self.root.after(500,demo2)
        self.lb_question.config(text=result1[1])
        self.bt_option_A.config(text=result1[2])
        self.bt_option_B.config(text=result1[3])
        self.bt_option_C.config(text=result1[4])
        self.bt_option_D.config(text=result1[5])

        self.root.mainloop()


# if __name__ == '__main__':
#     kbc3()
