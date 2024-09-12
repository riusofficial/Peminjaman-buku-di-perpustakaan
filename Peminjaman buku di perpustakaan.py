# Inisialisasi list buku sebagai contoh
buku_perpustakaan = []

# Fungsi Create - Menambah buku ke perpustakaan
def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    tahun = input("Masukkan tahun terbit: ")
    buku = {
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun
    }
    buku_perpustakaan.append(buku)
    print("Buku berhasil ditambahkan!\n")

# Fungsi Read - Menampilkan semua buku di perpustakaan
def tampilkan_buku():
    if not buku_perpustakaan:
        print("Tidak ada buku dalam perpustakaan.\n")
    else:
        for index, buku in enumerate(buku_perpustakaan, start=1):
            print(f"{index}. Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun: {buku['tahun']}")
        print()

# Fungsi Update - Mengupdate informasi buku berdasarkan judul
def update_buku():
    judul = input("Masukkan judul buku yang ingin diupdate: ")
    for buku in buku_perpustakaan:
        if buku['judul'].lower() == judul.lower():
            buku['judul'] = input("Masukkan judul baru: ")
            buku['penulis'] = input("Masukkan nama penulis baru: ")
            buku['tahun'] = input("Masukkan tahun terbit baru: ")
            print("Informasi buku berhasil diupdate!\n")
            return
    print("Buku tidak ditemukan!\n")

# Fungsi Delete - Menghapus buku berdasarkan judul
def hapus_buku():
    judul = input("Masukkan judul buku yang ingin dihapus: ")
    for buku in buku_perpustakaan:
        if buku['judul'].lower() == judul.lower():
            buku_perpustakaan.remove(buku)
            print("Buku berhasil dihapus!\n")
            return
    print("Buku tidak ditemukan!\n")

# Fungsi utama untuk mengatur navigasi
def main():
    while True:
        print("=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Semua Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_buku()
        elif pilihan == '2':
            tampilkan_buku()
        elif pilihan == '3':
            update_buku()
        elif pilihan == '4':
            hapus_buku()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih menu yang tersedia.\n")

# Menjalankan program utama
main()
