from tkinter import *


class View(Tk): #inherits from the tkinter class
    def __init__(self) -> None:
        super().__init__()
        """
        this class creates an object that handles the visuals.
        it creates the button, entry, background color, window size, title.
        """
        
        self.title("Calculator")
        
        self.geometry("400x600")
        self.resizable(False,FALSE)
        self.config(bg="red")
        self.expression = StringVar()

        self.btn1 = Button(self, text="1", font=("arial",20), width=5)
        self.btn2 = Button(self, text="2", font=("arial",20), width=5)
        self.btn3 = Button(self, text="3", font=("arial",20), width=5)
        self.btn4 = Button(self, text="4", font=("arial",20), width=5)
        self.btn5 = Button(self, text="5", font=("arial",20), width=5)
        self.btn6 = Button(self, text="6", font=("arial",20), width=5)
        self.btn7 = Button(self, text="7", font=("arial",20), width=5)
        self.btn8 = Button(self, text="8", font=("arial",20), width=5)
        self.btn9 = Button(self, text="9", font=("arial",20), width=5)
        self.btn0 = Button(self, text="0", font=("arial",20), width=11)

        self.btndecimal = Button(self, font=("arial",20), text=".", width=5)
        self.btnequal = Button(self, font=("arial",20), text="=", width=5)
        self.btnadd = Button(self, text="+", font=("arial",20), width=5)
        self.btnsub = Button(self, text="-", font=("arial",20), width=5)
        self.btnmult = Button(self, text="x", font=("arial",20), width=5)
        self.btndivision = Button(self, text="/", font=("arial",20), width=5)
        self.btnback = Button(self, text="Back", font=("arial",20), width=11)
        self.btnclear = Button(self, text="C", font=("arial",20), width=5)
        
        
        self.btn0.place(x=10, y=530)
        self.btndecimal.place(x=205, y=530)
        self.btnequal.place(x= 305, y = 530)
        self.btn1.place(x=10, y=450)
        self.btn2.place(x=108, y=450)
        self.btn3.place(x=205, y=450)

        self.btn4.place(x=10, y=370)
        self.btn5.place(x=108, y=370)
        self.btn6.place(x=205, y=370)

        self.btn7.place(x= 10, y=290)
        self.btn8.place(x= 108, y=290)
        self.btn9.place(x= 205, y=290)
        self.btn7.place(x= 10, y=290)

        self.btnback.place(x= 10, y=210)
        self.btnclear.place(x= 205, y=210)
        self.btndivision.place(x=305, y = 210)


        self.btnmult.place(x =305, y =290)        
        self.btnsub.place(x=305, y= 370)
        self.btnadd.place(x=305, y=450)

        self.equation = Entry(self, justify= RIGHT, font=("arial",25),width=29,disabledforeground="black")
        self.equation.place(x=10, y=10, height=140, width= 380)
        

        
    def main(self) -> None:

        """
        this creates the window
        """
        self.mainloop()
