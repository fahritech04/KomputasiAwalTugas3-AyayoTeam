# Mengimpor modul threading untuk membuat dan menjalankan thread
import threading

# Meminta input angka awal dari pengguna
angka_awal = int(input("Input angka awal: "))

# Meminta input angka akhir dari pengguna
angka_akhir = int(input("Input angka akhir: "))

# Meminta jumlah thread dari pengguna
jumlah_thread = int(input("Thread yang digunakan (minimal 2): "))

# Memeriksa apakah jumlah thread minimal 2
if jumlah_thread < 2:
    print("Jumlah thread minimal adalah 2.")
    exit()

# Membuat list kosong untuk menyimpan hasil dari setiap thread
hasil_thread = [0] * jumlah_thread

# Membuat fungsi yang akan dijalankan oleh setiap thread
def hitung_jumlah(index, awal, akhir):
    # Menghitung jumlah angka pada rentang yang diberikan
    hasil_thread[index] = sum(range(awal, akhir + 1))

# Menghitung jumlah angka yang harus diproses setiap thread
total_angka = angka_akhir - angka_awal + 1

# Menghitung ukuran pembagian angka untuk setiap thread
ukuran = total_angka // jumlah_thread

# Membuat list kosong untuk menyimpan objek thread
threads = []

# Melakukan perulangan untuk membuat setiap thread
for i in range(jumlah_thread):
    # Menentukan angka awal untuk thread saat ini
    awal = angka_awal + i * ukuran

    # Menentukan angka akhir untuk thread saat ini
    if i == jumlah_thread - 1:
        akhir = angka_akhir
    else:
        akhir = awal + ukuran - 1

    # Membuat objek thread dan menentukan fungsi yang dijalankan
    thread = threading.Thread(
        target=hitung_jumlah,
        args=(i, awal, akhir)
    )

    # Menambahkan thread ke dalam list
    threads.append(thread)

    # Menjalankan thread
    thread.start()

# Menunggu seluruh thread selesai bekerja
for thread in threads:
    thread.join()

# Menjumlahkan seluruh hasil dari masing-masing thread
hasil_akhir = sum(hasil_thread)

# Menampilkan hasil penjumlahan
print("Hasil penjumlahan:", hasil_akhir)