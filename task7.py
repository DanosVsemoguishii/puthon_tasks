st = (input()).split(",")

def is_correct(st):
    count = 0
    for i in range(len(st) - 1):
        if int(st[i]) + 1 == int(st[i+1]):
            count+=1
    if count == 2:
        print(count)
        return True
    else:
        print(count)
        return False

def summ(st):
    summm = 0
    if is_correct(st):
        for c in st:
            summm+=int(c)
            return summm
    else:
        return "Validate is poshel nafig"


print(summ(st))


