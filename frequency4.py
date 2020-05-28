def most_frequency(str):
    d = {}
    for n in str:
        keys = d.keys()
        if n in keys:
            d[n] += 1
        else:
            d[n] = 1
    for keys, n in d.items():
        print(keys,"=", n)

io = input("please enter a string")
most_frequency(io)
