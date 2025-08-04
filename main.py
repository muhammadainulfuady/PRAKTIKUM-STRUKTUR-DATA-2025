# def stack():
#     s = []
#     return s
# def push(s, data):
#     s.append(data)
# def pop(s):
#     data = s.pop()
#     return data
# def peek(s):
#     return s[-1]
# def isEmpty(s):
#     return (s==[])
# def size(s):
#     return(len(s))


gerbang = []
chr = "[()]"
kurung_buka = ["(", "{", "["]
kurung_tutup = [")", "}", "]"]
for char in chr:
    if char in kurung_buka:
        gerbang.append(char)
    elif char in kurung_tutup:
        antri = char
        s = gerbang.pop()
        print(s)
print(gerbang)