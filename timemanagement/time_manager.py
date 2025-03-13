from datetime import datetime
#import time

class TimeManager():
    def __init__(self):
        self.start_time = None
        self.used_time = 0

    def start(self):
        self.start_time = datetime.now()

    def stop(self):
        if self.start_time:
            end_time = datetime.now()
            self.used_time += (end_time - self.start_time).total_seconds()
            self.start_time = None

    def reset(self):
        self.start_time =  None
        self.used_time = 0
