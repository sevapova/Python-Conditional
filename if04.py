
ticket = 100

age = int(input("Yoshingizni kiriting: "))

if age < 7 :
    ticket *= 0.5


if age >= 7 and age <= 17:
    ticket *= 0.8


if age > 60 :
    ticket *= 0.7


print("Bilet narxi: ",ticket)
