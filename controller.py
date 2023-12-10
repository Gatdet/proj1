from model import Model

class Controller:
    """
    creates a controller
    """
    def __init__(self) -> None:
        self.__model = Model()
    
    def main(self) -> None:
        """
        creates the window"""
        self.__model.main()


if __name__=="__main__":
    calc = Controller()
    calc.main()