# input user

# data yang dimasukan pasti string
data = input("Masukan data:12")

print("data = ",data,",type =",type(data))

# jika kita ingin mengambil int, maka
angka = float(input("masukan angka: "))
angka = int(input("masukan angka: "))
print("data = ",angka,",type =",type(angka))

# bagaimana dengan boolean
biner = bool(int(input("masukan nilai boolean: ")))
print("data = ",biner,",type =",type(biner))