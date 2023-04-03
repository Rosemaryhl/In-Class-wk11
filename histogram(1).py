def histogram(word):
    d = dict()
    for char in word:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


a = histogram("south bend")
print(a)
inverse=invert_dict(a)
print(inverse)
