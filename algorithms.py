import time

def bubble_sort(data, draw_data):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                # colors the two rects being evaluated 'red'
                draw_data(data, ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))])
                time.sleep(0.2)
    # once sorted, recolors entire array 'green'
    draw_data(data, ['green' for _ in range(len(data))])


def selection_sort(data, draw_data):
    pass

def insertion_sort(data, draw_data):
    pass

def merge_sort(data, draw_data):
    pass

def quick_sort(data, draw_data):
    pass