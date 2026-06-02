
def menu():
    menuList = ["Data Kamar", "Data Penghuni", "Pembayaran", "Keluhan", "Laporan"]
    
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
        #usrChoiceProc(usrChoice)



if __name__ == '__main__':
    main()