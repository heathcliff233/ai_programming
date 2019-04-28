def move_substr(s, flag, n):
    length = len(s)
    if (n==0 or n>=length):
        ri = 'the n is too large'
        return ri
    elif (flag == 1):
        out = n
        s1 = s[:out]
        s2 = s[out:]
        s = s2 + s1
        return s
    else:
        out = n
        s2 = s[-out:]
        s1 = s[:length-out]
        s = s2 + s1
        return s
if __name__ == '__main__':
    strr = input()
    lst = strr.split(',')
    a = move_substr(lst[0], int(lst[1]), int(lst[2]))
    print(a)