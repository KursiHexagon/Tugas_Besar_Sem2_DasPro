def Laporan():
    # Sementara
    print("--- LAPORAN SISTEM ---")
    print(f"Total Kamar Terdaftar : {len(kamar)}")
    print(f"Total Penghuni Aktif  : {totalPenghuni}")
    print(f"Total Transaksi       : {totalPembayaran}")
    print(f"Total Keluhan         : {totalKeluhan}")
    print("-" * 22)


def MDKn():
    global keluhan
    global totalKeluhan

    while True:
        choice = str(input("Apakah kamu ingin melihat list keluhan? (Y/n): "))

        if choice.upper() == "Y":
            print("--- LIST KELUHAN ---")
            print(f"{'No. Kamar':<10} | {'Tanggal':<10} | {'Bulan':<10} | {'Tahun':<10} | {'Deskripsi Keluhan':<30} | {'Status':<10}")
            print('-' * 85) 

            for i in range(totalKeluhan):
                print(f"{keluhan[i][0]:<10} | {keluhan[i][1]:<10} | {keluhan[i][2]:<10} | {keluhan[i][3]:<10} | {keluhan[i][4]:<30} | {keluhan[i][5]:<10}")
        
        else:
            inputKeluhan = str(input("Apakah kamu ingin menambahkan list keluhan? (Y/n): "))

            if inputKeluhan.upper() == "Y":
                keluhan += [None]
                keluhan[totalKeluhan] = [None] * 6

                keluhan[totalKeluhan][0] = str(input("No. Kamar: "))
                keluhan[totalKeluhan][1] = str(input('Tanggal (DD): '))
                keluhan[totalKeluhan][2] = str(input('Bulan (MM): '))
                keluhan[totalKeluhan][3] = str(input('Tahun (YYYY): '))    
                keluhan[totalKeluhan][4] = str(input("Deskripsi Masalah: "))
                keluhan[totalKeluhan][5] = str(input("Status (Resolved / WIP): "))

                totalKeluhan += 1
                print("-"*6, "DATA KELUHAN BERHASIL MASUK KE SISTEM", "-" * 6)   
         
        finishChoice = input("Keluar dari menu keluhan? (Y/n): ")
        if finishChoice.upper() == "Y":
            break


def MDPn():    
    global penghuni
    global pembayaran 
    global totalPembayaran

    while True:
        choice = str(input("Apakah kamu ingin menambahkan list pembayaran? (Y/n): "))

        while choice.upper() == "Y":
            pList = str(input("Apakah kamu ingin lihat list penghuni terlebih dahulu? (Y/n): "))

            if pList.upper() == "Y":
                print("--- LIST PENGHUNI ---")
                print(f"{'ID':<3} | {'Nama':<10} | {'NIK':<20} | {'No Telepon':<15} | {'Tanggal Masuk':<13} | {'Bulan Masuk':<11} | {'Tahun Masuk':<11} | {'Jenis Sewa':<10} | {'No. Kamar':<2}")
                print('-' * 115) 

                for i in range(totalPenghuni):
                    print(f"{penghuni[i][0]:<3} | {penghuni[i][1]:<10} | {penghuni[i][2]:<20} | {penghuni[i][3]:<15} | {penghuni[i][4]:<13} | {penghuni[i][5]:<11} | {penghuni[i][6]:<11} | {penghuni[i][7]:<10} | {penghuni[i][8]:<2}")
            else:
                pembayaran += [None]
                pembayaran[totalPembayaran] = [None] * 6

                pembayaran[totalPembayaran][0] = int(input("Masukkan ID penghuni: "))
                pembayaran[totalPembayaran][1] = str(input('Masukkan tanggal masuk (DD): '))
                pembayaran[totalPembayaran][2] = str(input('Masukkan bulan masuk (MM/Nama Bulan): '))
                pembayaran[totalPembayaran][3] = str(input('Masukkan tahun masuk (YYYY): '))
                pembayaran[totalPembayaran][4] = str(input("Jenis Pembayaran (Cash/Transfer): "))
                pembayaran[totalPembayaran][5] = int(input("Nominal Pembayaran: "))

                totalPembayaran += 1
                print("-" * 6, "DATA PEMBAYARAN BERHASIL MASUK KE SISTEM", "-" * 6)
            
            choice = str(input("Apakah kamu ingin menambahkan list pembayaran? (Y/n): "))

        print("-" * 6, "FIELD INPUT PENGHUNI DITUTUP", "-" * 6)
        break


def MDPi():
    global penghuni
    global kamar
    global totalPenghuni

    while True:

        choice = str(input("Apakah kamu ingin lihat list penghuni sekarang? (Y/n): "))

        if choice.upper() == "Y":
            print("--- LIST PENGHUNI ---")
            print(f"{'ID':<3} | {'Nama':<10} | {'NIK':<20} | {'No Telepon':<15} | {'Tanggal Masuk':<13} | {'Bulan Masuk':<11} | {'Tahun Masuk':<11} | {'Jenis Sewa':<10} | {'No. Kamar':<2}")
            print('-' * 115) 

            for i in range(totalPenghuni):
                print(f"{penghuni[i][0]:<3} | {penghuni[i][1]:<10} | {penghuni[i][2]:<20} | {penghuni[i][3]:<15} | {penghuni[i][4]:<13} | {penghuni[i][5]:<11} | {penghuni[i][6]:<11} | {penghuni[i][7]:<10} | {penghuni[i][8]:<2}")

        else:
            inputPenghuni = str(input("Apakah kamu ingin menambahkan penghuni baru? (Y/n): "))

            # Input Penghuni
            while inputPenghuni.upper() == "Y":
                penghuni += [None]
                penghuni[totalPenghuni] = [None] * 9

                penghuni[totalPenghuni][0] = (totalPenghuni + 1)
                penghuni[totalPenghuni][1] = str(input('Masukkan nama penghuni: '))
                penghuni[totalPenghuni][2] = int(input('Masukkan NIK penghuni: '))
                penghuni[totalPenghuni][3] = int(input('Masukkan no telepon penghuni: '))
                penghuni[totalPenghuni][4] = str(input('Masukkan tanggal masuk (DD): '))
                penghuni[totalPenghuni][5] = str(input('Masukkan bulan masuk (MM/Nama Bulan): '))
                penghuni[totalPenghuni][6] = str(input('Masukkan tahun masuk (YYYY): '))
                penghuni[totalPenghuni][7] = str(input('Masukkan jenis sewa penghuni (bulanan/tahunan): '))
                penghuni[totalPenghuni][8] = int(input('Masukkan no. kamar penghuni: '))

                totalPenghuni += 1
                print("-" * 6, "DATA PENGHUNI BERHASIL MASUK KE SISTEM", "-" * 6)

                inputPenghuni = str(input("Apakah kamu ingin menambahkan penghuni baru? (Y/n): "))
                
        finishChoice = input("Keluar dari menu penghuni? (Y/n): ")
        if finishChoice.upper() == "Y":
            print("-" * 6, "FIELD INPUT PENGHUNI DITUTUP", "-" * 6)
            break

def MDKr():
    global kamar

    while True:
        while True:
            choice = str(input("Apakah kamu ingin lihat list kamar sekarang? (Y/n): ")).strip()
            if choice == "":
                print("ERROR: Input tidak boleh kosong! Silakan masukkan 'Y' atau 'n'.")
            elif choice.upper() == "Y" or choice.upper() == "N":
                break
            else:
                print("ERROR: Pilihan tidak valid! Harap masukkan 'Y' atau 'n'.")

        if choice.upper() == "Y":
            print("================== LIST KAMAR ==================")
            print(f"{'Nomor Kamar':<15} | {'Status Ketersediaan':<20}")
            print("-" * 48)
            if kamar == []:
                print(f"{'(Belum ada kamar yang terdaftar)'}")
            for data in kamar:
                print(f"Kamar {data['no']:<9} | {data['status']:<20}")
            print("================================================")
            
            while True:
                finishChoice = input("Keluar dari input kamar sekarang?(Ketik 'Y' untuk keluar, atau Enter untuk lanjut): ").strip()
                if finishChoice == "" or finishChoice.upper() == "Y":
                    break
                else:
                    print("ERROR: Input tidak valid! Tekan Enter langsung atau ketik 'Y'.")
            
            if finishChoice.upper() == "Y":
                break
            
        while True:
            inputKamar = str(input("Apakah kamu ingin menambahkan kamar baru? (Y/n): ")).strip()
            
            # error handling 
            if inputKamar == "":
                print("ERROR: Input tidak boleh kosong! Silakan masukkan 'Y' atau 'n'.")
            elif inputKamar.upper() == "Y" or inputKamar.upper() == "N":
                break
            else:
                print("ERROR: Pilihan tidak valid! Harap masukkan 'Y' atau 'n'.")
        

        while inputKamar.upper() == "Y":
            while True:
                raw_noKamar = input("-> Masukkan nomor kamar: ")
                
                # error handling 
                if raw_noKamar == "":
                    print("ERROR: Nomor kamar tidak boleh kosong!")
                    continue
                
                if raw_noKamar.isdigit():
                    noKamar = int(raw_noKamar)
                    
                    # check apakah no kamar sudah ada
                    if any(data['no'] == noKamar for data in kamar):
                        print("WARNING: No kamar sudah ada! Silakan masukkan nomor lain.")
                    else:
                        break
                else:
                    print("ERROR: Input salah! Harap masukkan nomor kamar berupa angka asli (contoh: 101).")
    
            statusKamar = "Available"
            newData = {"no": noKamar, "status": statusKamar}
            kamar += [newData]

            print("=" * 49)
            print(f"{' DATA KAMAR BERHASIL MASUK KE SISTEM ':^49}")
            print("=" * 49)
            print(f"Nomor Kamar : {noKamar}")
            print(f"Status      : {statusKamar}")
            print("=" * 49)

            while True:
                inputKamar = str(input(" Apakah kamu ingin input kamar baru lagi? (Y/n): "))
                if inputKamar == "":
                    print("ERROR: Input tidak boleh kosong!")
                elif inputKamar.upper() == "Y" or inputKamar.upper() == "N":
                    break
                else:
                    print("ERROR: Pilihan tidak valid! Harap masukkan 'Y' atau 'n'.")
        
        while True:
            finishChoice = input("Keluar dari input kamar sekarang? (Ketik 'Y' untuk keluar, atau Enter untuk lanjut): ")
            if finishChoice == "" or finishChoice.upper() == "Y":
                break
            else:
                print("ERROR: Input tidak valid! Tekan Enter langsung atau ketik 'Y'")
                
        if finishChoice.upper() == "Y":
            break

    return

def usrChoiceProc(uc):
    if uc == 1:
        MDKr()
    elif uc == 2:
        MDPi()
    elif uc == 3:
        MDPn()
    elif uc == 4:
        MDKn()
    elif uc == 5:
        Laporan()
    else:
        return


def menu():
    menuList = ["Input Data Kamar", "Input Data Penghuni", "Input Pembayaran", "Input Keluhan", "Lihat Laporan"]
    
    for i in range(5):
        print((i+1), menuList[i])

def userNameInput():
    UserName = str(input("Siapa nama anda? "))
    return UserName

def main():
    usn = userNameInput()

    print("=" * 10, end="")
    print(f" WELCOME {usn} ", end="")
    print("=" * 10, end="")
    print()

    while True:
        print("Apa yang ingin kita lakukan hari ini?")
        print("=== Menu yang tersedia ===")
        menu()    


        usrChoice = int(input("Masukkan angka 1-5: ")) 
        while usrChoice < 1 or usrChoice > 5 or usrChoice == "" :
            print("=" * 60)
            print("Maaf, namun menu yang tersedia hanyalah 1-5")
            usrChoice = int(input("Masukkan angka 1-5: "))
        
        usrChoiceProc(usrChoice)



if __name__ == '__main__':
    kamar = []
    penghuni = []
    pembayaran = []
    keluhan = []
    totalPenghuni = totalPembayaran = totalKeluhan = 0
    
    main()