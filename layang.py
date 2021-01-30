# Rumus Layang layang

# Luas 
# 1/2 * (diagonalSatu * diagonalDua)
# d1 = garis horizontal (kiri ke kanan)
# d2 = garis vertikal (atas ke bawah)
def luasLayangLayang() :
    diagonalSatu = int(input('Masukan Nilai d1 : '))
    diagonalDua = int(input('Masukan Nilai d2 : '))

    hasil = 1/2 * (diagonalSatu * diagonalDua)
    print(f'Luas Layang Layang Adalah {hasil}')

# Mencari keliling layang layang
def kelilingLayangLayang() :
    sisiSatu = int(input('Masukan Nilai sisi1 : '))
    sisiDua = int(input('Masukan Nilai sisi2 : '))

    hasil = 2 * (sisiSatu + sisiDua)
    print(f'keliling layang layang = {hasil}')
