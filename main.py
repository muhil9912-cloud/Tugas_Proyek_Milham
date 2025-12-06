# main.py

from helper import hitung_harga, tampilkan_pesanan

def main():
    pesanan_list = []

    print("=== Sistem Pemesanan Jasa Fotografer ===")

    while True:
        try:
            nama = input("\nMasukkan nama klien: ")
            paket = input("Pilih paket (basic/standard/premium): ")
            durasi = int(input("Durasi sesi (jam): "))

            total = hitung_harga(paket, durasi)

            pesanan = {
                "nama": nama,
                "paket": paket,
                "durasi": durasi,
                "total": total
            }

            pesanan_list.append(pesanan)
            print(f"✅ Pesanan atas nama {nama} berhasil ditambahkan! Total: Rp{total:,}")

        except ValueError as e:
            print(f"⚠ Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan tak terduga: {e}")

        lagi = input("\nTambah pesanan lain? (y/n): ").lower()
        if lagi != 'y':
            break

    tampilkan_pesanan(pesanan_list)
    print("\nTerima kasih telah menggunakan layanan fotografer kami! 📷")


if __name__ == "__main__":
    main()
