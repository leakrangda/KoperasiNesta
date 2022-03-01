import openpyxl as pxl
import sys
import datetime

if __name__ == "__main__":
    if len(sys.argv) > 1:
        workbook = pxl.load_workbook(sys.argv[1])
        aktif = workbook.active

        #take data
        for baris in aktif.values:
            tipe = [type(a) for a in baris]
            print("tipe=", tipe)
            print(baris)
        for baris in aktif.rows:
            print([a.value for a in baris ])