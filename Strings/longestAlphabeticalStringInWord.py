
def longestAlphabetical(s):
    count = 0
    m = 0
    for k in range(len(s)):
        count += 1
        for i in range(len('abcdefghijklmnopqrstuvwxyz')):
            while s[k % len(s)] == 'abcdefghijklmnopqrstuvwxyz'[i % 26]:
                k = k + 1
        if k-count+1 > m:
            m = (k-count+1)
            d = (s[count-1:k])
    return('Longest substring in alphabetical order is: ',d)