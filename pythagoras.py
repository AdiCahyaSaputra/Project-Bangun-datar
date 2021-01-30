# Rumus Pythagoras
# a**2 + b**2 = c**2

import math

# 1. Mencari Nilai A
def cariNilaiA() :
    nilaiB = int(input("Masukan Nilai B : "))
    nilaiC = int(input("Masukan Nilai C : "))

    nilaiA = int(math.sqrt((nilaiC**2) - (nilaiB**2)))
    print('Jika Nilai C = {} dan Nilai B = {} maka Nila A = {}'.format(nilaiC, nilaiB, nilaiA))

# 3. Mencari Nilai B
def cariNilaiB() :
    nilaiA = int(input("Masukan Nilai A : "))
    nilaiC = int(input("Masukan Nilai C : "))

    nilaiB = int(math.sqrt((nilaiC**2) - (nilaiA**2)))
    print('Jika Nilai C = {} dan Nilai A = {} maka Nila B = {}'.format(nilaiC, nilaiA, nilaiB))

# 2. Mencari Nilai C
def cariNilaiC() :
    nilaiA = int(input("Masukan Nilai A : "))
    nilaiB = int(input("Masukan Nilai B : "))

    nilaiC = int(math.sqrt((nilaiB**2) - (nilaiA**2)))
    print('Jika Nilai A = {} dan Nilai B = {} maka Nila C = {}'.format(nilaiA, nilaiB, nilaiC))

