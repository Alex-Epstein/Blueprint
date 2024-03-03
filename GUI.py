from tkinter import *
import chatgpt_api_call
import free_fall_sim
import orbit_sim
# import pend_sim
# import projectile_motion_sim

win = Tk()
win.geometry("500x200")

options = [
    "Free fall",
    "Orbit",
    "Pendulum",
    "Projectile motion"
]

clicked = StringVar()
clicked.set("Free fall")
drop = OptionMenu( win, clicked, *options )
drop.pack()

def submit():
    user_in = entry.get() #gets entry text
    print(user_in)
    free_fall_sim.main()
    #chatgpt_api_call.parse(user_in)


# Create an entry widget
entry=Entry(win, width=10, font=('Arial 24', 13))
entry.place(x=50, y=10, width=400, height=150) 

# Create a button
button=Button(win, text="Calculate", command=submit)
button.pack(side = BOTTOM, pady=10)

win.mainloop()