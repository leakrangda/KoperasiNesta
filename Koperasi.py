import mysql.connector as mconnect
import csv
from mysql.connector.errors import Error
import openpyxl
from itertools import repeat
from ObjectData import *

class Koperasi():
    def __init__(self, f=None, *arg):
        self.koneksi=None
        self.kursor=None
        self.tipe=''

        if f:
            self.f = f
            if self.file_cheker(self.f) in ('xls','xlsx','xlsm'):
                self.tipe = 'excel'
            elif self.file_cheker(self.f) in ('csv'):
                self.tipe = 'CSV'
            else:
                self.tipe = 'UNKNOWN'
        else:
            raise Exception
        self.konek(database="koperasi")
        if self.tipe == 'excel':
            self.buka(self.f, arg[0])
        else:
            self.buka(self.f)
    
    def konek(self, host:str="localhost", user:str="root", password:str="Neogenesis 1", database:str=None):
        try:
            self.koneksi = mconnect.connect(host=host, password=password, user=user, database=database)
            self.kursor = self.koneksi.cursor(buffered=True)
        except Exception as e:
            print("error konek database:",e)
    
    def insertSiswa(self):
        kelas=None
        kelamin=None

        if self.kursor:
            for i in self.data:
                if i[3]=="TBSM 1":
                    kelas=4004
                elif i[3]=="TBSM 2":
                    kelas=4005
                elif i[3]=="MM 1":
                    kelas=4000
                elif i[3]=="MM 2":
                    kelas=4001
                elif i[3]=="TKJ 1":
                    kelas=4002
                elif i[3]=="TKJ 2":
                    kelas=4003
                elif i[3]=="TITL 1":
                    kelas=4006
                elif i[3]=="TITL 2":
                    kelas=4007
                elif i[3]=="OTKP 1":
                    kelas=4009
                elif i[3]=="OTKP 2":
                    kelas=4010
                else:
                    kelas=4008
                if i[4]=="L":
                    kelamin=3000
                elif i[4]=="P":
                    kelamin=3001
                sql = "insert into siswa values({0}, \"{1}\", null, \"{2}\", {3});".format(kelas, i[0],\
                    i[2], kelamin)
                try:
                    self.kursor.execute(sql)
                    self.koneksi.commit()
                except  Error as e:
                    print("error insertion:",e)
                print(sql)
            print("berhasil")
        else:
            print("error")
            print(self.kursor)

    def buka(self, fl:str, *args):
        self.data=None
        if fl:
            if self.tipe == 'CSV' :
                with open(fl, "r") as mfile:
                    rdr = csv.reader(mfile, delimiter=';')
                    self.data = [a for a in rdr]
                    self.tipe = 'csv'
            elif self.tipe == 'excel':
                workbook = openpyxl.load_workbook(fl,read_only=True)
                aktif = workbook[args[0]]
                header = Header([a for a in aktif.iter_rows(1,1,1,8, values_only=True)], 1, 1)
                self.data = tuple(a for a in aktif.values)
                self.tipe = 'excel'
        else:
            print("error buka file")
        return self.data 

    def insertTransaksi(self):
        sql = "insert into transaksi values(default, '{0}', '{1}', '{2}', '{3}')"
        for i in self.data:
            try:
                idSiswa = self.kursor.execute("select nisn from siswa where nama=\"{0}\"".format(i[1].upper()))
                nisn=self.kursor.fetchone()
                if nisn:
                    print(sql.format(i[5],i[7],nisn[0],5000))
                    t= i[7]
                    d = i[5]
                    self.kursor.execute(sql.format(d, t, nisn[0], 5000))
                else:
                    print("tidak ada siswa yang bernama:{0}, jurusan:{1}".format(i[1].upper(),i[3].upper()))
            except Error as e:
                print("error insertion:", e)
        self.koneksi.commit()

    def insertBarang(self):
        sql = "insert into barang values(default, '{0}', '{1}','{2}', '{3}')"
        lstGender = []
        def retGender(gen:Gender, kel:str):
            if Gender.jenis_gender.lower() == kel.lower():
                return True
            else:
                return False 
        
        for i in self.data:
            try:
                self.kursor.execute("select * from gender")
                if any(self.kursor):
                    for i in self.kursor:
                        lstGender.append(Gender(*i))
                    #self.kuror.execute(sql.format(i[1], \
                    #    lstGender[ \
                    #        map(retGender, lstGender, repeat(i[2]).index(True))]), i[3], i[4])
                    print(lstGender)
                else:
                    print("data gender tidak ada, isi dulu!")
            except Exception:
                print("ada error!")

    def insertDetail(self):
        pass

    def insertAdmin(self):
        pass

    def insertGender(self):
        pass

    def insertJurusan(self):
        pass

    def insertKelas(self):
        pass

    def insertKeterangan(self):
        pass

    def insertPembayaran(self):
        pass

    def insertPengambilan(self):
        pass


    def file_cheker(self, file):
        return file.split('.')[-1]

