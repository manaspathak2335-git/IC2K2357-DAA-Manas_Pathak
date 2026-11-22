#Program to find longest substring with k distinct characters from a given string

def isunique(string):
    s=set(string)
    return len(s)

def Longest_SubStr(s,k):
    if not s:
        return
    
    left=0
    window=s[0]
    maxLen=0
    
    for right in range(len(s)):
        
        while isunique(window)>k:
            window = window[1:]
            left+=1

        maxLen = max(maxLen, len(window))

        if right < len(s)-1:
            window = s[left:right+2]

    return maxLen

s="araaci"
k=2
o=Longest_SubStr(s,k)
print(f"Input: s = {s}, k = {k} Output:{o}") 
