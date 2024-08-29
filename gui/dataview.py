import customtkinter as ctk
from gui.components import tasklist, taskchoice
from tkcalendar import DateEntry

class DataView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Data Viewer")

        self.tasklist = taskchoice(self)
        self.startdatechoice = CalendarDateChoice(self, "start date:")
        self.enddatechoice = CalendarDateChoice(self, "end date: ")
        self.submitbutton = ctk.CTkButton(
            self, text="search info",
            command=self.search_database)
        self.submitbutton.pack()
        self.mainloop()

    def search_database(self):
        pass

class CalendarDateChoice(ctk.CTkFrame):
    def __init__(self, parent, vartext='give date:'):
        super().__init__(parent, width=100)

        self.grid_rowconfigure(0, weight=1)
        datelabel = ctk.CTkLabel(self, text=vartext)
        datelabel.grid(row=0,column=0,padx=5, pady=5, sticky="ew")

        cal = DateEntry(self, width=12)
        cal.grid(row=0, column=1,padx=5, pady=5, sticky="ew")

        self.pack()

if __name__ == "__main__":
    DataView()
