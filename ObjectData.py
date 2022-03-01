from dataclasses import dataclass
from datetime import time


@dataclass
class Header:
    nama_head:list
    head_x_loc:int
    head_y_loc:int

@dataclass
class Transaksi:
    id_transaksi:str
    siswa:str
    kelamin:str
    jurusan:str
    jumlah:int
    kelas:str
    jam:time

@dataclass
class Siswa:
   id_kelas:int
   nisn:str
   nis:str
   nama:str
   id_gender:int

@dataclass
class Admin:
    id_admin:int
    nama:str
    akun:str
    password:str

@dataclass
class Barang:
    id_barang:int
    nama_barang:str
    id_gender:int
    harga:int
    jumlah:int

@dataclass
class Gender:
    id_gender:int
    jenis_gender:str

@dataclass
class Jenis_Transaksi:
    id_jenis:int
    nama_jenis:str

@dataclass
class Jurusan:
    id_jurusan:int
    kode:str
    nama_jurusan:str

@dataclass
class Kelas:
    id_kelas:int
    tingkat:int
    id_jurusan:int
    bagian:int

@dataclass
class Pembayaran:
    id_pembayaran:int
    id_transaksi:int
    jumlah_bayar:int

@dataclass
class Pengambilan:
    id_pengambilan:int
    id_transaksi:int
    id_barang:int
    jumlah:int
