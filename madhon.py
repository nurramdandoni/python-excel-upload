arr_nilai = [11,5,3,11,3,8]
arr_tgl   = [1,2,3,4,5,6]



temp = {}
final_index = []
final_value = []
for key,initial in enumerate(arr_tgl):
    temp[initial] = arr_nilai[key]

for key3, initial3 in enumerate(arr_tgl):
    if (arr_nilai.count(arr_nilai[key3]) < 2):
        final_index.append(key3)
    else:
        indeks_nilai_max = max([i for i, nilai in enumerate(arr_nilai) if nilai == arr_nilai[key3]])
        if(key3 < indeks_nilai_max ):
            final_index.append(indeks_nilai_max)


list_valid = sorted(set(final_index))
for keys, init in enumerate(list_valid):
    if(arr_nilai.count(arr_nilai[init]) < 2):
        final_value.append(arr_nilai[init])
    else:
        for val in range(arr_nilai.count(arr_nilai[init])):
            final_value.append(arr_nilai[init])
print(final_value)