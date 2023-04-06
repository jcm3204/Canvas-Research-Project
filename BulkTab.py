import tkinter as tk
from ttkwidgets import CheckboxTreeview
from CanvasConnection import getAssignments
from CanvasConnection import deleteAssignments

def makeBulkTab(root):
    # Bulk Tab (tab2)
    # The bulk tab will be able to list the assignments from a Canvas course
    # Professers will be able to select assignments (via checkboxes) and 
    # delete them or move them to a new Module

    # create checkboxtree to list assignments
    tree = CheckboxTreeview(root)

    # Get list of all assignmnets from our Canvas course (found in CanvasConnection.py)
    # and create checkboxes for all assignments in this course
    def show_assignments():

        # grab the list of current assignments from our Canvas course
        # using Rachel's code (CanvasConnection.py)
        assignments = getAssignments()

        # Create a label to show our assignments
        assingmentLabel = tk.Label(root, text = "List of Assignments: ")
        assingmentLabel.pack(side="top")

        # place the list of assingments on our GUI
        tree.pack(side="top")
        for a in assignments:
            tree.insert("", "end", a.id, text=a)

        # add a button to delete all checked assignments from Canvas
        # and also remove them from our list
        deleteButton = tk.Button(root, text="Delete Assigments", command=getDeleted)
        deleteButton.pack(side="top", pady = 50)
  
    # Create a button generate a list of all assignments
    button = tk.Button(root, text="Show Assigments", command=show_assignments)
    button.pack(side="top", pady = 50)

    # This method will be called by the "Delete Assignments" button
    # It will grab a list of the assignments to be deleted
    # This list will be sent back to Rachel's program which deletes 
    # the assignments from Canvas
    def getDeleted():
        deleted = tree.get_checked()
        deleteAssignments(deleted)
        for box in deleted:
            tree.delete(box)