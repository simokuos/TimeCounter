from datetime import datetime,timedelta
import time

class timestamp:
    def __init__(self):
        self._time = datetime.now()

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, t):
        self._time = t

    def resetTime(self):
        self._time = datetime.now()

    def timeDifference(self, t):
        start_date = self._time
        end_date = t
        delta = end_date._time - start_date
        return delta.total_seconds()

    def listTimeDifference(start_times, stop_times):
        temp = None
        delta = timedelta(days= 0)
        if(len(start_times) > 0 ):
            for index, time in enumerate(start_times):
                if (index < len(stop_times)):
                    temp = stop_times[index].time - time.time
                    delta += temp
        return delta.total_seconds()
