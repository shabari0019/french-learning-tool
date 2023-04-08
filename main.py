from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
card = {}
learn = {}
try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    learn = data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")
def known():
    learn.remove(card)
    ldata = pandas.DataFrame(learn)
    ldata.to_csv("data/to_learn.csv")
    next()

def flip():
    w2.itemconfig(ctitle,text="English",fill="white")
    w2.itemconfig(cword,text=card["English"],fill = "white")
    w2.itemconfig(background,image=bimage)

w1 = Tk()
w1.title("Flash")
w1.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
timer = w1.after(3000,func=flip)

def next():
    data= pandas.read_csv("data/to_learn.csv")
    learn = data.to_dict(orient="records")
    global card,timer
    w1.after_cancel(timer)
    card = random.choice(learn)
    w2.itemconfig(ctitle,text="French",fill = "black")
    w2.itemconfig(cword, text=card["French"],fill = "black")
    w2.itemconfig(background,image = fimag)
    timer = w1.after(3000, func=flip)

w2 = Canvas(width=800,height=526)
fimag = PhotoImage(file="images/card_front.png")
background = w2.create_image(400,263,image=fimag)
bimage = PhotoImage(file="images/card_back.png")
ctitle =w2.create_text(400,150,text="Title",font=("ariel",40,"italic"))
cword =w2.create_text(400,263,text="word",font=("bold",40,"italic"))
w2.config(bg=BACKGROUND_COLOR,highlightthickness=0)
w2.grid(row=0,column=0,columnspan=2)

cross = PhotoImage(file="images/wrong.png")
unbutton = Button(image=cross,command=next)
unbutton.grid(row=1,column=0)

right = PhotoImage(file="images/right.png")
rbutton = Button(image=right,command=known)
rbutton.grid(row=1,column=1)
next()
w1.mainloop()