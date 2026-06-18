==================== KAMUS DATA ====================

----------------------------------------------------------------------
FUNCTION main
----------------------------------------------------------------------
TUJUAN   : Fungsi utama program — menginisialisasi tanggal sistem awal,
           lalu menjalankan loop menu utama sampai user memilih keluar (0)
GLOBAL   : tanggalSekarang, bulanSekarang, tahunSekarang (diisi saat inisialisasi)
VARIABEL :
1. pilihan = var. penampung pilihan menu dari user, default -1 (int)

----------------------------------------------------------------------
FUNCTION menu

TUJUAN   : Menampilkan menu utama program beserta tanggal sistem saat ini
VARIABEL : (tidak ada variabel lokal — hanya membaca global tanggalSekarang,
            bulanSekarang, tahunSekarang untuk ditampilkan di header menu)

----------------------------------------------------------------------
FUNCTION cariIndexKamar

TUJUAN    : Mencari index posisi kamar dalam array berdasarkan nomor kamar
PARAMETER : no = nomor kamar yang dicari (int)
RETURN    : index posisi kamar (int), atau -1 jika tidak ditemukan (int)
VARIABEL  :
1. i = var. penghitung iterasi (int)

----------------------------------------------------------------------
FUNCTION hitungIsiKamar

TUJUAN    : Menghitung jumlah penghuni aktif yang menempati kamar dengan nomor tertentu
PARAMETER : no = nomor kamar yang ingin dicek (int)
RETURN    : jumlah penghuni yang menempati kamar tersebut (int)
VARIABEL  :
1. jumlah = var. penghitung hasil (int)
2. i      = var. penghitung iterasi (int)

----------------------------------------------------------------------
FUNCTION cariIndexPenghuni

TUJUAN    : Mencari index posisi penghuni dalam array berdasarkan ID penghuni
PARAMETER : idCari = ID penghuni yang dicari (int)
RETURN    : index posisi penghuni (int), atau -1 jika tidak ditemukan (int)
VARIABEL  :
1. i = var. penghitung iterasi (int)

----------------------------------------------------------------------
FUNCTION hitungSelisihHari

TUJUAN    : Menghitung selisih hari antara dua tanggal (Tanggal1 - Tanggal2)
            dengan asumsi 1 bulan = 30 hari dan 1 tahun = 360 hari
PARAMETER : tgl1, bln1, thn1 = tanggal pertama (int, int, int)
            tgl2, bln2, thn2 = tanggal kedua (int, int, int)
RETURN    : selisih hari antara dua tanggal (int), positif jika Tanggal1 > Tanggal2
VARIABEL  :
1. totalHari1 = var. konversi tanggal pertama ke total hari (int)
2. totalHari2 = var. konversi tanggal kedua ke total hari (int)

----------------------------------------------------------------------
FUNCTION generateTagihanBaru

TUJUAN    : Mereset dan membuat tagihan baru untuk penghuni di awal periode sewa berikutnya
PARAMETER : idx = index posisi penghuni dalam array (int)
VARIABEL  :
1. nomor    = var. penampung nomor kamar penghuni (int)
2. idxKamar = var. index posisi kamar dalam array (int)

----------------------------------------------------------------------
FUNCTION tambahKamar

TUJUAN   : Menambahkan data kamar baru ke dalam sistem
GLOBAL   : jumlahKamar (diperbarui setelah kamar ditambahkan)
VARIABEL :
1. no         = var. nomor kamar yang diinput user (int)
2. hargaBulan = var. harga sewa kamar per bulan (int)
3. hargaTahun = var. harga sewa kamar per tahun (int)

----------------------------------------------------------------------
FUNCTION lihatKamar

TUJUAN   : Menampilkan seluruh daftar kamar beserta info harga dan jumlah penghuni
VARIABEL :
1. i   = var. penghitung iterasi (int)
2. isi = var. penampung jumlah penghuni per kamar dari hitungIsiKamar (int)

----------------------------------------------------------------------
FUNCTION tambahPenghuni

TUJUAN   : Menambahkan data penghuni baru ke sistem beserta pembayaran DP awal (min. 50%)
GLOBAL   : jumlahPenghuni, nextId, totalPendapatan (semua diperbarui)
VARIABEL :
1.  nama         = var. input nama penghuni baru (string)
2.  kamar        = var. input nomor kamar yang dipilih (int)
3.  idxKamar     = var. index posisi kamar dalam array (int)
4.  pilih        = var. input pilihan jenis sewa 1=Bulanan / 2=Tahunan (int)
5.  tanggal      = var. input tanggal masuk penghuni (int)
6.  bulan        = var. input bulan masuk penghuni (int)
7.  tahun        = var. input tahun masuk penghuni (int)
8.  tempoTanggal = var. tanggal jatuh tempo sewa (int)
9.  tempoBulan   = var. bulan jatuh tempo sewa (int)
10. tempoTahun   = var. tahun jatuh tempo sewa (int)
11. sewa         = var. jenis sewa "Bulanan" / "Tahunan" (string)
12. tagihan      = var. nominal tagihan pokok sesuai jenis sewa (int)
13. minimalDP    = var. batas minimal DP (50% dari tagihan) (int)
14. dp           = var. input nominal DP yang dibayarkan penghuni (int)

----------------------------------------------------------------------
FUNCTION lihatPenghuni

TUJUAN   : Menampilkan seluruh daftar penghuni aktif beserta info kamar, jenis sewa,
           tanggal jatuh tempo, dan status pembayaran
VARIABEL :
1. i = var. penghitung iterasi (int)

----------------------------------------------------------------------
FUNCTION kelolaTamu

TUJUAN   : Mencatat tamu yang menginap bersama penghuni dan mengakumulasikan
           biaya tamu (Rp50.000 per tamu per hari) ke tagihan penghuni
VARIABEL :
1. idCari             = var. input ID penghuni yang dituju (int)
2. idx                = var. index posisi penghuni dalam array (int)
3. tamu               = var. input jumlah tamu baru yang menginap (int)
4. hari               = var. input lama tamu menginap dalam hari (int)
5. biayaKedatanganSkg = var. biaya tamu dari kedatangan kali ini saja (int)

----------------------------------------------------------------------
FUNCTION updateDendaRealtime

TUJUAN    : Menghitung dan memperbarui nilai denda keterlambatan pembayaran
            berdasarkan selisih hari antara tanggal sistem dan jatuh tempo (Rp10.000/hari)
PARAMETER : idx = index posisi penghuni dalam array (int)
VARIABEL  :
1. lewatHari = var. penampung hasil selisih hari, positif = terlambat (int)

----------------------------------------------------------------------
FUNCTION lihatTagihan

TUJUAN   : Menampilkan rincian tagihan real-time penghuni termasuk denda,
           biaya tamu, sisa tagihan, dan status pembayaran terkini
VARIABEL :
1. idCari       = var. input ID penghuni yang dituju (int)
2. idx          = var. index posisi penghuni dalam array (int)
3. biayaTamu    = var. penampung total akumulasi biaya tamu (int)
4. totalTagihan = var. total tagihan (pokok + denda + biaya tamu) (int)
5. sisaTagihan  = var. sisa yang belum dibayarkan (int)

----------------------------------------------------------------------
FUNCTION ubahTanggal

TUJUAN   : Mensimulasikan perubahan waktu sistem, sekaligus mengecek otomatis
           apakah ada penghuni yang jatuh tempo dan perlu periode tagihan baru
GLOBAL   : tanggalSekarang, bulanSekarang, tahunSekarang (semua diperbarui)
VARIABEL :
1. tanggal   = var. input tanggal baru sistem (int)
2. bulan     = var. input bulan baru sistem (int)
3. tahun     = var. input tahun baru sistem (int)
4. i         = var. penghitung iterasi penghuni (int)
5. lewatHari = var. penampung selisih hari untuk cek jatuh tempo (int)

----------------------------------------------------------------------
FUNCTION pembayaran

TUJUAN   : Memproses pembayaran tagihan penghuni, menghitung kembalian jika
           membayar lebih, dan mereset biaya tamu setelah tagihan lunas
GLOBAL   : totalPendapatan (diperbarui setiap ada pembayaran)
VARIABEL :
1. idCari       = var. input ID penghuni yang dituju (int)
2. idx          = var. index posisi penghuni dalam array (int)
3. biayaTamu    = var. penampung total akumulasi biaya tamu (int)
4. totalTagihan = var. total tagihan (pokok + denda + biaya tamu) (int)
5. sisaTagihan  = var. sisa tagihan yang belum dibayar (int)
6. bayar        = var. input nominal pembayaran dari penghuni (int)
7. wajibBayar   = var. nominal yang benar-benar wajib dibayar tanpa kelebihan (int)
8. kelebihan    = var. nominal kembalian jika bayar melebihi tagihan (int)

----------------------------------------------------------------------
FUNCTION checkoutPenghuni

TUJUAN   : Memproses checkout penghuni — menghapus data dari sistem dengan cara
           menggeser array, hanya bisa dilakukan jika tagihan sudah lunas
GLOBAL   : jumlahPenghuni (dikurangi 1 setelah checkout berhasil)
VARIABEL :
1. idCari       = var. input ID penghuni yang akan checkout (int)
2. idx          = var. index posisi penghuni dalam array (int)
3. biayaTamu    = var. penampung total akumulasi biaya tamu (int)
4. totalTagihan = var. total tagihan yang harus dilunasi sebelum checkout (int)
5. i            = var. penghitung iterasi penggeseran array (int)

----------------------------------------------------------------------
FUNCTION inputKeluhan

TUJUAN   : Mencatat keluhan baru dari penghuni ke dalam sistem dengan status awal
           "Belum Selesai"
GLOBAL   : jumlahKeluhan (ditambah 1 setelah keluhan dicatat)
VARIABEL :
1. idCari  = var. input ID penghuni yang mengajukan keluhan (int)
2. idx     = var. index posisi penghuni dalam array (int)
3. keluhan = var. input isi/teks keluhan dari penghuni (string)

----------------------------------------------------------------------
FUNCTION lihatKeluhan

TUJUAN   : Menampilkan seluruh daftar keluhan beserta ID penghuni pelapor,
           isi keluhan, dan status penanganan
VARIABEL :
1. i = var. penghitung iterasi (int)

----------------------------------------------------------------------
FUNCTION updateStatusKeluhan

TUJUAN   : Memperbarui status keluhan dari "Belum Selesai" menjadi "Selesai"
           berdasarkan nomor urut keluhan dalam daftar
VARIABEL :
1. noKeluhan  = var. input nomor urut keluhan yang ingin diupdate (int)
2. idx        = var. index posisi keluhan dalam array (noKeluhan - 1) (int)
3. konfirmasi = var. input konfirmasi user sebelum update status (string)

----------------------------------------------------------------------
FUNCTION laporan

TUJUAN   : Menampilkan laporan ringkasan sistem meliputi statistik kamar,
           status pembayaran penghuni, dan total pendapatan kas kost
NOTE     : Hanya membaca variabel global jumlahKamar, jumlahPenghuni, totalPendapatan
VARIABEL :
1. kamarTerisi = var. penghitung jumlah kamar yang sedang ditempati (int)
2. lunas       = var. penghitung penghuni dengan status "Lunas" (int)
3. belumLunas  = var. penghitung penghuni dengan status "Belum Lunas" (int)
4. i           = var. penghitung iterasi (int)
