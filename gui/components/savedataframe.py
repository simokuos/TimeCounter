import customtkinter as ctk
from database.datacontrol import datacontrol
from gui.components import taskchoice

class savedataframe(ctk.CTkFrame):
    def __init__(self, parent, timemanager):
        super().__init__(parent)
        # self.title("Save Data?")
        self.timemanager = timemanager
        self.parent = parent
        self.minutes =  ctk.DoubleVar()
        self.timestamp = ctk.StringVar()

        self.minutes.set(str(self.timemanager.getDifferenceInMinutes()))
        self.timestamp.set(str(self.timemanager))

        self.close_data = ctk.CTkButton(self, text='x', command=self.closeData)
        self.close_data.pack()

        self.minutes_entry = ctk.CTkEntry(self, textvariable=self.minutes)
        self.minutes_entry.pack()

        self.h_min_entry = ctk.CTkEntry(self, textvariable=self.timestamp)
        self.h_min_entry.pack()

        self.options = taskchoice(self)

        self.submitinfo = ctk.CTkButton(self, text='submit info', command=self.saveData)
        self.submitinfo.pack()
        self.pack()

    @property
    def choice(self):
        return self.options.choice

    def closeData(self):
        self.parent.toggleSaveData()

    def saveData(self):
        #add messagebox confirmation
        seconds = self.timemanager.getDifferenceInSeconds()
        date = self.timemanager.time[0].time
        project_name = self.choice
        closeWindow = datacontrol.saveToDatabase(project_name, date, seconds)
        if(closeWindow):
            self.parent.toggleSaveData()
