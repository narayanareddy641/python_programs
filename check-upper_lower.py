def low_up(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1

    print("original string ", s)
    print("no of upper case ", d["upper"])
    print("no of lowercase ", d["lower"])
