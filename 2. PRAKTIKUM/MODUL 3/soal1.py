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

def DesimalToBiner(number):
    temp_push = stack()
    temp_pop = stack()
    mengetahui = number
    iterasi = 1
    while number != 0:
        sisa = number % 2
        div = number // 2
        number = div
        push(temp_push, sisa)
        print(f"{iterasi}. Push stack with {sisa} --> {temp_push}")
        iterasi += 1

    print("")
    while not isEmpty(temp_push):
       delete_pop = pop(temp_push)
       push(temp_pop, delete_pop)
       print(f"{iterasi}. Pop stack with {delete_pop} --> {temp_push}")
       iterasi += 1

    print("")
    print(f"Biner {mengetahui} = {temp_pop}")
    return temp_push
DesimalToBiner(57)