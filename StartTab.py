import tkinter as tk
from tkinter import ttk
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
        
        createXLSX(name, first_day, last_day, meeting_days, user_days_off, recurringDays)

    # add a text box to enter class title
    label = tk.Label(root, text="Class Name:")
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

    def select_days():
        for day in days:
            if day not in dayTree.get_checked():
                dayTree.change_state(day, "checked")

    selectAll = tk.Button(root, text="Select All Days", command=select_days)
    selectAll.pack(side="top", pady = 10)
    
    # create a dictionary to hold our recurring days
    # keys are day (0-4) and values are description of recurring event (e.g. Lab Day)
    recurringDays = {}
    
    # Allow users to select recurring days off and give reasoning
    def select_recurring():
        #create a pop-up window 
        window = tk.Toplevel()
        window.title("Secondary Window")
        window.config(width=300, height=200)
        
        def add_reasoning():
            selection = "You selected " + getDay(var.get())
            optionLabel = tk.Label(window, text=selection)
            optionLabel.pack(side="top", pady=10)
            
             # add a text box to enter class title
            label = tk.Label(window, text="Enter reason for recurring day: ")
            label.pack(side="top", pady=10)
            recurr = tk.Entry(window, bd=5)
            recurr.pack(side="top")
            
            def save_day():
                day = var.get()
                reason = recurr.get()
                recurringDays[day] = reason
                window.destroy
            
            #create button to save day
            button_save = ttk.Button(window, 
                    text="Save Recurring Day",
                    command=save_day)
            button_save.pack(side="bottom")
            
            #create button to close window
            button_save = ttk.Button(window, 
                    text="Close Window",
                    command=window.destroy)
            button_save.pack(side="bottom")
            

        var = tk.IntVar()
        R1 = tk.Radiobutton(window, text="M", variable=var, value=0,
                  command=add_reasoning)
        R1.pack(side="bottom")

        R2 = tk.Radiobutton(window, text="T", variable=var, value=1,
                  command=add_reasoning)
        R2.pack(side="bottom")

        R3 = tk.Radiobutton(window, text="W", variable=var, value=2,
                  command=add_reasoning)
        R3.pack(side="bottom")
        
        R4 = tk.Radiobutton(window, text="R", variable=var, value=3,
                  command=add_reasoning)
        R4.pack(side="bottom")

        R5 = tk.Radiobutton(window, text="F", variable=var, value=4,
                  command=add_reasoning)
        R5.pack(side="bottom")
        
    
    # Add a button to select special recurring days
    reccurButton = tk.Button(root, text="Select Recurring Special Days", command=select_recurring)
    reccurButton.pack(side="top", pady = 10)

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
    button = tk.Button(root, text="Create Spreadsheet", command= createFile)
    button.pack(side = "top", pady=10)
