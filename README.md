# labpy1

#### Algoritma menentukan nilai terbeasar dari 3 buah bilangan.



- Diketahui 3 buah bilangan Bil1, Bil2, Bil3 akan dicari nilai terbesar.




1. Mulai

2. Inisiasi Bil1, Bil2, Bil3 sebagai Integer

3. Baca Bil1
4. Baca Bil2

5. Baca Bil3

6. Jika Bil1 > Bil2 dan Bil1 > Bil3 maka kerjakan langkah nomor 8, selain itu.

7. Jika Bil2 > Bil1 dan Bil2 > Bil3 maka kerjakan langkah nomor 9, selain itu kerjakan langkah nomor 10

8. Cetak "Bilangan terbesar bilangan pertama"

9. Cetak "Bilangan terbesar bilangan kedua"

10. Cetak "Bilangan terbesar bilangan ketiga"

11. Selesai



Berikut dibawah ini Flowchart dan screenshoot hasil eksekusi dari ke 3 kondisi input data program.


Gunakan statement if untuk A sebagai inisiasi Bilangan Pertama.
Gunakan statement elif untuk B sebagai inisiasi Bilangan Kedua.
Gunakan statement else untuk C sebagai inisiasi Bilangan Ketiga.
Kemudian Run

Silahkan lihat contoh di bawah ini :

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


Bilangan Pertama yang menjadi bilangan terbesar.


Bilangan Kedua yang menjadi bilangan terbesar.


Bilangan Ketiga sebagai bilangan terbesar.


Terima Kasih.




