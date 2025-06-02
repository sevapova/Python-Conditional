
import os

f_nomi = input("Fayl nomini kiriting: ")

if os.path.exists(f_nomi):
    print("Fayl mavjud")

else :
    print("Fayl mavjud emas")