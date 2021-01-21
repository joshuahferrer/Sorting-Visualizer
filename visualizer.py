# A simple python script using Tkinter to visualize sorting algorithms.
# Purpose of project is to review algorithms as well as practice GUI programming
# 9/9/2020


import tkinter as tk
from tkinter import ttk
import algorithms
import random


def run_algorithm():
    global data
    print("Algorithm selected: " + algVar.get())
    if algVar.get() == "Bubble Sort":
        algorithms.bubble_sort(data, draw_data)
    elif algVar.get() == "Selection Sort":
        algorithms.selection_sort(data, draw_data)

def change_algorithm(*args):
    print(algVar.get())

def random_array():
    global data
    # reset data array
    data = []
    # get random set of integers
    for _ in range(25):
        data.append(random.randrange(0, 101))
    draw_data(data,['blue' for _ in range(len(data))])  # will color rects 'blue'

def draw_data(data, colorArray):
    # clears the canvas and draws the new set of integers
    canvas.delete('all')
    canv_height = 380
    canv_width = 600
    # bars
    x_width = canv_width / (len(data) + 1)
    offset = 10
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = canv_height - height * 340
        # bottom left
        x1 = (i + 1) * x_width + offset
        y1 = canv_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    root.update_idletasks()

# ------------------ END OF FUNCTIONS ------------------------------------------


# create root widget
root = tk.Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
#root.config(bg='black')

# frame / canvas
mainFrame =tk.Frame(root, width = 600, height = 200)
mainFrame.grid(row=0, column=0, padx=10, pady=5)

canvas = tk.Canvas(root, width = 600, height = 380)
canvas.grid(row=1, column=0, padx=10, pady=5)

# Variables
algVar = tk.StringVar()
data = []

# Dictionary with algorithm options
CHOICES = [
    "Bubble Sort",
    "Selection Sort",
    "Quick Sort",
    "Heap Sort"
] 
algVar.set("Choose Algorithm") # set the default value


# ----------------------- UI ---------------------------------------------------

# OptionMenu to choose algorithm
choose_algorithm = tk.OptionMenu(mainFrame, algVar, *CHOICES)
choose_algorithm.grid(row=0, column=1, padx=5, pady=5)

# Get random array of integers
generate_array = tk.Button(mainFrame, text='Generate array', command=random_array)
generate_array.grid(row=0, column = 3, padx=5, pady=5)

# Run sorting algorithm
run_algorithm = tk.Button(mainFrame, text="Sort", command=run_algorithm, bg='red')
run_algorithm.grid(row=1, column=2, padx=5, pady=5)



# tkinter event loop
root.mainloop()
