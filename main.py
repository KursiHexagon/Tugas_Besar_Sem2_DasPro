def Laporan():

def MDKn():

def MDPn():    

def MDPi():

def MDKr():
    global kamar

    while True:
        choice = str(input("Apakah kamu ingin lihat list kamar sekarang? (Y/n): "))

        if choice.upper() == "Y":
            print("\n--- LIST KAMAR ---")
            for data in kamar:
                print(f"Nomor Kamar: {data['no']}, Status: {data['status']}")
            print("-" * 18)
        else:   
            inputKamar = str(input("Apakah kamu ingin input kamar baru? (Y/n): "))
            
            while inputKamar.upper() == "Y":
                while True:
                    noKamar = int(input("Masukkan nomor kamar: "))
                    
                    if any(data['no'] == noKamar for data in kamar):
                        print("No kamar sudah ada! Silakan masukkan nomor lain.")
                    else:
                        break 
    
                statusKamar = "Available"

                newData = {"no": noKamar, "status": statusKamar}
                kamar += [newData]

                print("\n" + "=" * 6, "DATA KAMAR BERHASIL MASUK KE SISTEM", "=" * 6)
                print(f"No Kamar - {noKamar}, status - {statusKamar}")

                inputKamar = str(input("Apakah kamu ingin input kamar baru? (Y/n): "))
            
        finishChoice = input("Keluar dari input kamar sekarang? (Ketik 'Y' untuk keluar, atau Enter untuk lanjut) ")
        if finishChoice.upper() == "Y" or finishChoice == "":
            break
        else:
            continue                
        

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
    main()

    kamar = []