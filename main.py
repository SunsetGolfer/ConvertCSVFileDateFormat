# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import csv
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print('Reading: ',file_path)


def readmyfile(filename):
    dates = []
    scores = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            Subject.append(row[0])
            Startdate.append(row[1])
            Starttime.append(row[2])
            Enddate.append(row[3])
            Endtime.append(row[4])
            Alldayevent.append(row[5])
            Description.append(row[6])
            Location.append(row[7])
            Private.append(row[8])
    return Subject, Startdate, Starttime, Enddate, Endtime, Alldayevent, Description, Location, Private



print(Subject)
print(Enddate)

# Subject,Start date,Start time,End Date,End Time,All day Event,Description,Location,Private
# Subject, Startdate, Starttime, Enddate, Endtime, Alldayevent, Description, Location, Private
# Douglas Manfred Winni Udo ,08.06.2020,11:00:00,08.06.2020,13:00:00,FALSE,Douglas Manfred Winni Udo ,Borkstraße 17 - 48163 Münster,FALSE
