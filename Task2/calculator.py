from tkinter import *
from tkinter.messagebox import *
import math as m

font = ('verdana', '20', 'bold')

# functions


def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)


def all_clear():
    textField.delete(0, END)


def btn_click(event):
    b = event.widget
    text = b['text']
    # print(text)

    if text == 'x!':
        ex = textField.get()
        text = str(m.factorial(int(ex)))
        textField.delete(0, END)

    if text == '√':
        ex = textField.get()
        text = m.sqrt(int(ex))
        textField.delete(0, END)

    if text == 'x':
        textField.insert(END, "*")
        return

    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return

    textField.insert(END, text)


# create a window
window = Tk()
window.title('Calculator')
window.geometry('500x500')
window.resizable(0, 0)

# heading label
heading = Label(window, text="Calculator", font=font)
heading.pack(side=TOP, pady=15)


# textfield
textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=15, fill=X, padx=15)


# buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP, padx=10)

allClearBtn = Button(buttonFrame, text='AC',
                     font=font, width=5, relief='ridge',  fg="#fff", bg="#3697f5", activebackground="orange", activeforeground="white", command=all_clear)
allClearBtn.grid(row=0, column=0, padx=3, pady=3)

clearBtn = Button(buttonFrame, text='<-',
                  font=font, width=5, relief='ridge', fg="#fff", bg="#2a2d36", activebackground="#3697f5", activeforeground="white", command=clear)
clearBtn.grid(row=0, column=1, padx=3, pady=3)


rootBtn = Button(buttonFrame, text='√',
                 font=font, width=5, relief='ridge', fg="#fff", bg="#2a2d36", activebackground="#3697f5", activeforeground="white")
rootBtn.grid(row=0, column=2, padx=3, pady=3)


# Adding button
tmp = 1
for i in range(1, 5):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(tmp),
                     font=font, width=5, relief='ridge', fg="#fff", bg="#2a2d36", activebackground="#3697f5", activeforeground="white")
        btn.grid(row=i, column=j)
        tmp += 1
        btn.bind('<Button-1>', btn_click)

zeroBtn = Button(buttonFrame, text='0',
                 font=font, width=5,  relief='ridge', fg="#fff", bg="#2a2d36", activebackground="#3697f5", activeforeground="white")
zeroBtn.grid(row=4, column=1, padx=3, pady=3)

dotBtn = Button(buttonFrame, text='.',
                font=font, width=5, relief='ridge', fg="#fff", bg="#2a2d36", activebackground="#3697f5", activeforeground="white")
dotBtn.grid(row=4, column=0, padx=3, pady=3)

eqlBtn = Button(buttonFrame, text='=',
                font=font, width=5, relief='ridge', fg="#fff", bg="#fe9037", activebackground="#3697f5", activeforeground="white")
eqlBtn.grid(row=4, column=3, padx=3, pady=3)

exBtn = Button(buttonFrame, text='x!',
               font=font, width=5, relief='ridge', fg="#fff", bg="#2a2d36", activebackground="#3697f5", activeforeground="white")
exBtn.grid(row=4, column=2, padx=3, pady=3)


plusBtn = Button(buttonFrame, text='+',
                 font=font, width=5, relief='ridge', fg="#fff", bg="#fe9037", activebackground="#3697f5", activeforeground="white")
plusBtn.grid(row=3, column=3, padx=3, pady=3)

minusBtn = Button(buttonFrame, text='-',
                  font=font, width=5, relief='ridge', fg="#fff", bg="#fe9037", activebackground="#3697f5", activeforeground="white")
minusBtn.grid(row=2, column=3, padx=3, pady=3)

multiBtn = Button(buttonFrame, text='x',
                  font=font, width=5, relief='ridge', fg="#fff", bg="#fe9037", activebackground="#3697f5", activeforeground="white")
multiBtn.grid(row=1, column=3, padx=3, pady=3)

divideBtn = Button(buttonFrame, text='/',
                   font=font, width=5, relief='ridge', fg="#fff", bg="#fe9037", activebackground="#3697f5", activeforeground="white")
divideBtn.grid(row=0, column=3, padx=3, pady=3)

# Binding All Buttons
plusBtn.bind('<Button-1>', btn_click)
minusBtn.bind('<Button-1>', btn_click)
multiBtn.bind('<Button-1>', btn_click)
divideBtn.bind('<Button-1>', btn_click)

zeroBtn.bind('<Button-1>', btn_click)
exBtn.bind('<Button-1>', btn_click)
eqlBtn.bind('<Button-1>', btn_click)
dotBtn.bind('<Button-1>', btn_click)

rootBtn.bind('<Button-1>', btn_click)


window.mainloop()
