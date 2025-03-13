import customtkinter as ctk
from gui.constants.settings import *
from gui.constants.state_enum import AppStates

class timervisual(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.first = True
        #variables
        self.timenow = 0
        #tkinter variables
        self.ticks = ctk.StringVar()
        #widgets
        self.timelabel =ctk.CTkLabel(self, textvariable=self.ticks, font=TIMER_FONT)
        self.timelabel.pack()

        #create numeric visual on the first loop
        if self.first == True:
            self.first = False
            self.setTimeString()
            if self.parent.appstate == AppStates.STARTED:
                self.after(TICK_RATE, self.updateTimer)

        # self.after(10000, self.updateTimer)
        self.pack()

    def updateTimer(self):
        if self.parent.status is AppStates.STARTED:
            self.timenow = self.timenow + TICK_RATE/1000
            self.after(TICK_RATE, self.updateTimer)
        self.setTimeString()

    def setTimeString(self):
        hours = self.timenow // 3600
        minutes =( self.timenow%3600) //60
        text = "{0:02}:{1:02}"
        self.ticks.set(text.format(int(hours),int(minutes)))
        # self.parent.update()
