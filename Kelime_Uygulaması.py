import random
import os
def yeni_kelime_kayıt_et():
    English_word = input("ingilizce:").strip()
    Türkiye_word = input("türkçe:").strip()
    kelime_mevcut = False
    if os.path.exists("Kelime_Tablosu.txt"): # burada os la dosya varsa aç komutunu  verdik.
        with open("Kelime_Tablosu.txt","r",encoding="utf-8") as file1:
            satırlar = file1.readlines()
            for satir in satırlar:
                satir = satir.strip()
                if ":" in satir:
                    ing,turk = satir.split(":")
                    if ing.strip()==English_word or turk.strip == Türkiye_word:
                        kelime_mevcut = True
                        break
    if kelime_mevcut:
        print(" bu kelime zaten mevcut. ")
    else:

        with open("Kelime_Tablosu.txt","a",encoding="utf-8") as file2:
            file2.write(English_word+":"+Türkiye_word+"\n")
            print("yeni kelime başarıyla eklendi.")
def kelime_listesini_göster():
    with open("Kelime_Tablosu.txt","r",encoding="utf-8") as file:
        for i in file:
            print(i)
def kelime_tahmin_et(ingilizce_kelime,türkce_kelime,Çıkış):
    while True:
        kelime_tercihi = input("hangi şekilde oynamak istersiniz:")
        kelimeler = {}
        if kelime_tercihi == ingilizce_kelime:

            with open("Kelime_Tablosu.txt", "r", encoding="utf-8") as file:
                satirlar = file.readlines()
                for satır in satirlar:
                    satır = satır.strip()
                    if ":" in satır:
                        ingilizce, türkçe = satır.split(":")
                        kelimeler[ingilizce.strip()] = türkçe.strip()
            soru_sayısı = 0
            score = 0
            while True:
                soru_sayısı += 1
                ingilizce_kelimeler = random.choice(list(kelimeler.keys()))
                doğru_ccevap = kelimeler[ingilizce_kelimeler]
                print(f"{soru_sayısı}-İngilizcesi {ingilizce_kelimeler} olan kelimenin türkçesi nedir? ")
                kullanıcı_tahmin = input("Tahmininiz: ").strip()
                if kullanıcı_tahmin.lower() == doğru_ccevap.lower():
                    score += 10
                    print(f"Doğru! puanınız:{score}")
                else:
                    score -= 10
                    print(f"Yanlış. Doğru cevap {doğru_ccevap} idi. puanınız:{score} ")

        elif kelime_tercihi == türkce_kelime:
            with open("Kelime_Tablosu.txt","r",encoding="utf-8") as file:
                satirlar = file.readlines()
                for satır in satirlar:
                    satır = satır.strip()
                    if ":" in satır:
                        ingilizce,türkçe = satır.split(":")
                        kelimeler[türkçe.strip()] = ingilizce.strip()
            soru_sayısı = 0
            score = 0
            while True:
                soru_sayısı+=1
                turkce_kelime = random.choice(list(kelimeler.keys()))
                doğru_ccevap = kelimeler[turkce_kelime]
                print(f"{soru_sayısı}-Türkçesi {turkce_kelime} olan kelimenin ingilizcesi nedir? ")
                kullanıcı_tahmin = input("Tahmininiz: ").strip()
                if kullanıcı_tahmin.lower() == doğru_ccevap.lower():
                    score += 10
                    print(f"Doğru! puanınız:{score}")
                else:
                    score -= 10
                    print(f"Yanlış. Doğru cevap {doğru_ccevap} idi. puanınız:{score} ")
        else:
            if kelime_tercihi == Çıkış:
                print("Başarıyla çıkış yapıldı")
                break


while True:
    page = input("1- Yeni Kelime Kayıt Et\n2- Kelimeleri Göster\n3- Kelime Tahmin Et\n4- Çıkış\n Seçenek= ")
    if page=="1":
        yeni_kelime_kayıt_et()
    elif page == "2":
        kelime_listesini_göster()
    elif page == "3":
        print("Doğru cevap sayısı +10 yanlış cevap sayısı -10 puandır.")
        kelime_tahmin_et(ingilizce_kelime="ingilizce",türkce_kelime="türkçe",Çıkış="q")
    else:
        break