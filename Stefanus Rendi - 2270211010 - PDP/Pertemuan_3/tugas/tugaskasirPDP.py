print("========== SUN CAFE & EATERY ===========")

print("=========Final Project Kasir========")
print("=============RAWRRRRRR=========")

import time

tanggal = time.strftime (" %d-%m-%y - %H:%M:%S ")
print(tanggal)
print(type(tanggal))

Nama_Customer=str(input("Masukkan Nama Customer: "))
Alamat=str(input("Alamat : "))
No_Handphone=str(input("Masukan nomor Handphone anda: "))

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. French Fries  - Rp 15000")
   print("2. Cireng Goreng - Rp 9000")
   print("3. Bakmi Ayam - Rp 18000")
   print("4. Bakmi Ayam Special - Rp 25000")
   print("5. Bihun Ayam - Rp 18000")
   print("6. Bihun Ayam Special - Rp 25000")
   print("7. Nasi Goreng Ayam - Rp 18000")
   print("8. Nasi Goreng Ayam Special - Rp 25000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," French Fries = Rp", totalmkn)
       mkn=("French Fries")
   elif nomor==2:
       totalmkn=porsi*9000
       print (porsi," Cireng Goreng = Rp", totalmkn)
       mkn=("Cireng Goreng")
   elif nomor==3:
       totalmkn=porsi*18000
       print (porsi, " Bakmi Ayam = Rp", totalmkn)
       mkn=("Bakmi Ayam")
   elif nomor==4:
       totalmkn=porsi*25000
       print (porsi, " Bakmi Ayam Special = Rp", totalmkn)
       mkn=("Bakmi Ayam Special")
   elif nomor==5:
       totalmkn=porsi*18000
       print (porsi, " Bihun Ayam = Rp", totalmkn)
       mkn=("Bihun Ayam")
   elif nomor==6:
       totalmkn=porsi*25000
       print (porsi, " Bihun Ayam Special = Rp", totalmkn)
       mkn=("Bihun Ayam Special")      
   elif nomor==7:
       totalmkn=porsi*18000
       print (porsi, " Nasi Goreng Ayam = Rp", totalmkn)
       mkn=("Nasi Goreng Ayam")
   elif nomor==8:
       totalmkn=porsi*25000
       print (porsi, " Nasi Goreng Ayam Special = Rp", totalmkn)
       mkn=("Nasi Goreng Ayam Special")    
   else:
      print("Pilih Yang Bener Dong Cuyy!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Cafe latte - Rp 22000")
   print("2. Americano - Rp 15000")
   print("3. Caramel Macchiato - Rp 25000")
   print("4. Pandan Latte - Rp 20000")
   print("5. Milk Tea - Rp 15000")
   print("6. Thai Tea - Rp 17000")
   print("7. Lychee Tea - Rp 17000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*22000
       print (gelas," Cafe Latte = Rp", totalmnm)
       mnm=(" Cafe Latte")
   elif nomor==2:
       totalmnm=gelas*15000
       print (gelas, " Americano = Rp", totalmnm)
       mnm=("Americano")
   elif nomor==3:
       totalmnm=gelas*25000
       print (gelas, " Caramel Macchiato = Rp", totalmnm)
       mnm=("Caramel Macchiato")
   elif nomor==4:
        totalmnm=gelas*20000
        print(gelas, "Pandan Latte = Rp", totalmnm) 
        mnm=("Pandan Latte")   
   elif nomor==5:
        totalmnm=gelas*15000
        print(gelas, "Milk Tea = Rp", totalmnm) 
        mnm=("Milk Tea")
   elif nomor==6:
        totalmnm=gelas*17000
        print(gelas, "Thai Tea = Rp", totalmnm) 
        mnm=("Thai Tea")
   elif nomor==7:
        totalmnm=gelas*17000
        print(gelas, "Lychee Tea = Rp", totalmnm) 
        mnm=("Lyche Tea")                    
   else:
      print("Pilih Yang Bener Dong Cuyyy!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n===============================================")
print("========== S U N C A F E & E A T E R Y ==========")
print("=============== Jatimekar ========================")

print("Tanggal\t        :",tanggal)
print ("Nama\t\t:",Nama_Customer)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("Alamat\t        :", Alamat)
print("No Handphone\t:", No_Handphone)
print("=================== S U N ===================")
print("========== THANK YOU & VISIT AGAIN ==========")
print("===============================================")