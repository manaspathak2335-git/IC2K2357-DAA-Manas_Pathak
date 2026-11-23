#Program to find smallest substring in s containing all characters of t using sliding window technique

from collections import Counter

def substring_exists(win,t):
    
    count_win = Counter(win)
    count_t = Counter(t)
    for ch,req in count_t.items():
        if count_win[ch] < req:
            return False
    return True

def Smallest_SubStr(s,t):

    if not s or not t:
        return ""
    
    left=0
    right=0
    window=s[0]
    smallest_sub=str()

    while right < len(s):
        
        if not substring_exists(window,t):
            right+=1
            window = s[left:right+1]

        if substring_exists(window,t):
            
            if len(window)<len(smallest_sub) or len(smallest_sub) == 0:
                smallest_sub = window
                
            left+=1
            window = s[left:right+1]

    return smallest_sub

s="ADOBECODEBANC"
t="ABC"
o=Smallest_SubStr(s,t)
print(f"Input: s = {s}, t = {t}, Output = {o}")
        
                
