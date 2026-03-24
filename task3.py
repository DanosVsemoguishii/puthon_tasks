st = input().split(", ")

def topa(st: list):
    count = 0
    if len(st) == 4:
        print(len(st))
        print(len(st) - 1)
        for i in range(len(st) - 1):
            if int(st[i])+1 == st[i+1]:
                count+=1
                print(count)
    if count + 1 == 4:
        print(int(st[0]) * int(st[1]) * int(st[2]) * int(st[3]) + 1)
    else:
        print("error")

topa(st)
