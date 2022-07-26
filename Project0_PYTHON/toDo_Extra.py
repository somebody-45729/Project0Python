# Extra class/module handler here

class toDo_Task():
    def __init__(self, task, month, day, year, priority):
        self._task = str(task)
        self._month = int(month)
        self._day = int(day)
        self._year = int(year)
        self._priority = str(priority)

        def __str__(self):
            return "Task: " + self._task + ", Month: " + str(self._month) + ", Day: " + str(self._day) + ", Year: " + str(self._year) + ", Priority: " + self._priority

class userEntry(toDo_Task):
    def chosenTask(self):
        print("***Task is Chosen***")
    