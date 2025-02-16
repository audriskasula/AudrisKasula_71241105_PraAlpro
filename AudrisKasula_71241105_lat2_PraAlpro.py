# LATIHAN 2.1
def bodyMassIndex(berat, tinggi) :
    rumusBmi = berat / (tinggi**2)
    return rumusBmi

berat = int(input("Masukan Berat(KG): "))
tinggi = int(input("Masukan Tinggi(CM): "))
konfersiKeMeter = tinggi / 100 #cm ke m

print(f"Berat: {berat} kg")
print(f"Tinggi: {konfersiKeMeter} m")
print(f"hasil Body Mass Index (BMI): {bodyMassIndex(berat, konfersiKeMeter)}")

# --------------------------------------------------------------------------

# LATIHAN 2.2
def rumusFungsi(x) :
    rumus = 2*x**3 + 2*x + 15/x
    return rumus

print(f"hasil operasi: {rumusFungsi(10)}")

# --------------------------------------------------------------------------

# LATIHAN 2.3
def PerhitunganGajiPengeluaran(gaji, jamKerja):
    total_pendapatan = (jamKerja * gaji) * 5 #minggu
    pajak = total_pendapatan * (14/100)
    gaji_bersih = total_pendapatan - pajak
    baju_aksesoris = gaji_bersih * (10/100)
    alat_tulis = gaji_bersih * (1/100)

    sisa_gaji = gaji_bersih - (baju_aksesoris + alat_tulis)
    
    donasi = sisa_gaji * (25/100)
    untuk_yatim =  donasi * (30/100)
    untuk_dhufa = donasi * (70/100)

    print(f"Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak: Rp.{total_pendapatan}")
    print(f"Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: Rp.{gaji_bersih}")
    print(f"Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp.{baju_aksesoris}")
    print(f"Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp.{alat_tulis}")
    print(f"Jumlah uang yang akan Budi sedekahkan.: Rp.{donasi}")
    print(f"Jumlah uang yang akan diterima anak yatim: Rp.{untuk_yatim}")
    print(f"Jumlah uang yang akan diterima kaum dhuafa: Rp.{untuk_dhufa}")

gajiPerjam = int(input("Gaji per jam yang anda inginkan: Rp."))
jamKerjaPerminggu = int(input("Jumlah jam kerja yang akan dilakukan dalam 1 minggu: "))
PerhitunganGajiPengeluaran(gajiPerjam, jamKerjaPerminggu)