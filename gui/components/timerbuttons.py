import customtkinter as ctk
from gui.constants.state_enum import AppStates
from gui.constants.settings import *
from timemanagement.timemanager import timemanager

class timerbuttons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.timemanager = timemanager()
        self.segmented_var = ctk.StringVar(value="")
        if self.parent.appstate == AppStates.STARTED:
            self.timemanager.addTime()
            self.segmented_var.set(value="Start")

        self.segmented = ctk.CTkSegmentedButton(
                        self,
                        values = ["Start","Pause","Stop"],
                        command = self.button_event_call,
                        variable = self.segmented_var
        )
        self.segmented.pack()

        self.pack()

    @property
    def timelist(self):
        return self.timemanager

    def resetTimer(self):
        self.timemanager = timemanager()
        self.segmented_var.set(value="")


    def button_event_call(self, value):
        match value:
            case 'Start':
                self.start_time()
            case 'Pause':
                self.pause_time()
            case 'Stop':
                self.stop_time()


    def start_time(self):
        if not self.parent.appstate == AppStates.STARTED:
            # self.start_times.append(timestamp())
            self.timemanager.addTime()
            self.parent.appstate = AppStates.STARTED
            self.parent.after(TICK_RATE, self.parent.timer.updateTimer)

    def pause_time(self):
        if(self.parent.appstate == AppStates.STARTED):
            # self.stop_times.append(timestamp())
            self.timemanager.addTime()
            self.parent.appstate = AppStates.PAUSED

    def stop_time(self):
        if not (self.parent.appstate == AppStates.INACTIVE or self.parent.appstate == AppStates.STOPPED):
            if(self.parent.appstate == AppStates.STARTED):
                self.timemanager.addTime()

            self.parent.appstate = AppStates.STOPPED

            self.parent.toggleSaveData()
