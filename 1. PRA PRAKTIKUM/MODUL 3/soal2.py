# Buat fungsi untuk menghasilkan list baru yang berisi karakter-karakter konsonan yang berbeda
# dari suatu string yang terdapat pada parameter, misalkan :
# input atau parameter :’’struktur data’’
# output-return value : [’s’,’t’,’r’,’k’,’d’]
def newList(dt):
    temp = []
    dct = {}
    temp2 = []
    vokal = "aiueoAIUEO"
    for index in dt:
        if index in dct:
            dct[index] += 1
        else:
            dct[index] = 1

    for key in dct:
        val = dct[key]
        if key not in vokal and key != " ":
            temp.append(key)
        else:
            temp2.append(key)
    return temp
dt = "struktur data"
print(f"Input atau parameter : {dt}\noutput-return value : {(newList(dt))}")