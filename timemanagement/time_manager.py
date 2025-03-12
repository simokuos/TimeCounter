from datetime import datetime
#import time

class TimeManager():
    def __init__(self):
        self.start_time = None
        self.used_time = 0

    def start_time(self):
        self.start_time = datetime.now()

    def stop_time(self):
        end_time = datetime.now()
        self.used_time += (end_time - self.start_time).total_seconds()

    def usedTimeToString(self):
        if self.used_time >= 60:
            hours   = t // 3600
            minutes = (t%3600) //60
            return "{0}h {1}min".format(int(hours), int(minutes))
        else:
            return "seconds: {:.2f}".format(self.used_time)
