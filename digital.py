import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Define the function to update the time
def time():
    string = strftime('%H:%M:%S %p \n %D')  # Corrected the time format
    label.config(text=string)
    label.after(1000, time)  # Call the function every 1000ms (1 second)

# Create the label to display the time
label = tk.Label(root, font=('calibri', 50, 'bold'), background='white', foreground='black')

# Pack the label into the window and center it
label.pack(anchor='center')

# Call the time function
time()

# Start the Tkinter event loop
root.mainloop()
