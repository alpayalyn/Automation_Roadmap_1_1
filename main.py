min_Sayi_1 = int(input("Lütfen minimum sayı giriniz."))
max_sayi_2 = int(input("Lütfen maximum sayı giriniz."))
bolunecek_sayi_3 = int(input("Lütfen bölüm için sayı giriniz."))

def bolum(min_Sayi_1, max_sayi_2, bolunecek_sayi_3):

    tum_sayilar = list(range(min_Sayi_1, max_sayi_2 +1))
    print(tum_sayilar)  #silelim

    tam_bolunen_sayilar = []

    i = 0 #silelim
    j = 0

    for e in tum_sayilar:
        sifirmi = tum_sayilar[j] % bolunecek_sayi_3
    # variable 1 defa kullanalmış, if içine alalım
        if (sifirmi == 0):

            tam_bolunen_sayilar.append(tum_sayilar[j])
            i += 1 #silelim

        j += 1

    return tam_bolunen_sayilar

son_durum = bolum(min_Sayi_1, max_sayi_2, bolunecek_sayi_3)
print(son_durum)
# variable 1 defa kullanalmış, print içine alalım
# variable camelCase olacak, ingilizce olsun
