from tkinter import *
from PIL import ImageTk,Image
from tkinter import font as tkFont
import sqlite3
import datetime

def on_select(selected): # defines function for Dropdown Menue(OptionMenu)
    global poop_type
    poop_type = selected

def on_click(): # defines function for button
    global poop_type
    dt = datetime.datetime.now()
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
    print_data=f'{myEntry.get()} : {poop_type} submitted'
    submitLabel = Label(root, text='Data Saved', bg=background_color, fg=font_color, font=large_font)
    submitLabel.grid(row=6, columnspan=2, pady=10)
    print(print_data)
    myEntry.delete(0,'end')

def show_chart():
    chart = Toplevel()
    chart.title('Bristol Stool Chart')
    chartCanvas = Canvas(chart, width=800, height=350, bg=background_color)
    chartCanvas.grid()
    img = ImageTk.PhotoImage(Image.open('chart.png'))
    chart_label = Label(chart, image=img)
    chart_label.image=img
    chart_label.grid(row=0,column=0,columnspan=2)
    chart.mainloop()

# -- variables --
background_color = '#3dd9d9'
font_color = '#fff'
default_font = ('Raleway', 20)
large_font = ('Raleway', 40)

poop_type = 'non selected'

root = Tk()
root.title('Stool-IO')
root.geometry('750x850')
root.configure(bg=background_color)

clicked = StringVar()
clicked.set('Select Poop Type')

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
canvas = Canvas(root, width=750, height=250)
typeLabel = Label(root, bg=background_color, fg=font_color, text='Stool Type: ', font=default_font)
aDropbox = OptionMenu(root, clicked, *pooptypes, command=on_select)
aDropbox.config(font=default_font, fg=font_color, bg=background_color)
commentLabel = Label(root, fg=font_color, bg=background_color,text='Comments:', font=default_font)
myEntry = Entry(root, font=default_font, width=33,)
submitBtn = Button(root, fg=font_color, bg=background_color,text='Submit', command=on_click, font=default_font)
chartBtn = Button(root, text='See Bristol Stool Chart', command=show_chart, font=default_font, fg=font_color, bg=background_color)

# display widgets on screen
canvas.grid(columnspan=2)
logo = ImageTk.PhotoImage(Image.open('logo.png'))
logo_label = Label(image=logo)
logo_label.image=logo
logo_label.grid(row=0,column=0,columnspan=2)
typeLabel.grid(row=1, column=0, pady=10, padx=25, sticky='w')
aDropbox.grid(row=1, column=1)
commentLabel.grid(row=2, column=0, pady=10, padx=25, sticky='w')
myEntry.grid(row=2, column=1, pady=20)
submitBtn.grid(row=4, column=0, columnspan=2, pady=10)
chartBtn.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
