#python modules
import customtkinter as ctk
#application modules
from gui.components import timervisual, tasklist, savedataframe, timerbuttons

from gui.constants.state_enum import AppStates
from gui.constants.settings import *


class CountGUI(ctk.CTk):
    def __init__(self, status = AppStates.INACTIVE):
        super().__init__()
        self.title("Timer")
        #attributes
        self.status = status
        #widgets
        self.timer = timervisual(self)
        self.buttons = timerbuttons(self)

        self.savedata_window = None

        self.mainloop()

    @property
    def appstate(self):
        return self.status

    @appstate.setter
    def appstate(self, status):
        self.status = status

    def toggleSaveData(self, value=None):
        if self.savedata_window is None:
            self.timer.pack_forget()
            self.buttons.pack_forget()
            self.savedata_window = savedataframe(self, value)
        else:
            self.savedata_window.pack_forget()
            self.savedata_window = None
            self.timer.pack()
            self.buttons.pack()
            self.resetTimer()

    def resetTimer(self):
        self.buttons.resetTimer()
        self.timer.resetTimerVisual()
        self.appstate = AppStates.INACTIVE


if __name__ == "__main__":
    datacontrol.initTables()
    CountGUI(AppStates.STARTED)
