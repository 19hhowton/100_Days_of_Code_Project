import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

## Label 
""" When I click the button, the text should be "Button got clicked'"""
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side = "left")

# my_label["text"] = "New Text"
# my_label.config(text="New Text")

## Button
def button_clicked():
    my_label.config(text="Button got clicked")
    # print("I got clicked")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

## Entry
input = tkinter.Entry(width=10)
input.pack()
print(input.get())

## Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

## Checkbox
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

## Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

## RadioButton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

## Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

window.mainloop()