#python modules
import customtkinter as ctk
from enum import Enum
#application modules
from timemanagement.timemanager import timemanager
from .settings import *
from .tasklist import tasklist
from database.datacontrol import datacontrol

class AppStates(Enum):
    INACTIVE = 0
    STARTED = 1
    PAUSED = 2
    STOPPED = 3

class CountGUI(ctk.CTk):
    def __init__(self, status = AppStates.INACTIVE):
        super().__init__()
        self.title("Timer")
        #attributes
        self.status = status

        #widgets
        self.timer = timervisual(self)
        self.buttons = buttongrid(self)

        self.savedata_window = None

        self.mainloop()

    @property
    def appstate(self):
        return self.status

    @appstate.setter
    def appstate(self, status):
        self.status = status

    def openSaveDataWindow(self):
        if self.savedata_window is None or not self.savedata_window.winfo_exists():
            self.savedata_window = SaveDataWindow(self, self.buttons.timelist)
        else:
            self.savedata_window.focus()

    def resetTimer(self):
        self.buttons.resetTimer()
        self.timer.resetTimerVisual()
        self.appstate = AppStates.INACTIVE

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

    def resetTimerVisual(self):
        self.timenow = 0
        self.setTimeString()

    def updateTimer(self):
        if(self.parent.appstate == AppStates.STARTED):
            self.timenow = self.timenow + TICK_RATE/1000
            #print("timenow :", self.timenow)
            self.after(TICK_RATE, self.updateTimer)
        self.setTimeString()

    def setTimeString(self):
        hours = self.timenow // 3600
        minutes =( self.timenow%3600) //60
        text = "{0:02}:{1:02}"
        self.ticks.set(text.format(int(hours),int(minutes)))

class buttongrid(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.timemanager = timemanager()
        self.segmented_var = ctk.StringVar(value="")
        if self.parent.appstate == AppStates.STARTED:
            self.timemanager.addTime()
            self.segmented_var.set(value="Start")

        # set grid
        # self.grid_columnconfigure((0,1,2),weight = 1)
        # self.grid_rowconfigure(0,weight = 1)


        self.segmented = ctk.CTkSegmentedButton(
                        self,
                        values = ["Start","Pause","Stop"],
                        command = self.button_event_call,
                        variable = self.segmented_var
        )
        self.segmented.pack()

        # self.button_start = ctk.CTkButton(
        #     self,
        #     text="start",
        #     command=self.start_time)
        # self.button_start.grid(column=0, row=0)
        #
        # self.button_pause = ctk.CTkButton(
        #     self,
        #     text="pause",
        #     command= self.pause_time)
        # self.button_pause.grid(column=1, row=0)
        #
        #
        # self.button_stop = ctk.CTkButton(
        #     self,
        #     text="stop",
        #     command=self.stop_time
        #     )
        # self.button_stop.grid(column=2, row=0)
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

            self.parent.openSaveDataWindow()

class SaveDataWindow(ctk.CTkToplevel):
    def __init__(self, parent, timemanager):
        super().__init__(parent)
        self.title("Save Data?")
        self.timemanager = timemanager
        self.parent = parent
        self.minutes =  ctk.DoubleVar()
        self.timestamp = ctk.StringVar()

        self.minutes.set(str(self.timemanager.getDifferenceInMinutes()))
        self.timestamp.set(str(self.timemanager))

        self.minutes_entry = ctk.CTkEntry(self, textvariable=self.minutes)
        self.minutes_entry.pack()

        self.h_min_entry = ctk.CTkEntry(self, textvariable=self.timestamp)
        self.h_min_entry.pack()

        self.options = TaskChoice(self)

        self.submitinfo = ctk.CTkButton(self, text='submit info', command=self.saveData)
        self.submitinfo.pack()

    @property
    def choice(self):
        return self.options.choice

    def saveData(self):
        #add messagebox confirmation
        seconds = self.timemanager.getDifferenceInSeconds()
        date = self.timemanager.time[0].time
        project_name = self.choice
        closeWindow = datacontrol.saveToDatabase(project_name, date, seconds)
        if(closeWindow):
            self.parent.resetTimer()
            self.destroy()

class TaskChoice(ctk.CTkOptionMenu):
    def __init__(self, parent, tasklist = tasklist()):
        super().__init__(parent,
                        values=tasklist.tasks,
                        command=self.taskchoice_event)

        self.pack()
        self.set(tasklist.curr_task)
        self._parent = parent
        self._tasklist = tasklist
        self._newchoice = ""

    @property
    def choice(self):
        return self._newchoice

    @choice.setter
    def choice(self, newchoice):
        self._newchoice = newchoice

    def taskchoice_event(self, choice):
        if(choice[0] == '+'):
            # add messagebox that calls updatetask on given entry
            new_input = ctk.CTkInputDialog(text = "Give the new option:", title="")
            self.choice = new_input.get_input()
            self._tasklist.addTask(self.choice)
            self._tasklist.curr_task = self.choice
            self.set(self.choice)
            self.configure(values=self._tasklist.tasks)
        else:
            self.choice = choice
            self.set(choice)

if __name__ == "__main__":
    datacontrol.initTables()
    CountGUI(AppStates.STARTED)
