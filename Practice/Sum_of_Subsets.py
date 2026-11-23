#Program to find number of subsets of given set having sum of elements equal to T 

def Sum_of_Subsets(i, Input, Remain_sum, Target, Subset=[]): #takes element index, Input list, sum of unprocessed elements, target sum, and current subset
    if sum(Subset) == Target: #checks if current_sum equals target, if yes prints subset
        print(Subset)
        return

    if i == len(Input): #returns at end of list
        return

    if sum(Subset) > Target: #returns when current_sum > Target
        return

    if sum(Subset) + Remain_sum < Target: #returns if Target couldn't be achieved
        return

    Remain_sum = Remain_sum - Input[i] #subtracts element from remaining sum

    #Excluding i
    Sum_of_Subsets(i+1, Input, Remain_sum, Target, Subset)

    #Including i
    Subset.append(Input[i])
    Sum_of_Subsets(i+1, Input, Remain_sum, Target, Subset)
    Subset.pop()

I=[5,10,12,13,15,18]
T=30
Sum_of_Subsets(0,I,sum(I),T)
