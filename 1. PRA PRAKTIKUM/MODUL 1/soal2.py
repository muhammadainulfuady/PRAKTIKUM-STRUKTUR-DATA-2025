# Buat fungsi add list(a, b), yaitu fungsi untuk menambahkan dua buah list yaitu a dan b, dimana ukuran
# dari dua buah list tersebut haruslah sama

def addList(a, b):
    temp = []
    flag = False
    if len(a) == len(b):
        for index in range(len(a)):
            result = a[index] + b[index]
            temp.append(result)
            flag = True
    if flag == True:
        print(f"{a}\n{b}\n\n{temp}")
    else:
        print("panjang tidak sama")
    return temp
a = [1, 2, 3, 9]
b = [1, 2, 4]
addList(a, b)