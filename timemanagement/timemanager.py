from .timestamp import timestamp
# from timestamp import timestamp
class timemanager:
    def __init__(self):
        self.timelist = []

    @property
    def time(self):
        return self.timelist

    @time.setter
    def time(self, timelist):
        self.timelist = timelist

    def addTime(self):
        self.timelist.append(timestamp())

    def getTime(self, n):
        return self.timelist[n].time

    def setTime(self, t):
        self.timelist.append(t)

    def removeAllTimes(self):
        self.timelist.clear() # same as del s[:]

    def getDifferenceInSeconds(self):
        index = 0
        seconds = 0
        list_len = len(self.timelist)

        if not list_len%2 == 0 and list_len > 0:
            list_len = list_len - 1

        while(index < list_len):
            if(self.timelist[index] != None):
                seconds += self.timelist[index].timeDifference(self.timelist[index + 1])
            index = index + 2
        return seconds

    def getDifferenceInMinutes(self):
        seconds = self.getDifferenceInSeconds()
        minutes = seconds //60
        return minutes

    def secondsToTimeString(self, t):
        if(t >= 60):
            hours = t // 3600
            minutes =( t%3600) //60
            text = "{0}h {1}min"
            return text.format(int(hours), int(minutes))
        else:
            text = "seconds: {:.2f}"
            return text.format(t)

    def __str__(self):
        if(self.timelist != []):
            return self.secondsToTimeString(self.getDifferenceInSeconds())
        return "no work done"

if __name__ == "__main__":
    test = timemanager()
    test.addTime()
    test.addTime()
    test.addTime()
    test.addTime()
    time = test.getDifferenceInSeconds()
    print(test.getTime(0))
    print(time)
    print(str(test))
    test.removeAllTimes()
    print(str(test))
