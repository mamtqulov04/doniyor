Energiya = 100
Pul = 500
Kalit = 0

togri = 0
xato = 0
dokon = 0
sarf = 0
oxirgi = "yoq"

while True:
    if inergiya <= 0:
        print("Game Over")
        break

    if kalit >=5:
        print("Tabriklaymiz! Siz bunkerdan chiqdinggiz!")
        break
    print("\n1. 1-xonaga kirish")
    print("2.2-xonaga kirish")
    print("3.dokon")
    print("4.inventar")
    print("5.statistika")
    print("0.chiqish")
    tanlov = int(input("Tanlang"))
    if tanlov ==1:
        javob = input("python qanaqa til:")
        if javob.lower() =="dasturlash":
            energiya +=20
            kalit +=1
            togri +=1
            print("togri")
        else :
            energiya -=15
            xato += 1
            print("noto'g;ri")
        if random.randint(1,5) ==3:
            pul +=100
            print("bonus:+100 pul")

            oxirgi = "1-xona"

        elif tanlov ==2:
            javob = int(input("30=20="))
        if javob ==50:
            pul +=200
            togri +=2
            energiya -=10
            print('togri')
            energiya -=10
            xato +=1
            print("notogri")
            oxirgi ="2-xona"

        elif tanlov ==3:
            energiya +=10
            print("bonus: +10 energiya")
            oxirgi ="2-xona"
        elif anlov ==3:
            dokon +=1
            print("1.dorixona(+30 energiya)-150")
            print("2. Kalit sotib olish -300")
            t=int(input("tangalar:"))
        if t==1:
           if pul >=150:
            pul-=150
            energeya+=30
            sarf +=150
            print("Sotib olindi:")
        elif t ==2:
            if pul >=300:
               pul -=300
               kalit +=5
               sarf +=300
               print("Kalit olindi.")
            else :
                print("Pul yetmaydi.")
                ohirgi = "do'kon"
        elif tanlov ==4:
            print("Energiya:",energiya)
            print("Pul:",pul)
            print("kalit:",kalit)
            
            oxirgi = "inventar"
        elif tanlov ==5:
            print("To'g'ri javoblar:",togri)
            print("Xato javoblar:",xato)
            print("Do'konga kirishlar:",dokon)
            print("Jami sariflangan pul:",sarf)
            print("oxirgi amal:",oxirgi)
            oxirgi = "statistika"
        elif tanlov ==0:
            print("Game Over.")
            break
        else:
            print("Noto'g'ri tanlov!")