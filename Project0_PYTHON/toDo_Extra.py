# Extra class/module handler here

class toDo_Task():
    def __init__(self, task, month, day, year, priority):
        self._task = str(task)
        self._month = int(month)
        self._day = int(day)
        self._year = int(year)
        self._priority = str(priority)

class userEntry(toDo_Task):
    def chosenTask(self):
        print("***Task is Chosen***")
    