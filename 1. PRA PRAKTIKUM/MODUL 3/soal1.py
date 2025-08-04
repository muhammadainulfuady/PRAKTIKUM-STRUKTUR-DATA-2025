def newList(dt):
    temp = []
    dct = {}
    for index in dt:
        if index in dct:
            dct[index] += 1
        else:
            dct[index] = 1
    for key in dct:
        val = dct[key]
        temp.append(key)
    return temp
dt = [1,3,1,1,4,5,7,7,1,5]
print(f"Input atau parameter : {dt}\noutput-return value : {(newList(dt))}")