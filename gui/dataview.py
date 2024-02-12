import customtkinter as ctk
from tasklist import tasklist
from tkcalendar import DateEntry

class DataView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Data Viewer")

        self.tasklist = TaskChoice(self)
        self.startdatechoice = CalendarDateChoice(self, "start date:")
        self.enddatechoice = CalendarDateChoice(self, "end date: ")
        self.submitbutton = ctk.CTkButton(self, text="search info", command=self.search_database)
        self.submitbutton.pack()
        self.mainloop()

    def search_database(self):
        pass

class TaskChoice(ctk.CTkOptionMenu):
    def __init__(self, parent, tasklist = tasklist('project name', False)):
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
        self.choice = choice
        self.set(choice)

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
