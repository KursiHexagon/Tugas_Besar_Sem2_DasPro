========================= KAMUS DATA =========================

FUNCTION MAIN:
1. usn = var. penampung username dari function userNameInput (string)
2. usrChoice = var. input pilihan menu user (int) 

FUNCTION userNameInput:
1. UserName = var. input nama pengguna (string)

FUNCTION menu:
1. menuList = array penampung menu (array of string)

FUNCTION useChoiceProc:
1. uc = var. parameter (integer)

FUNCTION MDKr (MANAJEMEN DATA KAMAR):
1. kamar = var. global array penampung data kamar (array of dict)
2. choice = var. input pilihan user untuk lihat list kamar (string)
3. inputKamar = var. input pilihan user untuk menambah kamar baru (string)
4. raw_noKamar = var. input nomor kamar sebelum dikonversi (string)
5. noKamar = var. nomor kamar yang sudah divalidasi (int)
6. statusKamar = var. status ketersediaan kamar, default "Available" (string)
7. newData = var. dict data kamar baru sebelum dimasukkan ke array kamar (dict)
8. finishChoice = var. input pilihan user untuk keluar dari menu kamar (string)

FUNCTION MDPi (MANAJEMEN DATA PENGHUNI):
1. penghuni = var. global array penampung data penghuni (array of array)
2. kamar = var. global array penampung data kamar (array of dict)
3. totalPenghuni = var. global penghitung jumlah penghuni terdaftar (int)
4. choice = var. input pilihan user untuk lihat list penghuni (string)
5. inputPenghuni = var. input pilihan user untuk menambah penghuni baru (string)
6. finishChoice = var. input pilihan user untuk keluar dari menu penghuni (string)

FUNCTION MDPn (MANAJEMEN DATA PEMBAYARAN):
1. penghuni = var. global array penampung data penghuni (array of array)
2. pembayaran = var. global array penampung data pembayaran (array of array)
3. totalPembayaran = var. global penghitung jumlah transaksi pembayaran (int)
4. choice = var. input pilihan user untuk menambah pembayaran (string)
5. pList = var. input pilihan user untuk lihat list penghuni terlebih dahulu (string)

FUNCTION MDKn (MANAJEMEN DATA KELUHAN):
1. keluhan = var. global array penampung data keluhan (array of array)
2. totalKeluhan = var. global penghitung jumlah keluhan terdaftar (int)
3. choice = var. input pilihan user untuk lihat list keluhan (string)
4. inputKeluhan = var. input pilihan user untuk menambah keluhan baru (string)
5. finishChoice = var. input pilihan user untuk keluar dari menu keluhan (string)

FUNCTION Laporan:
1. (Tidak ada variabel lokal — hanya membaca variabel global: kamar, totalPenghuni, totalPembayaran, totalKeluhan)
2. NOTE: NANTI DIKEMBANGKAN