import sqlite3
from tkinter import *
from PIL import ImageTk,Image
import datetime
from tkinter import font as tkFont

root = Tk()
root.title('Stool-IO')
#root.geometry('800x800')
root.configure(bg='#3dd9d9')


clicked = StringVar()
clicked.set('Select Poop Type')

poop_type = 'non selected'

#create sqlite3 database:
"""conn = sqlite3.connect('stool_log.db')
c = conn.cursor()
c.execute('''CREATE Table logs (
        date text,
        time text,
        type text,
        comment text
        )''')
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
    print_data=f'{poop_type} : {myEntry.get()} submitted'
    submitLabel = Label(root, text="Data Loged", font="Raleway")
    submitLabel.grid(row=5, columnspan=2, pady=10)
    print(print_data)
    myEntry.delete(0,'end')
    #messagebox.showinfo('showinfo','submitted')
    #root.messagebox.showinfo(title="Success",message="Successfully logged input")

# -- variables --
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

default_font = ('Raleway', 20)
#large_font = (family='Ariel', size=40)

# lay out/ initialize widgets for main window below
canvas = Canvas(root, width = 800, height = 390)
typeLabel = Label(root, text='Stool Type: ', font="default_font")
aDropbox = OptionMenu(root, clicked, *pooptypes, command=on_select)
aDropbox.config(font='Raleway')
commentLabel = Label(root, text='Comments:', font="Raleway")
myEntry = Entry(root, font="Raleway", width=70,)
submitBtn = Button(root, text='Submit', command=on_click, font="Raleway")
#chartBtn = Button(root, text='See Log', command=see_chart, font="default_font")

# display widgets on screen
canvas.grid(columnspan=2)
logo = ImageTk.PhotoImage(Image.open('logo.png'))
logo_label = Label(image=logo)
logo_label.image=logo
logo_label.grid(row=0,column=0,columnspan=2)
typeLabel.grid(row=1, column=0)
aDropbox.grid(row=1, column=1)
commentLabel.grid(row=2, column=0)
myEntry.grid(row=2, column=1, pady=20)
submitBtn.grid(row=4, column=0, columnspan=2)
#chartbrn.grid(row=5, cloumn=0, columnspan=2)

root.mainloop()
