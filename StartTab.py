import tkinter as tk
from tkcalendar import Calendar, DateEntry
from ttkwidgets import CheckboxTreeview
from GuiHelpers import getDay
from CreateXLSX import createXLSX

def makeStartTab(root):
    # Start Tab (tab1)

    # add method to create xlsx file
    def createFile():
        name = title.get() 
        first_day = cal1.get_date() 
        last_day = cal2.get_date() 
        meeting_days = dayTree.get_checked() 
        
        createXLSX(name, first_day, last_day, meeting_days, user_days_off)

    # add a text box to enter class title
    label = tk.Label(root, text="Enter Class Name:")
    label.pack(side="top", pady=10)
    title = tk.Entry(root, bd=5)
    title.pack(side="top")

    # add a box to select the first day of semester
    L1 = tk.Label(root, text="Select First Day: ")
    L1.pack(side="top", pady=10)
    cal1 = DateEntry(root, selectmode='day')
    cal1.pack(side="top")

    # add a box to select the last day of semester
    L2 = tk.Label(root, text="Select Last Day: ")
    L2.pack(side="top", pady=10)
    cal2 = DateEntry(root, selectmode='day')
    cal2.pack(side="top")

    # add option to select days of the week
    # this will be a list of 5 check buttons M-F
    label_days = tk.Label(root, text="Select Days of Week:")
    label_days.pack(side="top", pady=10)

    dayTree = CheckboxTreeview(root, height = 5)
    dayTree.pack(side="top")

    days = [0, 1, 2, 3, 4]

    for day in days:
        dayTree.insert("", "end", day, text=getDay(day))

    # Add Calendar
    cal = Calendar(root, selectmode = 'day',
               year = 2023, month = 1,
               day = 1)
 
    cal.pack(side="top", pady = 10)

    #Create list to hold our days off
    user_days_off = []

    # Define Function to select the date
    def get_day():
        day = cal.get_date()
        if day not in dayOffBox.get("1.0", tk.END+"-1c"):
            dayOffBox.insert(tk.END, day+ "\n")
            user_days_off.append(day)

    #Create a button to pick the days off (one at a time)
    button = tk.Button(root, text="Select Day Off", command=get_day)
    button.pack(side="top", pady = 10)

    # add text box to display all selected days off
    dayOffLabel = tk.Label(root, text = "List of Selected Days Off: ")
    dayOffLabel.pack(side="top")
    dayOffBox = tk.Text(root, height = 10, width = 30)
    dayOffBox.pack(side="top")

    # finally, add a button to generate the Xlsx template
    button = tk.Button(root, text="Create XLSX File", command= createFile)
    button.pack(side = "top", pady=10)
