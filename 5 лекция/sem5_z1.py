# работа на семинаре
# задача про мобильные телефоны/словари
numbers = '+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890'
listNumbers = numbers.split()
d = dict()

for i in listNumbers:
    # if i[:2] not in d:
    #     d[i[:2]] = [i]
    # else:
    #     d[i[:2]] += [i]
    d[i[:2]] = d.get(i[:2],[]) + [i]



print(*sorted(d.items()))
