# Buat fungsi create list(n), yaitu fungsi untuk menghasilkan suatu list, dimana n adalah banyaknya anggota dalam list, dan anggota list merupakan inputa dari user
def createList(n):
    temp = []
    iterasi = 0
    while iterasi < n:
        input_users = int(input(f"Masukkan angka list ke-{iterasi+1} : "))
        temp.append(input_users)
        iterasi += 1
    return temp
n = int(input("Masukkan banyak data : "))
print(createList(n))