from os import system, name
from time import sleep

wisata = {}
alam = {}
edukasi = {}
religi = {}
budaya = {}


class tampilan:
    def __init__():
        pass

    def utama():
        print("=====================")
        print("+       Menu        +")
        print("=====================")
        print(
            "1. Daftar Pariwisata\n2. Input Pariwisata Baru\n3. Delete Semua Pariwisata\n4. Exit"
        )
        try:
            a = int(input("Pilih Menu : "))
        except ValueError: #jika value yang dimasukkan salah
            print("Inputan harus Angka !\nSilahkan Ulangi!")
            sleep(2) #console akan tertidur selama 2 detik
            tampilan.clear() #membersihkan console
            return tampilan.utama() #kembali ke tampilan utama
        return tampilan.tampil(a)

    def tampil(a):
        if a == 1:
            print("=====================")
            print("1. Tampilkan Semua\n2. Tampilkan Berdasar Jenis")
            pil = input("Pilih : ")
            tampilan.clear()
            return next.nextamp(int(pil))
        elif a == 2:
            tampilan.clear()
            return next.nextamp(3)
        elif a == 3:
            tampilan.clear()
            return next.nextamp(4)
        elif a == 4:
            tampilan.clear()
            return None
        else:
            print("Menu tidak tersedia ! Ulangi!")
            sleep(1)
            tampilan.clear()
            return tampilan.utama()

    def tampAlam():
        print("========================")
        print("+  Daftar Wisata Alam  +")
        print("========================")
        berkas.tampAlam()

    def tampEdukasi():
        print("===========================")
        print("+  Daftar Wisata Edukasi  +")
        print("===========================")
        berkas.tampEdukasi()
    
    def tampReligi():
        print("===========================")
        print("+  Daftar Wisata Religi  +")
        print("===========================")
        berkas.tampReligi()
    
    def tampBudaya():
        print("===========================")
        print("+  Daftar Wisata Budaya  +")
        print("===========================")
        berkas.tampBudaya()

    def clear():
        """
    fungsi untuk clear shell/console
    """
        # windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


class next:
    def __init__():
        pass

    def nextamp(pil):
        if pil == 1:
            return berkas.readFile("")
        elif pil == 2:
            print(
                "Tampilkan berdasarkan Jenis : \n1. Alam\n2. Edukasi\n3. Religi\n4. Budaya\n5. Back"
            )
            try:
                nepil = int(input("Input Pilihan :"))
                if nepil == 1:
                    tampilan.clear()
                    return tampilan.tampAlam()
                elif nepil == 2:
                    tampilan.clear()
                    return tampilan.tampEdukasi()
                elif nepil == 3:
                    tampilan.clear()
                    return tampilan.tampReligi()
                elif nepil == 4:
                    tampilan.clear()
                    return tampilan.tampBudaya()
                elif nepil == 5:
                    tampilan.clear()
                    return tampilan.utama()
            except ValueError(nepil):
                print("Inputan harus Angka\nSilahkan Ulangi")
                sleep(2)
                tampilan.clear()
                return next.nextamp(2)
        elif pil == 3:
            print("========================")
            print("+ Input Berdasar Jenis +")
            print("========================")
            print("1. Alam\n2. Edukasi\n3. Religi\n4. Budaya\n5. Kembali")
            try:
                pill = int(input("Pilih : "))
                if pill == 1:
                    tampilan.clear()
                    return control.inpAlam()
                elif pill == 2:
                    tampilan.clear()
                    return control.inpEdukasi()
                elif pill == 3:
                    tampilan.clear()
                    return control.inpReligi()
                elif pill == 4:
                    tampilan.clear()
                    return control.inpBudaya()
                elif pill == 5:
                    tampilan.clear()
                    return tampilan.utama()
                else :
                    print("Menu tidak ada, Ulangi !")
                    sleep(1)
                    tampilan.clear()
                    return next.nextamp(3)
            except ValueError:
                print("Inputan harus Angka\nSilahkan Ulangi")
                sleep(1)
                tampilan.clear()
                return next.nextamp(3)
        elif pil == 4 :
              tampilan.clear()
              return control.delSemua()

class control:
    def __init__():
        pass

    def inpAlam():
        alam.clear()
        print("========================")
        print("+   Input Jenis Alam   +")
        print("========================\n")
        try:
            key = input("Masukkan nama tempat wisata   : ")
            jarak = int(input("Masukkan jarak tempat wisata  : "))
            alam[key] = jarak
            berkas.inputFileAlam()
            print("Data Berhasil Dimasukkan")
            sleep(2)
            tampilan.clear()
            return tampilan.utama()
        except ValueError(jarak):
            print("Inputan harus Angka\nSilahkan Ulangi")
            sleep(2)
            tampilan.clear()
            return control.inpAlam()

    def inpEdukasi():
        edukasi.clear()
        print("=========================")
        print("+  Input Jenis Edukasi  +")
        print("=========================\n")
        try:
            key = input("Masukkan nama tempat wisata   : ")
            jarak = int(input("Masukkan jarak tempat wisata  : "))
            edukasi[key] = jarak
            berkas.inputFileEdukasi()
            print("Data Berhasil Dimasukkan")
            sleep(2)
            tampilan.clear()
            return tampilan.utama()
        except ValueError(jarak):
            print("Inputan harus Angka\nSilahkan Ulangi")
            sleep(2)
            tampilan.clear()
            return control.inpEdukasi()

    def inpReligi():
        religi.clear()
        print("==========================")
        print("+   Input Jenis Religi   +")
        print("==========================\n")
        try:
            key = input("Masukkan nama tempat wisata   : ")
            jarak = int(input("Masukkan jarak tempat wisata  : "))
            religi[key] = jarak
            berkas.inputFileReligi()
            print("Data Berhasil Dimasukkan")
            sleep(2)
            tampilan.clear()
            return tampilan.utama()
        except ValueError(jarak):
            print("Inputan harus Angka\nSilahkan Ulangi")
            sleep(2)
            tampilan.clear()
            return control.inpReligi()

    def inpBudaya():
        budaya.clear()
        print("==========================")
        print("+   Input Jenis Budaya   +")
        print("==========================\n")
        try:
            key = input("Masukkan nama tempat wisata   : ")
            jarak = int(input("Masukkan jarak tempat wisata  : "))
            budaya[key] = jarak
            berkas.inputFileBudaya()
            print("Data Berhasil Dimasukkan")
            sleep(2)
            tampilan.clear()
            return tampilan.utama()
        except ValueError(jarak):
            print("Inputan harus Angka\nSilahkan Ulangi")
            sleep(2)
            tampilan.clear()
            return control.inpBudaya()
    
    def delSemua():
      wisata.clear()
      alam.clear()
      edukasi.clear()
      budaya.clear()
      religi.clear()
      with open('alam.txt', 'w') as data:
        data.write("")
      with open('edukasi.txt', 'w') as data:
        data.write("")
      with open('budaya.txt', 'w') as data:
        data.write("")
      with open('religi.txt', 'w') as data:
        data.write("") 

      print("Data telah dihapus ! \nkembali ke menu utama !")
      sleep(2)
      tampilan.clear()
      return tampilan.utama()
    

class berkas:
    def __init__():
      pass

    def readFile(keywords):
        with open("alam.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                wisata[key] = value
        with open("edukasi.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                wisata[key] = value
        with open("budaya.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                wisata[key] = value
        with open("religi.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                wisata[key] = value
        witas = list(wisata.items())
        urut.sortAscend(witas)
        wisatasort = dict(witas)
        print("=====================")
        print("+ Daftar Pariwisata +")
        print("=====================")
        #print data
        if len(wisata) == 0 :
          print("Data Kosong")
        else :
          i = 0
          while i < len(wisata):
            my_list = list(wisatasort.keys())
            my_listv = list(wisatasort.values())
            print("{}. {}      Jarak {} Km ".format(i + 1, my_list[i],my_listv[i]))
            i += 1
        lnjt = input("Kembali (y/n) ? ")
        return berkas.lanjut(lnjt)

    def inputFileAlam():
        with open('alam.txt', 'a') as data:
            for key, value in alam.items():
                data.write('%s    ,%s\n' % (key, value))

    def inputFileEdukasi():
        with open('edukasi.txt', 'a') as data:
            for key, value in edukasi.items():
                data.write('%s    ,%s\n' % (key, value))

    def inputFileReligi():
        with open('religi.txt', 'a') as data:
            for key, value in religi.items():
                data.write('%s    ,%s\n' % (key, value))

    def inputFileBudaya():
        with open('budaya.txt', 'a') as data:
            for key, value in budaya.items():
                data.write('%s    ,%s\n' % (key, value))

    def tampAlam():
        
        with open("alam.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                alam[key] = value

        witas = list(alam.items())
        urut.sortAscend(witas)
        ala = dict(witas)

        if len(wisata) == 0 :
          print("Data Kosong")
        else :
          i = 0
          while i < len(ala):
            my_list = list(ala.keys())
            my_listv = list(ala.values())
            print("{}. {}      Jarak {} Km ".format(i + 1, my_list[i], my_listv[i]))
            i += 1
        lnjt = input("Kembali Menu Utama (y/n) ? ")
        return berkas.lanjut(lnjt)

    def tampEdukasi():
        with open("edukasi.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                edukasi[key] = value

        witas = list(edukasi.items())
        urut.sortAscend(witas)
        edukas = dict(witas)
        if len(wisata) == 0 :
          print("Data Kosong")
        else :
          i = 0
          while i < len(edukas):
            my_list = list(edukas.keys())
            my_listv = list(edukas.values())
            print("{}. {}      Jarak {} Km ".format(i + 1, my_list[i], my_listv[i]))
            i += 1
        lnjt = input("Kembali Menu Utama (y/n) ? ")
        return berkas.lanjut(lnjt)
    
    def tampReligi():
        with open("religi.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                religi[key] = value
        
        witas = list(religi.items())
        urut.sortAscend(witas)
        relig = dict(witas)

        if len(wisata) == 0 :
          print("Data Kosong")
        else :
          i = 0
          while i < len(relig):
            my_list = list(relig.keys())
            my_listv = list(relig.values())
            print("{}. {}      Jarak {} Km ".format(i + 1, my_list[i], my_listv[i]))
            i += 1
        lnjt = input("Kembali Menu Utama (y/n) ? ")
        return berkas.lanjut(lnjt)
    
    def tampBudaya():
        with open("budaya.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                budaya[key] = value
        
        witas = list(budaya.items())
        urut.sortAscend(witas)
        buday = dict(witas)
        
        if len(wisata) == 0 :
          print("Data Kosong")
        else :
          i = 0
          while i < len(buday):
            my_list = list(buday.keys())
            my_listv = list(buday.values())
            print("{}. {}      Jarak {} Km ".format(i + 1, my_list[i], my_listv[i]))
            i += 1
        lnjt = input("Kembali Menu Utama (y/n) ? ")
        return berkas.lanjut(lnjt)

    def lanjut(lnjt):
        if lnjt.lower() in ['y']:
            tampilan.clear()
            return tampilan.utama()
        elif lnjt.lower() in ['n']:
            print("Exit !")
            sleep(2)
            tampilan.clear()
            return None


class urut:
    def __init__():
      pass

    def sortAscend(my_list):
        for j in range(len(my_list) - 1):
            for i in range(len(my_list) - 1 - j):
                if my_list[i] > my_list[i + 1]:
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        return my_list 
