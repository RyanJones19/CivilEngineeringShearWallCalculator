import tkinter as tk

def draw_room(length, width, num_horizontal_walls, num_vertical_walls):
    # Clear canvas before redrawing
    canvas.delete("all")

    # Draw the outer rectangle
    canvas.create_rectangle(10, 10, 10 + length, 10 + width, outline="black", fill="green")

    # Calculate the spacing for internal walls
    horizontal_spacing = width / (num_horizontal_walls + 1)
    vertical_spacing = length / (num_vertical_walls + 1)

    # Draw internal horizontal walls
    for i in range(1, num_horizontal_walls + 1):
        y = 10 + i * horizontal_spacing
        canvas.create_line(10, y, 10 + length, y, fill="black")

    # Draw internal vertical walls
    for i in range(1, num_vertical_walls + 1):
        x = 10 + i * vertical_spacing
        canvas.create_line(x, 10, x, 10 + width, fill="yellow")

def get_dimensions():
    length = entry_length.get()
    width = entry_width.get()
    num_horizontal_walls = entry_horizontal_walls.get()
    num_vertical_walls = entry_vertical_walls.get()

    try:
        length = float(length)
        width = float(width)
        num_horizontal_walls = int(num_horizontal_walls)
        num_vertical_walls = int(num_vertical_walls)

        draw_room(length, width, num_horizontal_walls, num_vertical_walls)
    except ValueError:
        result_label.config(text="Please enter valid numeric values for dimensions and wall counts.")

# Create the main window
root = tk.Tk()
root.title("Shear Load Calculator")

# Create labels and entry widgets for length, width, and wall counts
label_length = tk.Label(root, text="Length:")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

label_width = tk.Label(root, text="Width:")
label_width.grid(row=1, column=0, padx=10, pady=10)

entry_width = tk.Entry(root)
entry_width.grid(row=1, column=1, padx=10, pady=10)

label_horizontal_walls = tk.Label(root, text="Number of Horizontal Walls:")
label_horizontal_walls.grid(row=2, column=0, padx=10, pady=10)

entry_horizontal_walls = tk.Entry(root)
entry_horizontal_walls.grid(row=2, column=1, padx=10, pady=10)

label_vertical_walls = tk.Label(root, text="Number of Vertical Walls:")
label_vertical_walls.grid(row=3, column=0, padx=10, pady=10)

entry_vertical_walls = tk.Entry(root)
entry_vertical_walls.grid(row=3, column=1, padx=10, pady=10)

# Create a button to draw the room
draw_button = tk.Button(root, text="Draw Room", command=get_dimensions)
draw_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create a label for displaying error messages
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

# Create a canvas for drawing
canvas = tk.Canvas(root, width=800, height=800)
canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()

