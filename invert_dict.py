def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

d={"a":1,"p":1,"r":2,"t":1,"0":1}
print(invert_dict(d))
