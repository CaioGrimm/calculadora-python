from tkinter import *


class Calc:

    def __init__(self):

        self.window = Tk()
        self.window.title("Calc")
        self.window.resizable(0, 0)

        self.screen_number = Entry(self.window, font="Arial 20 bold", bg="#1d2f38", fg="white", width=25)
        self.screen_number.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        self.button1 = Button(self.frame, bg="orange", bd=1, text="1", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("1"))
        self.button2 = Button(self.frame, bg="orange", bd=1, text="2", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("2"))
        self.button3 = Button(self.frame, bg="orange", bd=1, text="3", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("3"))
        self.button4 = Button(self.frame, bg="orange", bd=1, text="4", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("4"))
        self.button5 = Button(self.frame, bg="orange", bd=1, text="5", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("5"))
        self.button6 = Button(self.frame, bg="orange", bd=1, text="6", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("6"))
        self.button7 = Button(self.frame, bg="orange", bd=1, text="7", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("7"))
        self.button8 = Button(self.frame, bg="orange", bd=1, text="8", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("8"))
        self.button9 = Button(self.frame, bg="orange", bd=1, text="9", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("9"))
        self.button_plus = Button(self.frame, bg="orange", bd=1, text="+", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("+"))
        self.button_minus = Button(self.frame, bg="orange", bd=1, text="-", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("-"))
        self.button_multi = Button(self.frame, bg="orange", bd=1, text="x", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("*"))
        self.button_div = Button(self.frame, bg="orange", bd=1, text="/", font="arial 20 bold", fg="white",
                              width=5, height=3, command=lambda: self.touch("/"))
        self.button_equal = Button(self.frame, bg="orange", bd=1, text="=", font="arial 20 bold", fg="white",
                              width=11, height=3, command=self.total)
        self.button_clear = Button(self.frame, bg="orange", bd=1, text="C", font="arial 20 bold", fg="white",
                              width=5, height=3, command=self.clear)

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.button_div.grid(row=0, column=3)
        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)
        self.button_multi.grid(row=1, column=3)
        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)
        self.button_minus.grid(row=2, column=3)
        self.button_plus.grid(row=3, column=3)
        self.button_equal.grid(row=3, column=0, columnspan=2)
        self.button_clear.grid(row=3, column=2)

        self.window.mainloop()

    def touch(self, num):
        self.screen_number.insert(END, num)

    def clear(self):
        self.screen_number.delete(0, END)

    def total(self):
        calc = eval(self.screen_number.get())
        self.screen_number.delete(0, END)
        self.screen_number.insert(END, calc)

Calc()
