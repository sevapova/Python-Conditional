
password = input("Parolni kiriting: ")

if len(password) >= 8 and password.isalpha() and password.isdigit():
    print("qabul qilindi")

else:
    print("Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak.")