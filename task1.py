st = input()

nums = st.split()

count_p = 0
count_n = 0

numbers = []

for i in range(len(nums)):
    nums[i] = int(nums[i])
    numbers.append(nums[i])

def is_positive(num: int):
    if num >= 0:
        return True
    else:
        return False

def count_positive(numbers:list, count_p: int):
    for i in range(len(numbers)):
        if is_positive(numbers[i]):
            count_p+=1
    return count_p

def count_negitive(numbers:list, count_p, count_n):
    count_n = len(numbers) - count_p
    print(count_n)

print(count_positive(numbers, count_p))
count_negitive(numbers, count_positive(numbers, count_p), count_n)