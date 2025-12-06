# helper.py

def hitung_harga(paket: str, durasi: int) -> int:
    """
    Menghitung total harga berdasarkan paket dan durasi pemotretan.
    """
    harga_per_jam = {
        "basic": 250000,
        "standard": 400000,
        "premium": 600000
    }

    if paket.lower() not in harga_per_jam:
        raise ValueError("Paket tidak valid. Pilih: basic, standard, atau premium.")

    return harga_per_jam[paket.lower()] * durasi


def tampilkan_pesanan(pesanan_list):
    """
    Menampilkan semua data pesanan klien.
    """
    print("\n📸 Daftar Pemesanan Fotografer:")
    for idx, p in enumerate(pesanan_list, 1):
        print(f"{idx}. {p['nama']} - Paket {p['paket']} ({p['durasi']} jam) | Total: Rp{p['total']:,}")