a = input()
dc = ""
so = "0123456789"
ds = ""
for i in a:
    if i in so:
        ds += i
    else:
        dc += i
if dc == "":
    print("_")
    print(ds)
elif ds == "":
    print(dc)
    print("_")
else:
    print(dc)
    print(ds)