import getopt
import sys
from Koperasi import Koperasi

if __name__ == "__main__":
    inputFile = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:ts",["file="])
    except getopt.GetoptError:
        print("usage: insertData.py -t -s -f <nama file>")
        sys.exit(1)
    if args:
        inputFile = args[0]
    for opt, arg in opts:
        if opt in ('-f','--file'):
            inputFile = arg
        if opt == '-s':
            if inputFile.split(".")[-1] in ("xlsx", "xls", "xlm"):
                f = Koperasi(inputFile, "siswa")
            else:
                f = Koperasi(inputFile)
            f.insertSiswa()
        elif opt == '-t':
            if inputFile.split(".")[-1] in ("xlsx", "xls", "xlsm"):
                f = Koperasi(inputFile, "Transaksi Harian")
            else:
                f = Koperasi(inputFile)
            f.insertTransaksi()
        else:
            print("usage: insertData.py -t -s -f <nama file>")
    print("ini dieksekusi, opt={0}, args=({1})".format(opts, args))