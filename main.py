import sqlite3
from tkinter import *
import datetime

root = Tk()
root.title('Poop Tracker')
root.geometry('400x400')


clicked = StringVar()
clicked.set('Select Poop Type')

poop_type = 'non selected'
def on_select(selected): # defines function for Dropdown Menue(OptionMenu)
    global poop_type
    poop_type = selected
def on_click(): # defines function for button
    global poop_type
    dt = datetime.datetime.now()
    # SQL code follows:
    conn = sqlite3.connect('log.db')
    c = conn.cursor()
    c.execute("""INSERT INTO log (
            Date,
            Time,
            Type,
            Comment
    ) VALUES(?,?,?,?)
    """,(
            dt.strftime("%B %d,%Y"),
            dt.strftime("%H:%M %Z"),
            poop_type,
            myEntry.get()
    ))
    conn.commit()
    c.close()
    conn.close()


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
typeLabel = Label(root, text='Type: ')
aDropbox = OptionMenu(root, clicked, *pooptypes, command=on_select)
commentLabel = Label(root, text='Comments:')
myEntry = Entry(root)
submitbtn = Button(root, text='Submit', command=on_click)

# display widgets on screen
typeLabel.grid(row=0, column=0)
aDropbox.grid(row=0, column=1)
commentLabel.grid(row=2, column=0)
myEntry.grid(row=3, column=0, columnspan=2)
submitbtn.grid(row=4, column=0, columnspan=2)



root.mainloop()
