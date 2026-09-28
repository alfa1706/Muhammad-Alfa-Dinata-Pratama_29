#kasus satu: sistem pendataan mahasiswa
class mahasiswa:
    def __init__(self, nama, nim, prodi, nilai):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.nilai = nilai

    def __cek__status(self):
        if self.nilai >= 75:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __tampilkan(self) -> None:
        print ("Nama:", self.nama)
        print ("NIM:", self.nim)
        print ("Jurusan:", self.prodi)
        print ("Nilai:", self.nilai)
        print ("Keterangan:", self.__cek__status())

mahasiswa1 = mahasiswa("Doni", 4566, "Teknik Informatika", 65)
mahasiswa2 = mahasiswa("Rara", 4567, "Pendidikan Agama Islam", 75)
mahasiswa3 = mahasiswa("Intan", 4568, "Teknik Mesin", 90)

print("===MAHASISWA===")
mahasiswa1._mahasiswa__tampilkan()
mahasiswa2._mahasiswa__tampilkan()
mahasiswa3._mahasiswa__tampilkan()

#Kasus dua: Sistem Rental Kendaraan
class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

class mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.kursi = jumlah_kursi

    def tampilkan(self):
        print("Nama Kendaraan:", self.nama)
        print("Merk:", self.merk)
        print("Keluar Tahun:", self.tahun)
        print("Kecepatan Maks:", self.kecepatan, "km/h")
        print("Ada Berapa Kursi:", self.kursi, "kursi")

class motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe = tipe_motor

    def tampilkan(self):
        print("Nama Kendaraan:", self.nama)
        print("Merk:", self.merk)
        print("Keluar Tahun:", self.tahun)
        print("Kecepatan Maks:", self.kecepatan, "km/h")
        print("Tipe:", self.tipe)

Mobil = mobil ("Brio", "Honda", 2012, 145, 5)
Motor = motor ("Aerox 155", "Yamaha", 2016, 148, "Sporty Scooter")

print("===KENDARAAN===")
Mobil.tampilkan()
Motor.tampilkan()

#Kasus tiga: Sistem manajemen pegawai
class ID_Pegawai:
    def __init__(self, identitas_pegawai, nama):
        self.id_pegawai = identitas_pegawai
        self.nama_pegawai = nama

class Gaji:
    def __init__(self, gaji):
        self.gaji = gaji

class Nama_proyek:
    def __init__(self, namaproyek):
        self.proyek = namaproyek

class Project_Manager(ID_Pegawai, Gaji, Nama_proyek):
    def __init__(self, identitas_pegawai, nama, gaji, namaproyek):
        ID_Pegawai.__init__(self, identitas_pegawai, nama)
        Gaji.__init__(self, gaji)
        Nama_proyek.__init__(self, namaproyek)

    def tampilkan(self):
        print("++Profil++")
        print("ID Pegawai  :", self.id_pegawai)
        print("Nama Pegawai:", self.nama_pegawai)
        print("Gaji        :", self.gaji)
        print("Tanggungjawab Proyek:", self.proyek)

manajer = Project_Manager(4529, "Alfa", 700000000, "Proyek Pembangunan Roket")
print("===Manajemen Pegawai==")
manajer.tampilkan()