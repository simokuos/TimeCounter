import customtkinter as ctk

class WorkOptions(ctk.CTkOptionMenu):
    def __init__(self, parent, worklist, isUpdateable = False):

        if isUpdateable:
            worklist.append("+ add new task")
        self.worklist = worklist

        super().__init__(parent,
                        values=worklist,
                        command=self.option_event)

        self.pack()
        self.set("Choose or Add a name")
        self.isSetStartValue = True

    def hasOption(self):
        return (not self.isSetStartValue)

    def option_event(self, choice):
        self.isSetStartValue = False
        if choice[0] == '+':
                new_input = ctk.CTkInputDialog(text = "Give new option:", title="").get_input()
                end_value = self.worklist.pop()
                self.set(new_input)
                self.worklist.extend([new_input,end_value])
                self.configure(values=self.worklist)
                return None

        self.set(choice)
