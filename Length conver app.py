import tkinter as tk

INCH_TO_CM = 2.50
def convert():
    """Calculates and display the conversion."""
    try:
        inches = float(entry_inches.get())
        cm = inches * INCH_TO_CM
        label_result.config(text=f"{cm:.2f} cm")
    except ValueError:
        label_result.config(text="Invalid Input")

root = tk.Tk()
root.title("Inches to CM")
entry_inches = tk.Entry(root)
entry_inches.pack(pady=10)
button_convert = tk.Button(root, text="Convet", command=convert)
button_convert.pack(pady=5)
label_result = tk.Label(root, text="Enter inches")
label_result.pack(pady=10)

root.mainloop()