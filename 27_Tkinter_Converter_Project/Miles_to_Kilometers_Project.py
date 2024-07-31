import tkinter

FONT = ("Arial", 10)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=30)
window.config(padx=15, pady=15)


def calculate_miles_to_km():
    miles = input.get()
    kilometer = float(miles) * 1.60934
    label_3.config(text = kilometer)

## Entry
input = tkinter.Entry(width=10)
input.place(x=70, y=10)

# Label
label_1 = tkinter.Label(text="Miles", font=FONT)
label_1.place(x=120, y=10)

## Label
label_2 = tkinter.Label(text="is equal to", font=FONT)
label_2.place(x=0, y=40)

## Label
label_3 = tkinter.Label(text="0", font=FONT)
label_3.place(x=70, y=40)

## Label
label_4 = tkinter.Label(text="Km", font=FONT)
label_4.place(x=120, y=40)

## Button
button = tkinter.Button(text="Calculate", command=calculate_miles_to_km)
button.place(x=70, y=70)




window.mainloop()