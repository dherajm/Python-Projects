import tkinter as tk


def calculate_miles():
    km = float(km_input.get())
    miles = km / 1.609
    miles = round(miles, 2)
    miles_output.config(text=miles)


screen = tk.Tk()
screen.title("km to miles converter")
screen.minsize(width=200, height=100)
screen.config(padx=20, pady=20)

km_input = tk.Entry(width=5)
km_input.grid(row=2, column=3)

miles_output = tk.Label(text="0")
miles_output.grid(row=3, column=3)

km_label = tk.Label(text="km")
km_label.grid(row=2, column=4)

miles_label = tk.Label(text="miles")
miles_label.grid(row=3, column=4)

label1 = tk.Label(text="is equal to")
label1.grid(row=3, column=1)

calculate_button = tk.Button(text="Calculate", command=calculate_miles)
calculate_button.grid(row=4, column=3)

screen.mainloop()
