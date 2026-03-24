hackers = [1, 5 ,10]
security_level = 3
incriense = 1

def hackers_func(hackers: list, security_level: int, incriense: int):
    if hackers == []:
        return 0
    else:
        count=0
        for c in hackers:
            if int(c) < security_level:
                security_level+=incriense
            else:
                count+=1
        return count

print(hackers_func(hackers, security_level, incriense))
