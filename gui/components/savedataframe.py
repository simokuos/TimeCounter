import customtkinter as ctk
from database.datacontrol import datacontrol
from gui.components.workoptions import WorkOptions
from database.model import Model

class savedataframe(ctk.CTkFrame):
    def __init__(self, parent, used_seconds):
        super().__init__(parent)
        self.model = Model()
        # self.title("Save Data?")
        self.used_seconds = used_seconds
        self.parent = parent
        self.minutes =  ctk.DoubleVar()
        self.timestamp = ctk.StringVar()

        self.minutes.set(str(self.used_seconds //60))
        self.timestamp.set(str(self.usedTimeToString()))

        self.close_data = ctk.CTkButton(self, text='x', command=self.closeData)
        self.close_data.pack()

        self.minutes_entry = ctk.CTkEntry(self, textvariable=self.minutes)
        self.minutes_entry.pack()

        self.h_min_entry = ctk.CTkEntry(self, textvariable=self.timestamp)
        self.h_min_entry.pack()

        values = self.model.get_recent_unique_projects()
        self.options =  WorkOptions(self, values, True)

        self.submitinfo = ctk.CTkButton(self, text='submit info', command=self.saveData)
        self.submitinfo.pack()
        self.pack()

    def usedTimeToString(self):
        if self.used_seconds >= 60:
            hours   = self.used_seconds // 3600
            minutes = (self.used_seconds%3600) //60
            return "{0}h {1}min".format(int(hours), int(minutes))
        else:
            return "seconds: {:.2f}".format(self.used_seconds)

    def closeData(self):
        self.parent.toggleSaveData()

    def saveData(self):
        if self.options.hasOption():
            seconds = self.used_seconds
            project_name = self.options.get()
            self.model.add_workhours(project_name, seconds)
            self.parent.toggleSaveData()
