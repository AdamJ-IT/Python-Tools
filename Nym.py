#header
from tkinter import *
from tkinter import filedialog
import re

root = Tk()
root.title("Nym - A Bulk Renaming Program")


#Frame1 - Selecting and Displaying filenames

def getname():
    global oldnames
    root.filename = filedialog.askopenfilename(initialdir = "/Users/Jinx/Desktop/test", title="select a file", filetypes=(("png files", "*.png"),("all files","* . *")))
    oldnames=root.filename
    oldnamesdisplay = displayBox.insert(0,oldnames)

frame1 = LabelFrame(root, text="", padx = 50,pady=50)
frame1.grid(row = 0, column=0)

chFile = Button(frame1, text="Select files to rename", command = getname)
display = Label(frame1, text="Display")
displayBox = Entry(frame1,text="", width=20, borderwidth = 5)
chFile.grid(row = 0, column = 0)
display.grid(row = 1, column = 0,columnspan = 3)
displayBox.grid(row = 2, column = 0,columnspan = 3)

#Frame2 - Resulting filenames

def resultname():
    #this matches filenames including spaces
    newnameRegex = re.compile(r'[ \w-]+?(?=\.)')
    matches = newnameRegex.search(oldnames)
    global resultName
    global newnames
    
    #variable to constantly be changing
    resultName = matches.group()
    str(resultName)
    newnames = resultBox.insert(0,resultName)

frame2 = LabelFrame(root, text="", padx =50, pady=50)
frame2.grid(row = 1, column=0)

result = Label(frame2, text="View Result")
resultBox = Entry(frame2,text="", width=20, borderwidth = 5)
result.grid(row = 3, column = 0)
resultBox.grid(row = 4, column = 0)
check = Button(frame2,text="Check Names", command=resultname)
check.grid(row = 5, column = 0)


#Frame 3 - Data Manipulation


frame3 = LabelFrame(root, text="", padx =50,pady=50)
frame3.grid(row =0, column=1)

#Add prefix Button
def addprefix():
    prefixString = prefixEntry.get()
    global newnames
    newnames = resultBox.insert(0, prefixString)


prefix = Label(frame3, text="Prefix")
prefixEntry = Entry(frame3, width = 10, borderwidth = 5)
addprefix = Button(frame3, text="Add", command = addprefix) 

prefix.grid(row =0, column = 4)
prefixEntry.grid(row=0, column =5)
addprefix.grid(row = 0, column =6)

#Add Suffix button

def addsuffix():
    suffixString = suffixEntry.get()
    global newnames
    newnames = resultBox.insert(END,suffixString)


suffix = Label(frame3, text="Suffix")
suffixEntry = Entry(frame3, width = 10, borderwidth = 5)
addsuffix = Button(frame3, text="Add", command = addsuffix)

suffix.grid(row =1, column = 4)
suffixEntry.grid(row = 1, column =5)
addsuffix.grid(row = 1, column =6)

#Find and Replace text Button

#def findandreplace():
 #   find = 


    
replaceInput = Label(frame3, text="Replace")
replaceInputBox = Entry(frame3, width = 10, borderwidth = 5)
replaceOutput = Label(frame3, text="With")
replaceOutputBox = Entry(frame3, width = 10, borderwidth = 5)
replaceButton = Button(frame3, text="Replace")

replaceInput.grid(row =2, column =4)
replaceInputBox.grid(row = 2, column =5)
replaceOutput.grid(row =2, column = 6)
replaceOutputBox.grid(row = 2, column =7)
replaceButton.grid(row = 2, column = 8)


#1.4 frame4
frame4 = LabelFrame(root, text="", padx =50,pady=50)
frame4.grid(row =1, column=1)

x = Label(frame4, text="Placeholder")
x.grid(row=1, column=1)


#creates the main loop that keeps the program running 
root.mainloop()
