from tkinter import *
import chatgpt_api_call

win = Tk()
win.geometry("500x200")

def submit():
    user_in = entry.get() #gets entry text
    chatgpt_api_call.parse(user_in)


# Create an entry widget
entry=Entry(win, width=10, font=('Arial 24', 13))
entry.place(x=50, y=10, width=400, height=150) 

# Create a button
button=Button(win, text="Calculate", command=submit)
button.pack(side = BOTTOM, pady=10)

win.mainloop()