num=(input()).split()


def is_zero_num(numb):
    if int(numb) == 0:
        return True
    else:
        return False

def count_zeros(num):
    count = 0
    for _ in num:
        if is_zero_num(_):
            count+=1
    return count
def count_non_zeros(num):
    count_zer=0
    for _ in num:
        if not is_zero_num(_):
            count_zer+=1
    return count_zer

print(count_zeros(num))
print(count_non_zeros(num))
