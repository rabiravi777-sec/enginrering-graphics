import tkinter as tk

root = tk.Tk()
root.title("Basic Geometric Primitives")
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# 1. Line
canvas.create_line(50, 50, 200, 50, fill="red", width=5)

# 2. Circle
canvas.create_oval(250, 20, 350, 120, fill="blue", outline="black")

# 3. Rectangle
canvas.create_rectangle(400, 20, 550, 120, fill="green", outline="black")

# 4. Ellipse
canvas.create_oval(600, 20, 750, 120, fill="orange", outline="black")

# 5. Polygon
canvas.create_polygon(
    100, 200,
    200, 150,
    300, 200,
    250, 300,
    150, 300,
    fill="purple",
    outline="black"
)

# 6. Triangle
canvas.create_polygon(
    450, 300,
    550, 150,
    650, 300,
    fill="yellow",
    outline="black"
)

root.mainloop()
