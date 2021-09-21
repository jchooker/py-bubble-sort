#simple bubble swap

arr = [11,2,0,-4,5,22]

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                print(f"swapping {arr[i]} and {arr[i+1]}")
                arr[j],arr[j+1] = arr[j+1],arr[j]
            else:
                print("no swap needed")
    print(arr)
    return arr

bubbleSort(arr)