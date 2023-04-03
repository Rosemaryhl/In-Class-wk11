def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()
h={"pie":3,"pie":7,"goldfish":4,"cookie":6}
print(reverse_lookup(h,7))
