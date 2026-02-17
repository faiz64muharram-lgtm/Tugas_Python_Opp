from abc import ABC,abstractmethod
import time

class Laundry(ABC):
    def __init__(self,harga_per_kg):
        self.__harga_per_kg = harga_per_kg
    

    @abstractmethod

    def hitung_harga(self,berat) -> int :
        pass

    def per_kg(self) -> int :
        return self.__harga_per_kg
    
class Paket_biasa(Laundry):
    def __init__(self):
        super().__init__(20000)

    def hitung_harga(self, berat):
        return berat * self.per_kg()
    
class Paket_express(Laundry):
    def __init__(self):
        super().__init__(40000)

    def hitung_harga(self, berat):
        return berat * self.per_kg()
    

#Orderan


class Orderan_Laundry:
    def __init__(self, nama:str,berat:int,layanan:Laundry):
        self.nama = nama
        self.berat = berat
        self.layanan = layanan
        self.__status = "Diterima"
        self.waktu_skrg = time.time()
        pass

    @property

    def status(self) -> str :
        self.update_status()
        return self.__status

    def update_status(self):

        waktu_skrg = time.time()

        if waktu_skrg >= 20 :
            self.__status ="Diterima"

        else :
            self.__status ="Masih Dicuci"

    def biaya(self) :
         return self.layanan.hitung_harga(self.berat)
    
    def tampilan(self):
        print("\n=== DATA LAUNDRY ===")
        print(f"Nama Santri:{self.nama}")
        print(f"Berat kg :{self.berat}")
        print(f"Status:{self.status}")
        print(f"Total Biaya: RP {self.biaya()}")

   
   #Menu Utama

def layanan_laundry():
    print("\n Pilih Layanan :")
    print("(1. Paket Biasa (20.000/KG)")
    print("(2. Paket Express (40.000/KG)")

    while True:
        pilihan = input("Pilih (1,2):")

        if pilihan == "1":
            return Paket_biasa()
    
        elif pilihan == "2":
            return Paket_express()
        else:
            print("❌ Pilihan Gak Ada")


def main():

    menu=[]

    while True:
        print("\nMENU :")
        print("(1.Input Order")
        print("(2.Lihat Orderan")
        print("(3.Keluar")

        pilihan =input("Pilih Menu:")

        if pilihan == "1":
           nama = input("Nama Santri:")

           try :
               berat = float(input("Berat kg:"))
   
           except TypeError:
               print("Permintaan Tidak Difahami")
   
               continue
   
           layanan = layanan_laundry()
   
           order = Orderan_Laundry(nama,berat,layanan)
   
           menu.append(order)
   
           print("✅ Orderan Berhasil")
        

        elif pilihan == "2":
            if not menu:
                print("Belom Ada Orderan")

            for order in menu:
                order.tampilan()

        elif pilihan == "3":
            print("Terima Kasih")

            break
        else:
            print("Mau Apa LU !")


if __name__ == "__main__":
     main()



    



        


        
    

    
       
           











        


        





    
