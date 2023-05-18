#My Solution
from collections import deque

def anagram(s):
    length = len(s)
    if length % 2:
        return -1
    else:
        s1 = deque(s[:length//2])
        s2 = deque(s[length//2:])
        i = 0
        while i < len(s1):
            if s1[i] in s2:
                s2.remove(s1[i])
                s1.remove(s1[i])
            else:
                i+= 1
    return len(s1)

#Other Solution
from collections import Counter

def anagram2(s):
    if len(s)%2 == 1:
        return -1
    else:
        temp = Counter(s[0:len(s)//2]) - Counter(s[len(s)//2:])
    return sum(temp.values())