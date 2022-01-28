ogrenciAdSoyad = str(input("Ad Soyad : "))
vizeNotu = int(input("Vize notu gir : "))
finalNotu = int(input("Final notu gir :"))

ortalamaNot = (0.4 * vizeNotu) + (0.6 * finalNotu)  # Vize notunun %40 ve Final puanının %60 ını hesaplayalım .

print("Öğrencinin Adı Soyadı : " + ogrenciAdSoyad)
print("Not ortalamanız : ", ortalamaNot)

a = ortalamaNot >= 50  # Döngü kısmına bir de final notunun 50'den büyük olmasını şart koşalım.
b = ortalamaNot <= 50  # Döngü kısmına bir de final notunun 50'den küçük olmasını şart koşalım.

while a:
        bütNotu = finalNotu
        bortalamaNot = (0.4 * vizeNotu) + (0.6 * bütNotu)
        if ortalamaNot >= 90:
            harfNotu= "Harf Notunuz AA Geçtiniz"
            print("Harf Notunuz AA")
            break
        elif ortalamaNot >= 85 and ortalamaNot < 90:
            harfNotu = "Harf Notunuz BA Geçtiniz"
            print("Harf Notunuz BA")
            break
        elif ortalamaNot >= 80 and ortalamaNot < 85:
            harfNotu = "Harf Notunuz BB Geçtiniz"
            print("Harf Notunuz BB")
            break
        elif ortalamaNot >= 75 and ortalamaNot < 80:
            harfNotu = "Harf Notunuz CB Geçtiniz"
            print("Harf Notunuz CB")
            break
        elif ortalamaNot >= 70 and ortalamaNot < 75:
            harfNotu = "Harf Notunuz CC Geçtiniz"
            print("Harf Notunuz CC")
            break
        elif ortalamaNot >= 60 and ortalamaNot < 70:
            harfNotu = "Harf Notunuz DC Geçtiniz"
            print("Harf Notunuz DC")
            break
        elif ortalamaNot >= 50 and ortalamaNot < 60:
            harfNotu = "Harf Notunuz DD Geçtiniz"
            print("Harf Notunuz DD")
            break
        else:
            harfNotu = "Harf Notunuz FF Kaldınız"
            print("Harf notunuz FF büte kaldınız .")


while b:

        print("Büte Kaldınız")
        vizeNotu = float(input("Vize notunu tekrar gir : "))
        bütNotu = float(input("Büt notu gir :"))
        print("Öğrencinin Adı Soyadı : " + ogrenciAdSoyad)
        bortalamaNot = (0.4 * vizeNotu) + (0.6 * bütNotu)
        print("Not ortalamanız : ", bortalamaNot)

        if bortalamaNot >= 90:
            harfNotu = "Harf Notunuz AA Geçtiniz"
            print("Harf Notunuz AA")
            break
        elif bortalamaNot >= 85 and bortalamaNot < 90:
            harfNotu = "Harf Notunuz BA Geçtiniz"
            print("Harf Notunuz BA")
            break
        elif bortalamaNot >= 80 and bortalamaNot < 85:
            harfNotu = "Harf Notunuz BB Geçtiniz"
            print("Harf Notunuz BB")
            break
        elif bortalamaNot >= 75 and bortalamaNot < 80:
            harfNotu = "Harf Notunuz CB Geçtiniz"
            print("Harf Notunuz CB")
            break
        elif bortalamaNot >= 70 and bortalamaNot < 75:
            harfNotu = "Harf Notunuz CC Geçtiniz"
            print("Harf Notunuz CC")
            break
        elif bortalamaNot >= 60 and bortalamaNot < 70:
            harfNotu = "Harf Notunuz DC Geçtiniz"
            print("Harf Notunuz DC")
            break
        elif bortalamaNot >= 50 and bortalamaNot < 60:
            harfNotu = "Harf Notunuz DD Geçtiniz"
            print("Harf Notunuz DD")
            break
        else:
            harfNotu = "Harf Notunuz FF Kaldınız"
            print("Harf notunuz FF kaldınız .")
            break

with open("dosya.txt", "a",encoding="UTF-8") as f:
    f.write("-----Yeni Kişi----- \n")
    f.write("Öğrenci Adı Soyadı : "+ogrenciAdSoyad + "\n")
    f.write(str("Vize Notu : " +str(vizeNotu) + "\n"))
    f.write(str("Final Notu : " + str(finalNotu) + "\n"))
    f.write(str("Büt Notu : " +str(bütNotu) + "\n"))
    f.write(str("Ortalama Not : " +str(bortalamaNot) + "\n"))
    f.write(str(harfNotu))
    f.write("\n")

