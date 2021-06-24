import sqlite3
from tkinter import *
from tkinter import font as tkFont
import datetime

root = Tk()
root.title('Stool-IO')
root.geometry('400x400')
root.configure(bg='#3dd9d9')


clicked = StringVar()
clicked.set('Select Poop Type')

poop_type = 'non selected'

#create sqlite3 database:
"""conn = sqlite3.connect('stool_log.db')
c = conn.cursor()
c.execute(CREATE Table logs (
        date text,
        time text,
        type text,
        comment text
        ))
conn.commit()
conn.close()"""

def on_select(selected): # defines function for Dropdown Menue(OptionMenu)
    global poop_type
    poop_type = selected
def on_click(): # defines function for button
    global poop_type
    dt = datetime.datetime.now()
    # SQL code follows:
    conn = sqlite3.connect('stool_log.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs VALUES(:date,:time,:type,:comment)",{
            'date': dt.strftime("%B %d,%Y"),
            'time': dt.strftime("%H:%M %Z"),
            'type': poop_type,
            'comment': myEntry.get()
    })
    conn.commit()
    conn.close()
    messagebox.showinfo('showinfo','submitted')
    #root.messagebox.showinfo(title="Success",message="Successfully logged input")


# define options for Dropdown Menu (OptionMenu)
pooptypes=[
    '1. Separate hard lumps',
    '2. Sausage shaped but lumpy',
    '3. Sausage shaped but with cracks',
    '4. Sausage or snake, smooth and soft' ,
    '5. Soft blobs with clear-cut edges',
    '6. Fluffy pieces with rigged edges, mushy',
    '7. Watery, no solid pieces'
]

# lay out/ initialize widgets for main window below
rale20 = tkFont.Font(family='raleway', size=20)
typeLabel = Label(root, text='Stool Type: ', font="rale20")
aDropbox = OptionMenu(root, clicked, *pooptypes, command=on_select)
commentLabel = Label(root, text='Comments:', font="rale20")
myEntry = Entry(root, font="rale20")
submitbtn = Button(root, text='Submit', command=on_click, font="rale20")
#chartbtn = Button(root, text='See Log', command=see_log, font="raleway")

# display widgets on screen
typeLabel.grid(row=0, column=0)
aDropbox.grid(row=0, column=1)
commentLabel.grid(row=2, column=0)
myEntry.grid(row=3, column=0, columnspan=2)
submitbtn.grid(row=4, column=0, columnspan=2)
#chartbrn.grid(row=5, cloumn=0, columnspan=2)

root.mainloop()
