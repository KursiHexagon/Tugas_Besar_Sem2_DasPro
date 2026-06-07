# Problems:
# 1. Checkout: Tagihan selalu terupdate setelah penghuni melunasi tagihan. Sementara penghuni tidak bisa checkout sebelum tagihan lunas.
# 2. Harga kos: Harga per tahun tetap menghitung (harga per tahun * 12)/jumlah penghuni.
# Contoh: harga bulanan Rp1.000.000. Maka bila ada 2 orang penghuni, harga kos tahunan = (Rp12.000.000)/2 yaitu Rp6.000.000 (terlalu jauh dengan harga seharusnya).

# File : Tubes_Daspro.py
# Penulis : Deven Gerrard Kartamihardja; Silalahi, Lorenzo Julio Pardamean
# Tujuan Program : Sistem Manajemen Kost
#
# Kamus Data
# MAX : kapasitas maksimum data

MAX = 100

# =========================
# DATA KAMAR
# =========================

noKamar = [0] * MAX
hargaKamar = [0] * MAX
kapasitasKamar = [0] * MAX

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

blnTempo = [0] * MAX
thnTempo = [0] * MAX

statusBayar = [""] * MAX

nominalTerbayar = [0] * MAX

tagihanPokok = [0] * MAX
dendaTagihan = [0] * MAX

jumlahPenghuni = 0

nextId = 1

# =========================
# DATA KELUHAN
# =========================

idKeluhanPenghuni = [0] * MAX
isiKeluhan = [""] * MAX

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


# ==================================================
# TAGIHAN BARU
# ==================================================


def generateTagihanBaru(idx):

    nomor = kamarPenghuni[idx]

    idxKamar = cariIndexKamar(nomor)

    harga = hargaKamar[idxKamar]

    isi = hitungIsiKamar(nomor)

    if isi == 0:
        isi = 1

    if jenisSewa[idx] == "Bulanan":
        tagihanPokok[idx] = harga // isi
    else:
        tagihanPokok[idx] = (harga * 12) // isi

    nominalTerbayar[idx] = 0
    dendaTagihan[idx] = 0


# ==================================================
# KELOLA KAMAR
# ==================================================


def tambahKamar():

    global jumlahKamar

    no = int(input("Nomor kamar : "))

    if cariIndexKamar(no) != -1:
        print("Nomor kamar sudah digunakan.")
        return

    harga = int(input("Harga kamar : "))
    kapasitas = int(input("Kapasitas kamar : "))
    while kapasitas <= 0:
        print("Kapasitas harus lebih dari 0")
        kapasitas = int(input("Kapasitas kamar : "))

    noKamar[jumlahKamar] = no
    hargaKamar[jumlahKamar] = harga
    kapasitasKamar[jumlahKamar] = kapasitas

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
        print(f"Harga       : Rp{hargaKamar[i]}")
        print(f"Kapasitas   : {kapasitasKamar[i]}")
        print(f"Terisi      : {isi}")
        print("-------------------------")

        i += 1


# ==================================================
# GENERATE TAGIHAN
# ==================================================


def hitungTagihanAwal(no):

    idx = cariIndexKamar(no)

    harga = hargaKamar[idx]

    isi = hitungIsiKamar(no)

    if isi == 0:
        return harga

    return harga // (isi + 1)


# ==================================================
# KELOLA PENGHUNI
# ==================================================


def tambahPenghuni():

    global jumlahPenghuni
    global nextId

    nama = input("Nama penghuni : ")

    kamar = int(input("Nomor kamar : "))

    idxKamar = cariIndexKamar(kamar)

    if idxKamar == -1:
        print("Kamar tidak ditemukan.")
        return

    isi = hitungIsiKamar(kamar)

    if isi >= kapasitasKamar[idxKamar]:
        print("Kamar sudah penuh.")
        return

    print("1. Bulanan")
    print("2. Tahunan")

    pilih = int(input("Pilihan : "))

    bulan = int(input("Bulan masuk : "))
    while bulan < 1 or bulan > 12:
        print("Bulan harus 1 - 12")
        bulan = int(input("Bulan masuk : "))
    tahun = int(input("Tahun masuk : "))

    if pilih == 1:

        tempoBulan = bulan + 1
        tempoTahun = tahun

        if tempoBulan > 12:
            tempoBulan = 1
            tempoTahun += 1

        sewa = "Bulanan"

    else:

        tempoBulan = bulan
        tempoTahun = tahun + 1

        sewa = "Tahunan"

    idxKamar = cariIndexKamar(kamar)

    harga = hargaKamar[idxKamar]

    isi = hitungIsiKamar(kamar)

    if isi == 0:
        pembagi = 1
    else:
        pembagi = isi + 1

    if pilih == 1:
        tagihan = harga // pembagi
    else:
        tagihan = (harga * 12) // pembagi

    idPenghuni[jumlahPenghuni] = nextId
    namaPenghuni[jumlahPenghuni] = nama

    kamarPenghuni[jumlahPenghuni] = kamar

    jenisSewa[jumlahPenghuni] = sewa

    blnMasuk[jumlahPenghuni] = bulan
    thnMasuk[jumlahPenghuni] = tahun

    blnTempo[jumlahPenghuni] = tempoBulan
    thnTempo[jumlahPenghuni] = tempoTahun

    tagihanPokok[jumlahPenghuni] = tagihan
    dendaTagihan[jumlahPenghuni] = 0

    nominalTerbayar[jumlahPenghuni] = 0

    statusBayar[jumlahPenghuni] = "Belum Lunas"

    print("\n===== DATA PENGHUNI =====")
    print(f"ID Penghuni : {nextId}")
    print(f"Nama        : {nama}")
    print(f"Tagihan     : Rp{tagihan}")

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
        print(f"Jatuh Tempo : {blnTempo[i]}/{thnTempo[i]}")
        print(f"Status      : {statusBayar[i]}")
        print("-------------------------")

        i += 1


# ==================================================
# LIHAT TAGIHAN
# ==================================================


def lihatTagihan():

    idCari = int(input("Masukkan ID Penghuni : "))

    idx = cariIndexPenghuni(idCari)

    if idx == -1:
        print("ID tidak ditemukan.")
        return

    totalTagihan = tagihanPokok[idx] + dendaTagihan[idx]
    sisaTagihan = totalTagihan - nominalTerbayar[idx]

    print("\n===== TAGIHAN =====")
    print(f"ID            : {idPenghuni[idx]}")
    print(f"Nama          : {namaPenghuni[idx]}")
    print(f"Tagihan Pokok : Rp{tagihanPokok[idx]}")
    print(f"Denda         : Rp{dendaTagihan[idx]}")
    print(f"Total Tagihan : Rp{totalTagihan}")
    print(f"Sudah Bayar   : Rp{nominalTerbayar[idx]}")
    print(f"Sisa Tagihan  : Rp{sisaTagihan}")
    print(f"Status        : {statusBayar[idx]}")

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

    bulanSekarang = int(input("Bulan sekarang : "))
    tahunSekarang = int(input("Tahun sekarang : "))

    selisihBulan = ((tahunSekarang - thnTempo[idx]) * 12) + (
        bulanSekarang - blnTempo[idx]
    )

    if selisihBulan > 0:
        dendaTagihan[idx] = selisihBulan * 50000
    else:
        dendaTagihan[idx] = 0

    totalTagihan = tagihanPokok[idx] + dendaTagihan[idx]

    print(f"\nTagihan Pokok : Rp{tagihanPokok[idx]}")
    print(f"Denda         : Rp{dendaTagihan[idx]}")
    print(f"Total Tagihan : Rp{totalTagihan}")
    print(f"Sudah Dibayar : Rp{nominalTerbayar[idx]}")

    bayar = int(input("Nominal pembayaran : "))

    nominalTerbayar[idx] += bayar

    totalPendapatan += bayar

    if nominalTerbayar[idx] >= totalTagihan:

        kelebihan = nominalTerbayar[idx] - totalTagihan

        print("Pembayaran lunas.")
        print(f"Kembalian : Rp{kelebihan}")

        statusBayar[idx] = "Lunas"

        if jenisSewa[idx] == "Bulanan":

            blnTempo[idx] += 1

            if blnTempo[idx] > 12:
                blnTempo[idx] = 1
                thnTempo[idx] += 1

        else:

            thnTempo[idx] += 1

        generateTagihanBaru(idx)

        statusBayar[idx] = "Belum Lunas"

    else:

        statusBayar[idx] = "Belum Lunas"

        sisa = totalTagihan - nominalTerbayar[idx]

        print(f"Sisa Tagihan : Rp{sisa}")


# ==================================================
# KELUHAN
# ==================================================


def inputKeluhan():

    global jumlahKeluhan

    idCari = int(input("Masukkan ID Penghuni : "))

    idx = cariIndexPenghuni(idCari)

    if idx == -1:
        print("ID tidak ditemukan.")
        return

    keluhan = input("Keluhan : ")

    idKeluhanPenghuni[jumlahKeluhan] = idCari
    isiKeluhan[jumlahKeluhan] = keluhan

    jumlahKeluhan += 1

    print("Keluhan berhasil dicatat.")


def lihatKeluhan():

    if jumlahKeluhan == 0:
        print("Belum ada keluhan.")
        return

    print("\n===== DATA KELUHAN =====")

    i = 0

    while i < jumlahKeluhan:

        print(f"ID Penghuni : {idKeluhanPenghuni[i]}")
        print(f"Keluhan     : {isiKeluhan[i]}")
        print("----------------------")

        i += 1


# ==================================================
# CHECKOUT PENGHUNI
# ==================================================


def checkoutPenghuni():

    global jumlahPenghuni
    global jumlahKeluhan

    idCari = int(input("Masukkan ID Penghuni : "))

    idx = cariIndexPenghuni(idCari)

    if idx == -1:
        print("ID tidak ditemukan.")
        return

    if statusBayar[idx] != "Lunas":
        print("Penghuni masih memiliki tunggakan.")
        return

    i = idx

    while i < jumlahPenghuni - 1:

        idPenghuni[i] = idPenghuni[i + 1]
        namaPenghuni[i] = namaPenghuni[i + 1]

        kamarPenghuni[i] = kamarPenghuni[i + 1]

        jenisSewa[i] = jenisSewa[i + 1]

        blnMasuk[i] = blnMasuk[i + 1]
        thnMasuk[i] = thnMasuk[i + 1]

        blnTempo[i] = blnTempo[i + 1]
        thnTempo[i] = thnTempo[i + 1]

        tagihanPokok[i] = tagihanPokok[i + 1]
        dendaTagihan[i] = dendaTagihan[i + 1]

        nominalTerbayar[i] = nominalTerbayar[i + 1]

        statusBayar[i] = statusBayar[i + 1]

        i += 1

    i = 0

    while i < jumlahKeluhan:

        if idKeluhanPenghuni[i] == idCari:

            j = i

            while j < jumlahKeluhan - 1:

                idKeluhanPenghuni[j] = idKeluhanPenghuni[j + 1]
                isiKeluhan[j] = isiKeluhan[j + 1]

                j += 1

            jumlahKeluhan -= 1

        else:
            i += 1

    jumlahPenghuni -= 1

    print("Checkout berhasil.")

    # ==================================================


# LAPORAN
# ==================================================


def laporan():

    kamarTerisi = 0

    i = 0

    while i < jumlahKamar:

        if hitungIsiKamar(noKamar[i]) > 0:
            kamarTerisi += 1

        i += 1

    kamarKosong = jumlahKamar - kamarTerisi

    lunas = 0
    belumLunas = 0

    i = 0

    while i < jumlahPenghuni:

        if statusBayar[i] == "Lunas":
            lunas += 1
        else:
            belumLunas += 1

        i += 1

    print("\n===== LAPORAN =====")

    print(f"Total Kamar      : {jumlahKamar}")
    print(f"Kamar Terisi     : {kamarTerisi}")
    print(f"Kamar Kosong     : {kamarKosong}")

    print(f"Total Penghuni   : {jumlahPenghuni}")

    print(f"Lunas            : {lunas}")
    print(f"Belum Lunas      : {belumLunas}")

    print(f"Jumlah Keluhan   : {jumlahKeluhan}")

    print(f"Total Pendapatan : Rp{totalPendapatan}")


# ==================================================
# MENU
# ==================================================


def menu():

    print("\n===== SISTEM MANAJEMEN KOST =====")

    print("1. Tambah Kamar")
    print("2. Lihat Kamar")

    print("3. Tambah Penghuni")
    print("4. Lihat Penghuni")
    print("5. Checkout Penghuni")

    print("6. Lihat Tagihan")
    print("7. Pembayaran")

    print("8. Input Keluhan")
    print("9. Lihat Keluhan")

    print("10. Laporan")

    print("0. Keluar")


# ==================================================
# MAIN PROGRAM
# ==================================================


def main():

    pilihan = -1

    while pilihan != 0:

        menu()

        pilihan = int(input("Pilihan : "))

        if pilihan == 1:
            tambahKamar()

        elif pilihan == 2:
            lihatKamar()

        elif pilihan == 3:
            tambahPenghuni()

        elif pilihan == 4:
            lihatPenghuni()

        elif pilihan == 5:
            checkoutPenghuni()

        elif pilihan == 6:
            lihatTagihan()

        elif pilihan == 7:
            pembayaran()

        elif pilihan == 8:
            inputKeluhan()

        elif pilihan == 9:
            lihatKeluhan()

        elif pilihan == 10:
            laporan()

        elif pilihan == 0:
            print("Program selesai.")

        else:
            print("Menu tidak tersedia.")

    return 0


if __name__ == "__main__":
    main()
