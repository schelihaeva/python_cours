# находим поллиндром
str_1 = "1233214"

def polindrom(s: str):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return polindrom(s[1:-1])

print(polindrom(str_1))