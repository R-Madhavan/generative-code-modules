from tkinter import *
from tkinter import ttk
# Conversion factors dictionary
conversion_factors = {
    ("Miles", "Kilometers"): 1.60934,
    ("Miles", "Meters"): 1609.34,
    ("Miles", "Feet"): 5280,
    ("Miles", "Inches"): 63360,
    ("Kilometers", "Miles"): 0.621371,
    ("Kilometers", "Meters"): 1000,
    ("Kilometers", "Feet"): 3280.84,
    ("Kilometers", "Inches"): 39370.1,
    ("Meters", "Miles"): 0.000621371,
    ("Meters", "Kilometers"): 0.001,
    ("Meters", "Feet"): 3.28084,
    ("Meters", "Inches"): 39.3701,
    ("Feet", "Miles"): 0.000189394,
    ("Feet", "Kilometers"): 0.0003048,
    ("Feet", "Meters"): 0.3048,
    ("Feet", "Inches"): 12,
    ("Inches", "Miles"): 1 / 63360,
    ("Inches", "Kilometers"): 1 / 39370.1,
    ("Inches", "Meters"): 1 / 39.3701,
    ("Inches", "Feet"): 1 / 12
}

def convert():
    """Convert from one unit to another and display the result."""
    try:
        amount = float(input_box.get())
        from_unit = from_unit_combo.get()
        to_unit = to_unit_combo.get()
        if from_unit == to_unit:
            result_label.config(text=f"{amount} {to_unit}")
        else:
            factor = conversion_factors.get((from_unit, to_unit))
            if factor:
                result = round(amount * factor, 4)
                result_label.config(text=f"{result} {to_unit}")
            else:
                result_label.config(text="Conversion not supported.")
    except ValueError:
        result_label.config(text="Invalid input")

def reset():
    """Clear the input and reset the result."""
    input_box.delete(0, END)
    result_label.config(text="0")

# Set up main window
window = Tk()
window.title("Advanced Unit Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20, bg="#f5f5f5")

# Title Label
title_label = Label(window, text="Advanced Unit Converter", font=("Arial", 16, "bold"), bg="#f5f5f5")
title_label.grid(column=0, row=0, columnspan=3, pady=(0, 10))

# Input Box
input_box = Entry(window, width=10, font=("Arial", 12))
input_box.grid(column=1, row=1)
input_box.insert(END, "0")

# From and To Unit Selectors
from_unit_combo = ttk.Combobox(window, values=["Miles", "Kilometers", "Meters", "Feet", "Inches"], state="readonly", width=10, font=("Arial", 10))
from_unit_combo.grid(column=0, row=1)
from_unit_combo.set("Miles")

to_unit_combo = ttk.Combobox(window, values=["Miles", "Kilometers", "Meters", "Feet", "Inches"], state="readonly", width=10, font=("Arial", 10))
to_unit_combo.grid(column=2, row=1)
to_unit_combo.set("Kilometers")

# "is equal to" Label
equal_label = Label(window, text="is equal to", font=("Arial", 12), bg="#f5f5f5")
equal_label.grid(column=0, row=2)

# Result Label
result_label = Label(window, text="0", font=("Arial", 12, "bold"), bg="#f5f5f5", fg="#4a90e2")
result_label.grid(column=1, row=2, pady=10)

# Buttons
convert_button = Button(window, text="Convert", command=convert, font=("Arial", 10), bg="#4a90e2", fg="white")
convert_button.grid(column=1, row=3, pady=(5, 0))

reset_button = Button(window, text="Reset", command=reset, font=("Arial", 10), bg="#d9534f", fg="white")
reset_button.grid(column=2, row=3, pady=(5, 0))

# Run the application(appliation will be open till close)
window.mainloop()
