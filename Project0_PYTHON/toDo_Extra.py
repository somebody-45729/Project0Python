# Extra class/module handler here

class toDo_Task():
    def __init__(self, task, date, priority):
        self._task = str(task)
        self._date = str(date)
        self._priority = str(priority)

class userEntry(toDo_Task):
    def chosenTask(self):
        print("***Task is Chosen***")
    