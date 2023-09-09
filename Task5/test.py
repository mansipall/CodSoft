from tkinter import Tk, Frame, Label, Button
import tkinter as tk


class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if (letter == self.correctLetter):
            label = Label(view, font="helvetica,15",
                          bg="#32CD32", text="RIGHT!")
            right += 1
        else:
            label = Label(view, font="helvetica,15",
                          bg="#FF3131", text="WRONG!")
        label.pack(pady=10)
        view.after(1000, lambda *args: self.unpackView(view))

    def getView(self, window):
        view = Frame(window, bg="#FFFFFF")
        Label(view, text=self.question, font="helvetica,20",
              bg="#FFFFFF").pack(pady=10)
        Button(
            view, text=self.answers[0], height=2, width=20, font="helvetica,15", bg="#DA70D6", command=lambda *args: self.check("A", view)).pack(pady=10)
        Button(
            view, text=self.answers[1], height=2, width=20, font="helvetica,15", bg="#DA70D6", command=lambda *args: self.check("B", view)).pack(pady=10)
        Button(
            view, text=self.answers[2], height=2, width=20, font="helvetica,15", bg="#DA70D6", command=lambda *args: self.check("C", view)).pack(pady=10)
        Button(
            view, text=self.answers[3], height=2, width=20, font="helvetica,1", bg="#DA70D6", command=lambda *args: self.check("D", view)).pack(pady=10)
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if (len(questions) == index + 1):
        Label(window, font="helvetica, 16", bg="#ADD8E6", text="Thank you for answering the questions. " + str(right) +
              " are correct, out of " + str(number_of_questions) + "\n Try Again !").pack(pady=10)
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()


questions = []
file = open("questions.txt", "r")
line = file.readline()
while (line != ""):
    questionString = line
    answers = []
    for i in range(4):
        answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
window.title("Quize App")
window.config(bg="#ADD8E6")
window.geometry("500x500")

heading = tk.Label(window, text="Quize App",
                   font="helvetica, 25", bg="#ADD8E6")
heading.pack(pady=20, padx=130)


button = Button(window, text="START",
                command=askQuestion, font="helvetica, 18", bg="#FFFFFF")
button.pack()
window.mainloop()
