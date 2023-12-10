from view import View

from tkinter import messagebox

class Model():
    def __init__(self) -> None:
        """
        this creates a model object that handles all the logic for the calculator.
        it gives the buttons command and handles the what each button does"""
      
        self.view = View()
        self.__total = 0
        self.__problem= ""

        self.view.btn1.config(command= lambda: self.clicked("1"))
        self.view.btn2.config(command= lambda: self.clicked("2"))
        self.view.btn3.config(command= lambda: self.clicked("3"))
        self.view.btn4.config(command= lambda: self.clicked("4"))
        self.view.btn5.config(command= lambda: self.clicked("5"))
        self.view.btn6.config(command= lambda: self.clicked("6"))
        self.view.btn7.config(command= lambda: self.clicked("7"))
        self.view.btn8.config(command= lambda: self.clicked("8"))
        self.view.btn9.config(command= lambda: self.clicked("9"))
        self.view.btn0.config(command= lambda: self.clicked("0"))
        self.view.btnadd.config(command= lambda: self.clicked("+"))
        self.view.btndivision.config(command= lambda: self.clicked("/"))
        self.view.btnmult.config(command= lambda: self.clicked("*"))
        self.view.btnsub.config(command= lambda: self.clicked("-"))
        
        self.view.btnback.config(command= self.back)        
        self.view.btndecimal.config(command= lambda: self.clicked("."))
        self.view.btnclear.config(command=self.clear)
        self.view.btnequal.config(command=self.calculation)
        self.view.equation.config(state= "disabled")

        

    def main(self) -> None:
        """
        this will allow access to the view window
        """
        self.view.main()



    def back(self) -> None:
        """
        this will delete the last number or button pressed
        """
        self.__problem=self.__problem[:-1]
        self.view.expression.set(self.__problem)

    def clear(self) -> None:
        """
        when pressed it will make the entry editable and delete the content. then it will make it unclickable again
        """
        self.view.equation.config(state= "normal")
        self.__problem=""
        self.view.equation.delete(0, "end")
        self.view.equation.config(state= "disabled")
    
    def clicked(self, num) -> None:
        """
        this function takes in a number and adds it to the equation and updates the equation shown
        """
        self.__problem+=num
        self.view.expression.set(self.__problem)
        self.view.equation.config(textvariable=self.view.expression)


    def calculation(self) -> None:
        """
        this function is in charge of the calculations and checking for errors in the equation
        
        """
        try: #testing if the equation is valid
            self.__total = str(eval(self.view.equation.get()))

            self.view.expression.set(self.__total)
            self.__problem =self.__total
            
        except: #if not then show a messagebox
            messagebox.showerror("Error", "Error Occured") 

  


