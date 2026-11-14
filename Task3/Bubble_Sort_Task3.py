Input=[8,3,15,6,2]

i=len(Input)
while(i>1):
    swapped=False
    for n in range(0,i-1):
        if Input[n] > Input[n+1]:
            Input[n],Input[n+1]=Input[n+1],Input[n]
            swapped=True
    if not swapped:
        break
    i-=1

print("Sorted List:",Input)
        


