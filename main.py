print("============BELANJA BULANAN===========")
print("--------------------------------------")

list_belanja = []
total = 0

while True:
    nama_belanja = input("nama belanjaan :")
    harga = (float(input("harga belanjaan :")))
    jumlah = (int(input("jumlah barang :")))
    
    subtotal = harga * jumlah
    list_belanja.append((nama_belanja, harga, jumlah, subtotal))
    total += subtotal
    
    tambah = input("tambah belanjaan? y/n:").lower()
    if tambah == "n":
        break
    
print("\n========LIST BELANJA BULANAN========")
print("--------------------------------------")
for item in list_belanja:
    print(f"{item[0]} x{item[2]} =RP {item[3]} ")
print("\n--------------------------------------")
print(f"total belanja {total}")
print("\n==============terimakasih sudah berbelanja=========")