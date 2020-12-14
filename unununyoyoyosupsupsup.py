from tkinter import*
import random
root = Tk()
root.title("Ununrerealal")
root.geometry("1000x3000")

ntry = Entry(root)
ntry.place(relx = 0.5, rely = 0.1,anchor = CENTER)
ntry1 = Entry(root)
ntry1.place(relx = 0.5, rely = 0.2,anchor = CENTER)
qentry = []
qentry1 = []
unlabel = Label(root)
unram = Label(root)
unlabel3 = Label(root)
unlabel32 = Label(root)

def undefi():
    fiend2 = ntry1.get()
    fiend = ntry.get()
    qentry.append(fiend)
    qentry1.append(fiend2)
    unlabel["text"] = "Country " + str(qentry)
    unram["text"] = "City " + str(qentry1)
    

def radm():
    lenth = len(qentry)
    lenth2 = len(qentry1)
    randomnum = random.randint(0,lenth - 1)
    randomnum1 = random.randint(0,lenth2 - 1)
    name = qentry[randomnum]
    name2 = qentry1[randomnum1]
    unlabel3["text"] = "Your unlucky uncountry is " + name
    unlabel32["text"] = "Your unlucky uncity is " + name2
    
button1 = Button(root,text="Un Lis ", command = undefi)
button2 = Button(root,text="unsup",command = radm)
button1.place(relx = 0.5, rely = 0.3,anchor = CENTER)
button2.place(relx = 0.5, rely = 0.4,anchor = CENTER)
unlabel.place(relx = 0.5, rely = 0.5,anchor = CENTER)
unram.place(relx = 0.5, rely = 0.6,anchor = CENTER)
unlabel3.place(relx = 0.5, rely = 0.7,anchor = CENTER)
unlabel32.place(relx = 0.5, rely = 0.8,anchor = CENTER)

root.mainloop()