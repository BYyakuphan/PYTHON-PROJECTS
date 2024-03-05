import tkinter as tk

def calculate_factorial():
    number = int(entry.get())
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    result_label.config(text=f"{number}! = {factorial}")

root = tk.Tk()
root.title("Factorial Calculation Program")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

entry_label = tk.Label(input_frame, text="Enter a Number:")
entry_label.pack(side="left")

entry = tk.Entry(input_frame)
entry.pack(side="left")

button = tk.Button(root, text="Calculate", command=calculate_factorial)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()