print ("Program mencari bilangan terbesar dari 3 bilangan\n")

A = int(input("Masukkan Bilangan Pertama: "))
B = int(input("Masukkan Bilangan Kedua: "))
C = int(input("Masukkan Bilangan Ketiga: "))


if A > B > C :
    print("\nBilangan Pertama adalah Bilangan Terbesar = %s" % A)
elif B > C :
    print("\nBilangan Kedua adalah  Bilangan Terbesar = %s" % B)
else:
    print("\nBilangan Ketiga adalah Bilangan Terbesar = %s" % C)
