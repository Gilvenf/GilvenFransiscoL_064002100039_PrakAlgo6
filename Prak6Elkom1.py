print("MENGHITUNG JARAK TEMPUH GLBB")
kecepatan_awal=int(input("Masukkan Angka V0:"))
waktu=int(input("Masukkan Angka T:"))
percepatan=int(input("Masukkan Angka A:"))
def jarak_tempuh (kecepatan_awal, waktu, percepatan):
    jarak_tempuh=kecepatan_awal*waktu+1/2*percepatan*(waktu**2)
    print("jarak tempuh kecepatan awal =",kecepatan_awal, "waktu =",waktu, "dan", "percepatan=",percepatan, "adalah",jarak_tempuh)
jarak_tempuh(kecepatan_awal,waktu,percepatan)

