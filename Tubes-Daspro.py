# File : Tubes_Daspro.py
# Penulis : Deven Gerrard Kartamihardja; Silalahi, Lorenzo Julio Pardamean
# Pembaruan: Menambahkan DP 50% terlebih dahulu sebelum bisa menghuni

MAX = 100

# =========================
# WAKTU SEKARANG (BERBASIS HARIAN)
# =========================
tanggalSekarang = bulanSekarang = tahunSekarang = 0

# =========================
# DATA KAMAR
# =========================
noKamar = [0] * MAX
hargaKamarBulanan = [0] * MAX
hargaKamarTahunan = [0] * MAX

# Array Tamu diaktifkan untuk mencatat inap tamu per kamar/penghuni
jumlahTamu = [0] * MAX
biayaTamuTerakumulasi = [0] * MAX
jumlahKamar = 0

# =========================
# DATA PENGHUNI
# =========================
idPenghuni = [0] * MAX
namaPenghuni = [""] * MAX
kamarPenghuni = [0] * MAX
jenisSewa = [""] * MAX

blnMasuk = [0] * MAX
thnMasuk = [0] * MAX

# Menggunakan tanggal jatuh tempo penuh
tglTempo = [0] * MAX
blnTempo = [0] * MAX
thnTempo = [0] * MAX

statusBayar = [""] * MAX
nominalTerbayar = [0] * MAX
tagihanPokok = [0] * MAX
dendaTagihan = [0] * MAX

jumlahPenghuni = 0
nextId = 1

# =========================
# DATA KELUHAN & KEUANGAN
# =========================
idKeluhanPenghuni = [0] * MAX
isiKeluhan = [""] * MAX
statusKeluhan = [""] * MAX
jumlahKeluhan = 0
totalPendapatan = 0

# ==================================================
# FUNCTION BANTU
# ==================================================


def cariIndexKamar(no):
    i = 0
    while i < jumlahKamar:
        if noKamar[i] == no:
            return i
        i += 1
    return -1


def hitungIsiKamar(no):
    jumlah = 0
    i = 0
    while i < jumlahPenghuni:
        if kamarPenghuni[i] == no:
            jumlah += 1
        i += 1
    return jumlah


def cariIndexPenghuni(idCari):
    i = 0
    while i < jumlahPenghuni:
        if idPenghuni[i] == idCari:
            return i
        i += 1
    return -1


def hitungSelisihHari(tgl1, bln1, thn1, tgl2, bln2, thn2):
    """Menghitung selisih hari (Tanggal 1 dikurangi Tanggal 2) dengan asumsi 1 bulan = 30 hari"""
    totalHari1 = (thn1 * 360) + (bln1 * 30) + tgl1
    totalHari2 = (thn2 * 360) + (bln2 * 30) + tgl2
    return totalHari1 - totalHari2


# ==================================================
# TAGIHAN BARU
# ==================================================


def generateTagihanBaru(idx):
    nomor = kamarPenghuni[idx]
    idxKamar = cariIndexKamar(nomor)

    if jenisSewa[idx] == "Bulanan":
        tagihanPokok[idx] = hargaKamarBulanan[idxKamar]
    else:
        tagihanPokok[idx] = hargaKamarTahunan[idxKamar]

    nominalTerbayar[idx] = 0
    dendaTagihan[idx] = 0
    statusBayar[idx] = "Belum Lunas"


# ==================================================
# KELOLA KAMAR
# ==================================================


def tambahKamar():
    global jumlahKamar
    no = int(input("Nomor kamar : "))
    if cariIndexKamar(no) != -1:
        print("Nomor kamar sudah digunakan.")
        return

    hargaBulan = int(input("Harga kamar (Per Bulan) : Rp"))
    hargaTahun = int(input("Harga kamar (Per Tahun) : Rp"))

    noKamar[jumlahKamar] = no
    hargaKamarBulanan[jumlahKamar] = hargaBulan
    hargaKamarTahunan[jumlahKamar] = hargaTahun
    jumlahKamar += 1
    print("Kamar berhasil ditambahkan.")


def lihatKamar():
    if jumlahKamar == 0:
        print("Belum ada data kamar.")
        return
    print("\n===== DATA KAMAR =====")
    i = 0
    while i < jumlahKamar:
        isi = hitungIsiKamar(noKamar[i])
        print(f"Nomor Kamar : {noKamar[i]}")
        print(f"Harga/Bulan : Rp{hargaKamarBulanan[i]}")
        print(f"Harga/Tahun : Rp{hargaKamarTahunan[i]}")
        print(f"Terisi      : {isi}")
        print("-------------------------")
        i += 1


# ==================================================
# KELOLA PENGHUNI
# ==================================================


def tambahPenghuni():
    global jumlahPenghuni, nextId, totalPendapatan

    nama = input("Nama penghuni : ")
    kamar = int(input("Nomor kamar : "))
    idxKamar = cariIndexKamar(kamar)

    if idxKamar == -1:
        print("Kamar tidak ditemukan.")
        return
    if hitungIsiKamar(kamar) >= 1:
        print("Kamar sudah ditempati.")
        return

    print("1. Bulanan\n2. Tahunan")
    pilih = int(input("Pilihan : "))

    tanggal = int(input("Tanggal masuk : "))
    while tanggal < 1 or tanggal > 30:
        print("Tanggal harus 1 - 30")
        tanggal = int(input("Tanggal masuk : "))

    bulan = int(input("Bulan masuk : "))
    while bulan < 1 or bulan > 12:
        print("Bulan harus 1 - 12")
        bulan = int(input("Bulan masuk : "))
    tahun = int(input("Tahun masuk : "))

    # Tanggal Jatuh Tempo persis sama dengan tanggal masuk di bulan/tahun depan
    tempoTanggal = tanggal
    if pilih == 1:
        tempoBulan = bulan + 1
        tempoTahun = tahun
        if tempoBulan > 12:
            tempoBulan = 1
            tempoTahun += 1
        sewa = "Bulanan"
        tagihan = hargaKamarBulanan[idxKamar]
    else:
        tempoBulan = bulan
        tempoTahun = tahun + 1
        sewa = "Tahunan"
        tagihan = hargaKamarTahunan[idxKamar]

    minimalDP = tagihan // 2

    print(f"Tagihan Pokok : Rp{tagihan}")
    print(f"Minimal DP (50%) : Rp{minimalDP}")

    dp = int(input("Masukkan nominal DP : Rp"))

    while dp < minimalDP or dp > tagihan:
        if dp < minimalDP:
            print("DP tidak boleh kurang dari 50% tagihan!")
        else:
            print("DP tidak boleh melebihi total tagihan!")
        dp = int(input("Masukkan nominal DP : Rp"))

    idPenghuni[jumlahPenghuni] = nextId
    namaPenghuni[jumlahPenghuni] = nama
    kamarPenghuni[jumlahPenghuni] = kamar
    jenisSewa[jumlahPenghuni] = sewa
    blnMasuk[jumlahPenghuni] = bulan
    thnMasuk[jumlahPenghuni] = tahun

    tglTempo[jumlahPenghuni] = tempoTanggal
    blnTempo[jumlahPenghuni] = tempoBulan
    thnTempo[jumlahPenghuni] = tempoTahun

    tagihanPokok[jumlahPenghuni] = tagihan
    dendaTagihan[jumlahPenghuni] = 0
    nominalTerbayar[jumlahPenghuni] = dp
    if dp == tagihan:
        statusBayar[jumlahPenghuni] = "Lunas"
    else:
        statusBayar[jumlahPenghuni] = "Belum Lunas"
    totalPendapatan += dp

    print("\n===== DATA PENGHUNI =====")
    print(f"ID Penghuni : {nextId}")
    print(f"Nama        : {nama}")
    print(f"Tagihan     : Rp{tagihan}")
    print(f"DP Dibayar  : Rp{dp}")
    print(f"Sisa Bayar  : Rp{tagihan - dp}")
    jumlahPenghuni += 1
    nextId += 1


def lihatPenghuni():
    if jumlahPenghuni == 0:
        print("Belum ada penghuni.")
        return
    print("\n===== DATA PENGHUNI =====")
    i = 0
    while i < jumlahPenghuni:
        print(f"ID          : {idPenghuni[i]}")
        print(f"Nama        : {namaPenghuni[i]}")
        print(f"Kamar       : {kamarPenghuni[i]}")
        print(f"Jenis Sewa  : {jenisSewa[i]}")
        print(f"Jatuh Tempo : {tglTempo[i]}/{blnTempo[i]}/{thnTempo[i]}")
        print(f"Status      : {statusBayar[i]}")
        print("-------------------------")
        i += 1


# ==================================================
# FITUR TAMU
# ==================================================


def kelolaTamu():
    idCari = int(input("Masukkan ID Penghuni: "))
    idx = cariIndexPenghuni(idCari)

    if idx == -1:
        print("ID Penghuni tidak ditemukan.")
        return

    print(f"Penghuni Kamar: {namaPenghuni[idx]} (Kamar {kamarPenghuni[idx]})")
    tamu = int(input("Jumlah tamu baru yang menginap : "))
    while tamu < 0:
        print("Jumlah tamu tidak boleh negatif")
        tamu = int(input("Jumlah tamu baru yang menginap : "))

    hari = int(input("Berapa hari menginap           : "))
    while hari < 0:
        print("Jumlah hari tidak boleh negatif")
        hari = int(input("Berapa hari menginap : "))

    # Kalkulasi biaya per kedatangan secara instan agar tidak terjadi perkalian silang salah
    biayaKedatanganSkg = tamu * hari * 50000

    # Akumulasikan langsung ke dalam nominal Rupiah
    jumlahTamu[idx] += tamu
    biayaTamuTerakumulasi[idx] += biayaKedatanganSkg

    print(
        f"Berhasil menambahkan {tamu} tamu untuk {hari} hari (Biaya: Rp{biayaKedatanganSkg})."
    )
    print(f"Total beban biaya tamu saat ini: Rp{biayaTamuTerakumulasi[idx]}")


# ==================================================
# LIHAT & UPDATE TAGIHAN REALTIME
# ==================================================


def updateDendaRealtime(idx):
    # Hitung selisih hari antara tanggal sistem saat ini dengan tanggal jatuh tempo
    lewatHari = hitungSelisihHari(
        tanggalSekarang,
        bulanSekarang,
        tahunSekarang,
        tglTempo[idx],
        blnTempo[idx],
        thnTempo[idx],
    )
    if lewatHari > 0 and statusBayar[idx] == "Belum Lunas":
        dendaTagihan[idx] = lewatHari * 10000
    else:
        dendaTagihan[idx] = 0


def lihatTagihan():
    idCari = int(input("Masukkan ID Penghuni : "))
    idx = cariIndexPenghuni(idCari)

    if idx == -1:
        print("ID tidak ditemukan.")
        return

    updateDendaRealtime(idx)

    # LANGSUNG AMBIL DARI NOMINAL YANG SUDAH BENAR
    biayaTamu = biayaTamuTerakumulasi[idx]

    totalTagihan = tagihanPokok[idx] + dendaTagihan[idx] + biayaTamu
    sisaTagihan = totalTagihan - nominalTerbayar[idx]
    if sisaTagihan < 0:
        sisaTagihan = 0

    print("\n===== TAGIHAN REAL-TIME =====")
    print(f"ID            : {idPenghuni[idx]}")
    print(f"Nama          : {namaPenghuni[idx]}")
    print(f"Tagihan Pokok : Rp{tagihanPokok[idx]}")
    print(
        f"Biaya Tamu    : Rp{biayaTamu} (Total akumulasi dari {jumlahTamu[idx]} tamu)"
    )
    print(f"Denda Terlambat: Rp{dendaTagihan[idx]}")
    print(f"Total Tagihan : Rp{totalTagihan}")
    print(f"Sudah Bayar   : Rp{nominalTerbayar[idx]}")
    print(f"Sisa Tagihan  : Rp{sisaTagihan}")
    print(f"Status        : {statusBayar[idx]}")


# ==================================================
# UBAH TANGGAL (SIMULASI WAKTU BERJALAN)
# ==================================================


def ubahTanggal():
    global tanggalSekarang, bulanSekarang, tahunSekarang
    print("\n--- Simulasi Perubahan Waktu ---")
    tanggal = int(input("Tanggal sekarang : "))
    while tanggal < 1 or tanggal > 30:
        print("Tanggal harus 1 - 30")
        tanggal = int(input("Tanggal sekarang : "))
    bulan = int(input("Bulan sekarang : "))
    while bulan < 1 or bulan > 12:
        print("Bulan harus 1 - 12")
        bulan = int(input("Bulan sekarang : "))
    tahun = int(input("Tahun sekarang : "))

    tanggalSekarang = tanggal
    bulanSekarang = bulan
    tahunSekarang = tahun
    print(f"Sistem diperbarui ke: {tanggalSekarang}/{bulanSekarang}/{tahunSekarang}")

    # Cek otomatisasi pembuatan periode tagihan baru jika tanggal sistem melompati tanggal tempo lama
    i = 0
    while i < jumlahPenghuni:
        updateDendaRealtime(i)
        lewatHari = hitungSelisihHari(
            tanggalSekarang,
            bulanSekarang,
            tahunSekarang,
            tglTempo[i],
            blnTempo[i],
            thnTempo[i],
        )

        # Jika waktu sudah maju melewati tempo dan status bulan lalu SUDAH LUNAS, perbarui ke periode bulan/tahun depan
        if lewatHari >= 0 and statusBayar[i] == "Lunas":
            if jenisSewa[i] == "Bulanan":
                blnTempo[i] += 1
                if blnTempo[i] > 12:
                    blnTempo[i] = 1
                    thnTempo[i] += 1
            else:
                thnTempo[i] += 1
            generateTagihanBaru(i)
            print(
                f"-> Penghuni {namaPenghuni[i]} (ID: {idPenghuni[i]}) memasuki periode sewa baru. Tagihan diterbitkan."
            )
        i += 1


# ==================================================
# PEMBAYARAN
# ==================================================


def pembayaran():
    global totalPendapatan
    idCari = int(input("Masukkan ID Penghuni : "))
    idx = cariIndexPenghuni(idCari)

    if idx == -1:
        print("ID tidak ditemukan.")
        return

    updateDendaRealtime(idx)

    # Ambil nominal uang langsung
    biayaTamu = biayaTamuTerakumulasi[idx]
    totalTagihan = tagihanPokok[idx] + dendaTagihan[idx] + biayaTamu

    print(f"\nTagihan Pokok : Rp{tagihanPokok[idx]}")
    print(f"Biaya Tamu    : Rp{biayaTamu}")
    print(f"Denda (Hari)  : Rp{dendaTagihan[idx]}")
    print(f"Total Tagihan : Rp{totalTagihan}")
    print(f"Sudah Dibayar : Rp{nominalTerbayar[idx]}")
    sisaTagihan = totalTagihan - nominalTerbayar[idx]
    if sisaTagihan < 0:
        sisaTagihan = 0
    print(f"Sisa Tagihan  : Rp{sisaTagihan}")

    if statusBayar[idx] == "Lunas":
        print("Tagihan periode ini sudah lunas!")
        return

    bayar = int(input("Nominal pembayaran : "))
    while bayar <= 0:
        print("Nominal pembayaran harus lebih dari 0")
        bayar = int(input("Nominal pembayaran : "))
    nominalTerbayar[idx] += bayar

    if nominalTerbayar[idx] >= totalTagihan:
        wajibBayar = totalTagihan - (nominalTerbayar[idx] - bayar)
        totalPendapatan += wajibBayar

        # RESET VARIABEL TAMU KE 0 SETELAH LUNAS
        jumlahTamu[idx] = 0
        biayaTamuTerakumulasi[idx] = 0

        kelebihan = nominalTerbayar[idx] - totalTagihan
        statusBayar[idx] = "Lunas"
        print("Pembayaran lunas.")
        if kelebihan > 0:
            print(f"Kembalian : Rp{kelebihan}")
            nominalTerbayar[idx] = totalTagihan
    else:
        totalPendapatan += bayar
        statusBayar[idx] = "Belum Lunas"
        print(f"Sisa Tagihan : Rp{totalTagihan - nominalTerbayar[idx]}")


# ==================================================
# CHECKOUT
# ==================================================


def checkoutPenghuni():
    global jumlahPenghuni, jumlahKeluhan
    idCari = int(input("Masukkan ID Penghuni : "))
    idx = cariIndexPenghuni(idCari)

    if idx == -1:
        print("ID tidak ditemukan.")
        return

    updateDendaRealtime(idx)
    biayaTamu = biayaTamuTerakumulasi[idx]
    totalTagihan = tagihanPokok[idx] + dendaTagihan[idx] + biayaTamu

    if nominalTerbayar[idx] < totalTagihan:
        print(
            f"Gagal Checkout! Sisa tagihan yang harus dilunasi: Rp{totalTagihan - nominalTerbayar[idx]}"
        )
        return

    # Geser Array Penghuni
    i = idx
    while i < jumlahPenghuni - 1:
        idPenghuni[i] = idPenghuni[i + 1]
        namaPenghuni[i] = namaPenghuni[i + 1]
        kamarPenghuni[i] = kamarPenghuni[i + 1]
        jenisSewa[i] = jenisSewa[i + 1]
        blnMasuk[i] = blnMasuk[i + 1]
        thnMasuk[i] = thnMasuk[i + 1]
        tglTempo[i] = tglTempo[i + 1]
        blnTempo[i] = blnTempo[i + 1]
        thnTempo[i] = thnTempo[i + 1]
        tagihanPokok[i] = tagihanPokok[i + 1]
        dendaTagihan[i] = dendaTagihan[i + 1]
        nominalTerbayar[i] = nominalTerbayar[i + 1]
        statusBayar[i] = statusBayar[i + 1]
        jumlahTamu[i] = jumlahTamu[i + 1]
        biayaTamuTerakumulasi[i] = biayaTamuTerakumulasi[i + 1]
        i += 1

    jumlahPenghuni -= 1
    print("Checkout berhasil. Data penghuni dihapus dan kamar dikosongkan.")


# ==================================================
# FITUR KELUHAN & LAPORAN (DIURUTKAN SECARA SEDERHANA)
# ==================================================


def inputKeluhan():
    global jumlahKeluhan
    idCari = int(input("Masukkan ID Penghuni : "))
    idx = cariIndexPenghuni(idCari)
    if idx == -1:
        return print("ID tidak ditemukan.")

    keluhan = input("Keluhan : ")
    idKeluhanPenghuni[jumlahKeluhan] = idCari
    isiKeluhan[jumlahKeluhan] = keluhan
    statusKeluhan[jumlahKeluhan] = "Belum Selesai"
    jumlahKeluhan += 1
    print("Keluhan dicatat.")


def lihatKeluhan():
    if jumlahKeluhan == 0:
        return print("Belum ada keluhan.")
    print("\n===== DATA KELUHAN =====")
    i = 0
    while i < jumlahKeluhan:
        print(
            f"ID Penghuni : {idKeluhanPenghuni[i]}\nKeluhan     : {isiKeluhan[i]}\nStatus      : {statusKeluhan[i]}\n----------------------"
        )
        i += 1


def updateStatusKeluhan():
    if jumlahKeluhan == 0:
        print("Belum ada keluhan.")
        return

    noKeluhan = int(input("Nomor keluhan yang ingin diupdate (lihat daftar keluhan): "))
    if noKeluhan < 1 or noKeluhan > jumlahKeluhan:
        print("Nomor keluhan tidak valid.")
        return

    idx = noKeluhan - 1
    print(f"Keluhan     : {isiKeluhan[idx]}")
    print(f"Status saat ini: {statusKeluhan[idx]}")

    if statusKeluhan[idx] == "Selesai":
        print("Keluhan ini sudah ditandai selesai.")
        return

    konfirmasi = input("Tandai sebagai selesai? (y/n): ")
    if konfirmasi == "y":
        statusKeluhan[idx] = "Selesai"
        print("Status keluhan berhasil diperbarui.")
    else:
        print("Tidak ada perubahan.")


def laporan():
    kamarTerisi = 0
    i = 0
    while i < jumlahKamar:
        if hitungIsiKamar(noKamar[i]) > 0:
            kamarTerisi += 1
        i += 1

    lunas = belumLunas = 0
    i = 0
    while i < jumlahPenghuni:
        if statusBayar[i] == "Lunas":
            lunas += 1
        else:
            belumLunas += 1
        i += 1

    print("\n===== LAPORAN KEUANGAN & UNIT =====")
    print(
        f"Total Kamar/Kosong/Terisi : {jumlahKamar} / {jumlahKamar-kamarTerisi} / {kamarTerisi}"
    )
    print(
        f"Total Penghuni Aktif      : {jumlahPenghuni} (Lunas: {lunas}, Belum Lunas: {belumLunas})"
    )
    print(f"Total Pendapatan Kas Kost : Rp{totalPendapatan}")


# ==================================================
# MENU & MAIN
# ==================================================


def menu():
    print(f"\n===== SELAMAT DATANG DI KOS =====")
    print(f"Tanggal Hari Ini: {tanggalSekarang}/{bulanSekarang}/{tahunSekarang}")
    print("NO\t\t\t\tNO\t\t")
    print(f"-----------------------------------------------------------------")
    print("1.\tTambah Kamar\t\t2.\tLihat Kamar")
    print("3.\tTambah Penghuni\t\t4.\tLihat Penghuni")
    print("5.\tKelola Tamu Menginap\t6.\tLihat Tagihan Real-time")
    print("7.\tPembayaran\t\t8.\tCheckout Penghuni")
    print("9.\tInput Keluhan\t\t10.\tUpdate Status Keluhan")
    print("11.\tLihat Keluhan\t\t12.\tLaporan keuangan")
    print("13.\tUbah Tanggal (Simulasi)")
    print("0.\tKeluar")


def main():
    global tanggalSekarang, bulanSekarang, tahunSekarang

    print("=== INISIALISASI TANGGAL AWAL SISTEM ===")
    tanggalSekarang = int(input("Tanggal (1-30) : "))
    bulanSekarang = int(input("Bulan (1-12)   : "))
    tahunSekarang = int(input("Tahun          : "))

    pilihan = -1
    while pilihan != 0:
        menu()
        pilihan = int(input("Pilihan menu : "))

        if pilihan == 1:
            tambahKamar()
        elif pilihan == 2:
            lihatKamar()
        elif pilihan == 3:
            tambahPenghuni()
        elif pilihan == 4:
            lihatPenghuni()
        elif pilihan == 5:
            kelolaTamu()
        elif pilihan == 6:
            lihatTagihan()
        elif pilihan == 7:
            pembayaran()
        elif pilihan == 8:
            checkoutPenghuni()
        elif pilihan == 9:
            inputKeluhan()
        elif pilihan == 10:
            updateStatusKeluhan()
        elif pilihan == 11:
            lihatKeluhan()
        elif pilihan == 12:
            laporan()
        elif pilihan == 13:
            ubahTanggal()
        elif pilihan == 0:
            print("Program keluar.")
        else:
            print("Pilihan salah.")


if __name__ == "__main__":
    main()
