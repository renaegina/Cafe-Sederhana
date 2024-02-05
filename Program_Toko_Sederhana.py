# Nama    : Program Toko Sederhana Menggunakan Python
# Tanggal : 8 Desember 2021
# Author  : Rena Egina

print("=======================================")
print("\t\tRENSCAFE")
print("=======================================")
print("Pilihan Menu")
print("1. French Fries     = Rp.35.000,-")
print("2. Fruit Salad      = Rp.35.000,-")
print("3. Truffle Fries    = Rp.30.000,-")
print("4. Steak Tuna       = Rp.45.000,-")
print("5. Asparagus Soup   = Rp.50.000,-")
pilih = int(input("Masukan menu : "))
if pilih == 1:
    print("French Fries dengan harga Rp.35.000,-")
    jumlah =  int(input("Jumlah pesanan : "))
    print("")
    total = jumlah * 35.000
    print("Total harga : ",total)
    print("**********Terimakasih**********")
elif pilih == 2:
    print("Fruit Salad dengan harga Rp.35.000,-")
    jumlah =  int(input("Jumlah pesanan : "))
    print("")
    total = jumlah * 35.000
    print("Total harga : ",total)
    print("**********Terimakasih**********")
elif pilih == 3:
    print("Truffle Fries  dengan harga Rp.30.000,-")
    jumlah =  int(input("Jumlah pesanan : "))
    print("")
    total = jumlah * 30.000
    print("Total harga : ",total)
    print("**********Terimakasih**********")
elif pilih == 4:
    print("Steak Tuna dengan harga Rp.45.000,-")
    jumlah =  int(input("Jumlah pesanan : "))
    print("")
    total = jumlah * 45.000
    print("Total harga : ",total)
    print("**********Terimakasih**********")
elif pilih == 5:
    print("Asparagus Soup dengan harga Rp.50.000,-")
    jumlah =  int(input("Jumlah pesanan : "))
    print("")
    total = jumlah * 50.00
    print("Total harga : ",total)
    print("**********Terimakasih**********")

