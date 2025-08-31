import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Counter App")

# Initialize the counter variable
counter = 0

# Function to increment the counter and update the label
def increment_counter():
    global counter
    counter += 1
    counter_label.config(text=str(counter))

# Create a label to display the counter value
counter_label = tk.Label(root, text="0", font=("Arial", 48))
counter_label.pack(pady=20)

# Create the increment button
increment_button = tk.Button(root, text="Increment", command=increment_counter, font=("Arial", 24))
increment_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
