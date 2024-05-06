def insertion_sort(arr,mode):
    process = f"Process: \n{arr}\n"
    if mode == "Ascending":
        for i in range(1, len(arr)):
            for iterate in range(0,i):
                if arr[iterate] > arr[i]:
                    arr[iterate], arr[i] = arr[i], arr[iterate]
            process += f"{arr} \n"
    else: 
        for i in range(1, len(arr)):
            for iterate in range(0,i):
                if arr[iterate] < arr[i]:
                    arr[iterate], arr[i] = arr[i], arr[iterate]
            process += f"{arr} \n"
    return arr , process

if __name__ == "__main__":
    array = [82,28,13,21,81]
    array , process = insertion_sort(array,"Descending")
    print(f"sorted array: {array}")
    print(process)