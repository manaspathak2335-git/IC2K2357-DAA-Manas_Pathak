#Program to implement Bubble Sort

def input_array():
    arr = [int(x) for x in input("Enter array elements separated by spaces: ").split()]
    print(f"Input Array: {arr}\n")
    return arr

arr=input_array()
i=len(arr)
while(i>1):
    swapped=False
    for n in range(0,i-1):
        if arr[n] > arr[n+1]:
            arr[n],arr[n+1]=arr[n+1],arr[n]
            swapped=True
    if not swapped:
        break
    i-=1

print("Sorted List:",Input)
        


