def stack():
    s = []
    return s
def push(s, data):
    s.append(data)
def pop(s):
    data = s.pop()
    return data
def peek(s):
    return s[-1]
def isEmpty(s):
    return (s==[])
def size(s):
    return(len(s))

# char = "([]{](]}"
char = "([][](])"
kurung_buka = ["(", "[", "{"]
kurung_tutup = [")", "]", "}"]
temp = stack()
flag = {
  ")":"(",
  "}":"{",
  "]":"["
}
eror = []

for ch in char:
    # jika kurung buka maka saya masukkan ke dalam temp
    if ch in kurung_buka:
        save_push = push(temp, ch)

    elif ch in kurung_tutup:
        if not isEmpty(temp):
            end_temp = peek(temp)
            print(end_temp, "end    ")
            if end_temp == flag[ch]:
                pop(temp)
                print(f"{flag[ch]} cocok dengan {ch}")
            elif end_temp != flag[ch]:
                pop(temp)
                print(f"{end_temp} tidak cocok dengan {ch}")
        elif isEmpty(temp):
            eror.append(ch)
            print(eror)