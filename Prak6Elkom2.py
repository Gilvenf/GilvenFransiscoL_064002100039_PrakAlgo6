print("KALKULATOR LUAS PERMUKAAN BANGUN RUANG")
print("1.Kubus")
print("2.Balok")
print("3.Tabung")
print("4.Kerucut")
print("5.Bola")
print("6.Keluar")
phi=3.14
pilih =int(input('pilih:'))
def kubus():
    kubus=6*sisi**2
    print("Luas Permukaan Bangun Ruang Kubus Adalah: ",kubus)
def balok():
    balok=2*(p*l+p*t+l*t)
    print("Luas Permukaan Bangun Ruang Balok Adalah: ",balok)
def tabung():
    tabung=2*phi*r*(r+t) 
    print("Luas Permukaan Bangun Ruang Tabung Adalah: ",tabung)
def kerucut():
    kerucut=phi*r*(r+s)
    print("Luas Permukaan Bangun Ruang Kerucut Adalah: ",kerucut)
def bola():
    bola=4*phi*r**2
    print("Luas Permukaan Bangun Ruang Bola Adalah: ",bola)


if pilih == 1 :
     sisi = int(input("Masukkan Sisi: "))
     kubus()
elif pilih == 2:
    p = int(input("Masukkan Panjang: "))
    l = int(input("Masukkan Lebar: "))
    t = int(input("Masukkan Tinggi: "))
    balok()
elif pilih == 3:
    r= int(input("Masukkan R:"))
    t= int(input("Masukkan T:"))
    tabung()
elif pilih == 4:
    r = int(input("Masukkan R:"))
    s = int(input("Masukkan S:"))
    kerucut()
elif pilih == 5:
    r= int(input("Masukkan R:"))
    bola()
elif pilih ==6:
    print("Byebye")
else:
    print("INPUT SALAH ")