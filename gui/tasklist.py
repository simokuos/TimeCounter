from database.datacontrol import datacontrol

class tasklist:
    def __init__(self, tasktype = 'project name', useDefaults = True):
        self.useDefaults =useDefaults
        if self.useDefaults == True:
            start_option = " choose a {0}"
            end_option = "+ Add new {0}"
            self.tasklist = [start_option.format(tasktype), end_option.format(tasktype)]
        else:
            self.tasklist = [tasktype]
        self.currentTask = self.tasklist[0]
        self.addValuesFromDatabase()


    @property
    def tasks(self):
        return self.tasklist

    @property
    def curr_task(self):
        return self.currentTask

    @curr_task.setter
    def curr_task(self, task):
        self.currentTask = task

    def addValuesFromDatabase(self):
        saved_values = datacontrol.initTaskList()
        if not saved_values == []:
            self.updateTaskList(saved_values)

    def addTask(self, option):
        self.tasklist.insert(-1, option)
        self.currentTask = self.tasklist[-1]

    def updateTaskList(self, tasklist):
        if self.useDefaults == True:
            temp_value = self.tasklist.pop()
            self.tasklist.extend(tasklist)
            self.tasklist.append(temp_value)
        else:
            self.tasklist.extend(tasklist)
