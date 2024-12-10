from tkinter import Tk, Button, Label

def toggle_widget():
    if widget.winfo_viewable():
        widget.pack_forget()
        toggle_button.config(text="Show Widget")
    else:
        widget.pack()
        toggle_button.config(text="Hide Widget")

root = Tk()

widget = Label(root, text="Hello, World!")
widget.pack()

toggle_button = Button(root, text="Hide Widget", command=toggle_widget)
toggle_button.pack()

root.mainloop()
