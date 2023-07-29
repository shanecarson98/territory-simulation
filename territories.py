import tkinter as tk
from PIL import Image, ImageTk
import random

def create_moving_images(canvas, rows, columns):
    grid_width = canvas.winfo_width()
    grid_height = canvas.winfo_height()
    cell_width = grid_width // columns
    cell_height = grid_height // rows

    images = []
    for row in range(rows):
        row_images = []
        for col in range(columns):
            color = f"#{random.randint(0, 0xFFFFFF):06x}"
            image = canvas.create_rectangle(col * cell_width, row * cell_height, (col + 1) * cell_width, (row + 1) * cell_height, fill=color)
            row_images.append(image)
        images.append(row_images)

    # Move the images randomly
    move_images(canvas, images, cell_width, cell_height)

def move_images(canvas, images, cell_width, cell_height):
    while True:
        for row_images in images:
            for image in row_images:
                x1, y1, x2, y2 = canvas.coords(image)
                dx = random.randint(-5, 5)
                dy = random.randint(-5, 5)

                if 0 <= x1 + dx < canvas.winfo_width() - cell_width:
                    x1 += dx
                    x2 += dx
                if 0 <= y1 + dy < canvas.winfo_height() - cell_height:
                    y1 += dy
                    y2 += dy

                canvas.coords(image, x1, y1, x2, y2)

        canvas.update()
        canvas.after(100)  # Update every 100 milliseconds

def main():
    root = tk.Tk()
    root.title("Moving Images Grid")

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack(fill=tk.BOTH, expand=True)

    rows = 10
    columns = 10

    create_moving_images(canvas, rows, columns)

    root.mainloop()


if __name__ == "__main__":
    main()

