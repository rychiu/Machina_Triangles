#Ryan Chiu

import random as rd
import tkinter as tk

class Triangle(object):
    def __init__(self, xVal, yVal):
        self.xVal = xVal
        self.yVal = yVal

    def computePoint(p1, p3):
    # computePoint(p1, p3) will generate the (x1,y1) values
    # for the point that will appear on our GUI
        x1 = 100*p1+10
        y1 = 110-100*p3


    
class Triangle_gui():
    def __init__(self):
        root=tk.Tk()
        root.title("Triangle")
        root.geometry("400x400")

        cvs=tk.Canvas(root,width=400,height=250)
        cvs.pack()
        cvs.create_line(10,110,10,10,width=2)
        cvs.create_line(10,110,110,110,width=2)
        cvs.create_line(10,10,110,110,width=2)

        e = tk.Entry(root)
        e.pack()

        e.focus_set()
        retVal = e.get().split(',')
        
        def callback():
            print (e.get().split(','))
            
        b = tk.Button(root, text="get", width=10, command=callback)
        b.pack()


##        def key(event):
##            valid_characters="qwertyuiopasdfghjklzxcvbnm"
##            if event.keysym:
##                letter=event.keysym
##                h.update(letter)
##                word.configure(text=h.display_word())
##
##                used.config(text = "Used letters:" + h.guessedletters() + " ")
##                for x in h.body_parts_used:
##                    if x=="head":
##                        cvs.create_oval(200,50,240,90,width=3)
##                    elif x=="trunk":
##                        cvs.create_line(220,90,220,140,width=6)
##                    elif x=="left arm":
##                        cvs.create_line(220,110,180,100,width=3)
##                    elif x=="right arm":
##                        cvs.create_line(220,110,260,100,width=3)
##                    elif x=="left leg":
##                        cvs.create_line(220,140,200,210,width=4)
##                    elif x=="right leg":
##                        cvs.create_line(220,140,240,210,width=4)
##
##                if len(h.bodyparts)==0:
##                    outcome.configure(text="You lost! Better luck next time.")
##                    word.configure(text="Your word was: "+h.word)
##                    self.game=False
##                    
##                elif "__ " not in h.display_word():
##                    outcome.configure(text="You won! Great job!")
##                    self.game=False
##
##            root.bind_all('<Key>',key)
##            root.mainloop()
Triangle_gui()
                    
        
