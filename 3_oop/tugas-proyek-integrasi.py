from abc import ABC, abstractmethod

# =======================
# ABSTRACT CLASS
# =======================
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0
        self.__harga_dasar = harga_dasar

    # Getter
    def get_stok(self):
        return self.__stok

    def get_harga_dasar(self):
        return self.__harga_dasar

    # Setter / Method update stok
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    # Abstract Methods
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# =======================
# CHILD CLASS: LAPTOP
# =======================
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        pajak = self.get_harga_dasar() * 0.10
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"   Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(10%): Rp {int(pajak):,}")

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.10
        return (self.get_harga_dasar() + pajak) * jumlah


# =======================
# CHILD CLASS: SMARTPHONE
# =======================
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        pajak = self.get_harga_dasar() * 0.05
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"   Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(5%): Rp {int(pajak):,}")

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.05
        return (self.get_harga_dasar() + pajak) * jumlah


# =======================
# POLYMORPHIC FUNCTION
# =======================
def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0

    for i, item in enumerate(daftar_barang, start=1):
        barang, jumlah = item
        barang.tampilkan_detail()
        subtotal = barang.hitung_harga_total(jumlah)
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}\n")
        total += subtotal

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total):,}")


# =======================
# MAIN PROGRAM
# =======================
print("--- SETUP DATA ---")

laptop = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
smartphone = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop.tambah_stok(10)
smartphone.tambah_stok(-5)  # harus gagal
smartphone.tambah_stok(20)

keranjang = [
    (laptop, 2),
    (smartphone, 1)
]

proses_transaksi(keranjang)
