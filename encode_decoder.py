from math import ceil
def encrypt(text,key):
    l = len(text)
    num_le = len(str(key))
    new = ''
    while key:
        j = key%10
        for x in range(ceil(l/num_le)):
            try:
                new += text[j+num_le*x+-1]
            except:
                new += ' '
        key //= 10
    return new
    
def decrypt(text,key):
    num_le = len(str(key))
    l ,c,le= [0 for _ in range(num_le)],1,len(text)
    new = ''
    while key:
        l[key%10-1] = c
        c += 1
        key //= 10
    down = le//num_le
    up = ceil(le/num_le)
    for x in range(up):
        for y in l:
            new += text[down*(y-1)+x]
    return new
