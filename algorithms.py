import time

# bubble sort repeatedly swaps adjacent elements if they are not in order
def bubble_sort(data, draw_data):
    for i in range(len(data)):
        for j in range(len(data)- i -1):
            if data[j] > data[j+1]:
                # swap the two elements
                data[j], data[j+1] = data[j+1], data[j]
                # colors the two rects being evaluated 'red'
                draw_data(data, ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))])
                time.sleep(0.1)
    # once sorted, recolors entire array 'green'
    draw_data(data, ['green' for _ in range(len(data))])


# Selection sort finds minimum element from unsorted part of array and puts at the start.
# Uses two subarrays (sorted and unsorted)
def selection_sort(data, draw_data):
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            # colors the two rects being evaluated 'red'
            draw_data(data, ['red' if x == min_index or x == j else 'blue' for x in range(len(data))])
            time.sleep(0.1)
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    draw_data(data, ['green' for _ in range(len(data))])

def insertion_sort(data, draw_data):
    pass

def merge_sort(data, draw_data):
    pass

def quick_sort(data, draw_data):
    pass