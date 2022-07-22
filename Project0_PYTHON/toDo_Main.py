import re
import logging
import sys
from datetime import datetime
import csv

from toDo_Extra import toDo_Task, userEntry

# NEED TO ASK HELP IN SETTING UP CONNECTION WITH .csv file read/write


def main():
    logging.basicConfig(filename = "To_Do_List.log", level = logging.DEBUG, format='%(asctime)s :: %(message)s')

    print("******** TO-DO LIST ********")
    
    csvName = "toDo_Items.csv"
    lst_toDo = []
    lst_toDo = load_Task(csvName)
    logging.info("Loading tasks into the list....")

    while(True):
        toDo = insert_Task()
        if toDo == None:
            break
        logging.info("Inserted new task!")
        lst_toDo.append(toDo)

    for list in lst_toDo:
        print(list)
    
    save_Task(csvName, lst_toDo)
    logging.info("Saving Task to " + csvName)
    print("\n\n")

def save_Task(csvName, lst_toDo):
    '''
    Save all submitted tasks to the csv file

    No return for this case
    '''
    with open(csvName, "w") as f:
        for toDo in lst_toDo:
            if type(toDo) == userEntry:
                f.write("Task, " + toDo._task + "," + str(toDo._date) + "," + toDo._priority + ",\n")
            else:
                pass


def load_Task(csvName):
    '''
    Load into the list, return the list
    '''
    lst_toDo = []

    with open(csvName, "r") as f:
        for row in f:
            infoLine = row.split(',')
            if infoLine[0] == "user":
                toDo = userEntry(infoLine[1], infoLine[2], infoLine[3])
            else:
                toDo = None

            if toDo != None:
                lst_toDo.append(toDo)
    return lst_toDo

def insert_Task() -> toDo_Task:
    '''
    ACTUALLY PROMPTING USER FOR INFO;

    Need the following: TASK -- DATE -- PRIORITY

    (TASK can be whatever, but date needs the datetime standard, and priority only limited to high, medium, or low choices)
    '''

    print("\nPlease select your entry for your to-do list:")
    print("\t1) userEntry")
    print("\t2 exit")
    userInput = input(">>>> ")

    if userInput not in ["1"]:
        return None

    while True:
        # Enter the name of the task/event
        try:
            event = input("\nEnter the task/event:\n>>>>")
            check = re.search(',', event)

            if check != None:
                raise ValueError
        except ValueError as ve:
            print("\nPLEASE AVOID COMMAS FOR SET EVENTS/TASKS:\n")
            logging.error("trying again")
        else:
            break

    while True:
        # Enter the date relevant to the task/event
        try:
            month = int(input("\nENTER MONTH OF EVENT/TASK IN NUMERIC FORM:\n>>>"))
            day = int(input("\nENTER DAY OF EVENT/TASK IN NUMERIC FORM:\n>>>"))
            year = int(input("\nENTER YEAR OF EVENT/TASK IN NUMERIC FORM:\n>>>"))
            date = datetime.date(month, day, year)
            check = re.search("[a-zA-Z].+ ',' ", date)

            if check != None:
                raise ValueError
        except ValueError as ve:
            print("\nNOT A PROPER INTEGER, PLEASE TRY AGAIN:\n")
            logging.error("Either entered a string character or a comma. Trying again....")
        else:
            break

    while True:
        # Now priorties: LOW, MEDIUM, or HIGH
        priority = input("\nIS THE PRIORITY OF EVENT/TASK LOW, MEDIUM, or HIGH:\n>>>")
        if priority.lower() != "low" or "medium" or "high":
            raise Exception("USER DID NOT ENTER high, medium, or low as input!")
        else:
            break

    
    if userInput == "1":
        toDo = userEntry(event, date, priority)
    else:
        toDo = None

    return toDo


if __name__ == "__main__":
    main()



            
        
       

