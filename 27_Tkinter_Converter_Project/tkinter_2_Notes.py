import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

## Label
label = tkinter.Label(text="This is a Label", font=("Arial", 14, "bold"))
label.grid(column=0, row=0)

## Button
button = tkinter.Button(text="Button #1")
button.grid(column=3, row=11)

## New Button
new_button = tkinter.Button(text="Button #2")
new_button.grid(column=0, row=3)

## Entry
input = tkinter.Entry(width=10)
input.grid(column=6, row=6)
# print(input.get())

window.mainloop()