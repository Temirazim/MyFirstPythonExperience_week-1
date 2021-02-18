x = 17391 % 17
l = 546 % 17
e = 934 % 17

if x < l and x < e:
    print("x")
if l < x and l < e:
    print("l")
if e < x or e < l:
    print("e")