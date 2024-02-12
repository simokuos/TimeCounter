import gui.window as window
from database.datacontrol import datacontrol

def initApplication():
    datacontrol.initTables()
    window.CountGUI()

if __name__ == "__main__":
    #window.helloworld()
    initApplication()
    #tkinter._test()
