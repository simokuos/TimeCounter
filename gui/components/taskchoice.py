import customtkinter as ctk
from gui.components import tasklist
print("taskchoice should not be used")
class taskchoice(ctk.CTkOptionMenu):
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
