import tkinter as tk

root = tk.Tk()

# Define a function that opens a new window and hides the previous one
def open_new_window():
    # Hide the root window
    root.withdraw()
    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.geometry('200x100')
    new_window.title('New Window')
    # Define a function that closes the new window and shows the root window
    def close_new_window():
        new_window.destroy()
        root.deiconify()
    # Create a Button widget that closes the new window and shows the root window when clicked
    button = tk.Button(new_window, text='Close New Window', command=close_new_window)
    button.pack()
    # Set focus to the new window
    new_window.grab_set()

# Create a Button widget that opens a new window when clicked
button = tk.Button(root, text='Open New Window', command=open_new_window)
button.pack()

root.mainloop()
