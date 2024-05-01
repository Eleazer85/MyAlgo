def bubble_sort(array,order):
    array_index = len(array) - 1
    sorted = False 
    process = "Process:\n"
    if order == "Ascending":
        while not sorted:
            sorted = True
            for i in range(0,array_index):
                process += f"{array}\n"
                if array[i] > array[i+1]:
                    sorted = False
                    array[i], array[i+1] = array[i+1], array[i]
    else:
        while not sorted:
            sorted = True
            for i in range(0,array_index):
                process += f"{array}\n"
                if array[i] < array[i+1]:
                    sorted = False
                    array[i], array[i+1] = array[i+1], array[i]
    return array , process