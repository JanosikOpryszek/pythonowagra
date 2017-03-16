#obiekt z klasy Mapa zawiera Liste o wymiarach które okreslasz do ktorej sa wstawione
#obiekty pokoje w ktorych w artybucie przedm jest przechowywany obiekt
#przedmiot z artybutem "jaki" i przybiera "D" dobry albo "Z" zly.
#Mamy również obiekt podroznik ktory ma plecak i poprzez kierowanie klawiszami
#porusza sie po mapie, tam gdzie trafi zabiera przedmiot z pokoju do plecaka
#i usuwa go z pokoju, kiedy dojdziesz do prawego dolnego końca gra liczy punkty
#im mniej ruchów tym lepiej, im więcej zebranych D tym lepiej, 


import random

class Mapa():                   #tworzy zagnieżdżoną listę o opodanej  dł i szer
    def __init__(self,dl,sz):
        self.dl=dl
        self.sz=sz
        self.mapa=[]

        for i in range (0,self.sz):
            self.mapa.append([])
            for j in range (0,self.dl):
                self.mapa[i].append(0)
            
        
    def obrazuj(self):              #wyświetla ją szerokosc to głównalista, 
        for i in range(0,self.sz):  #długość zagnieżdżone listy w niej
            print(self.mapa[i])
        

    def ustaw(self,x,y,pok):        #wstawia obiekt pokój  w określone miejsce listy
        self.x=x
        self.y=y
        self.pok=pok
        self.mapa[self.x][self.y]=self.pok


class Pokoj():          #pokoj potrafi przyjac obiekt przedmiotu "przedm"
    def dodaj(self,przedm):
        self.przedm=przedm
        
    def __repr__(self):
        rep = "*"
        if self.przedm!=0:      #jak w atryb przedm ma zero pokazuje 0
            return self.przedm.jaki  #a jak ma tam obiekt przedm to pokazuje jego atrybut jaki
        else:
            return rep
      

class Przedmiot():              #przedmiot ma jeden atrybut, jaki, który określa rodzaj przedmiotu
    def __init__(self,jaki):    #D - dobry Z - zły
        self.jaki=jaki
    def __repr__(self):
        return self.jaki

class Czlowiek():       #człowiek,przez "gdzie" odwoluje się do mapy(listy)
    def __init__(self,gdzie):   #po ktorej sie porusza
        self.plecak=[]
        self.gdzie=gdzie
    def pozycja(self,wx,wy):    #okresla jego pozycje
        self.wx=wx
        self.wy=wy
        if self.gdzie.mapa[self.wx][self.wy].przedm==0:     #sprawdza czy w pokoju jest przedmiot, jak jest 0
            print("Twój plecak nie powiększył zawartości")  #wyswietla komunikat, ze nie zabral przedmiotu 
            exit
        else:
            self.plecak.append(self.gdzie.mapa[self.wx][self.wy].przedm)   #dodaje przedmiot do plecaka
            self.gdzie.mapa[self.wx][self.wy].przedm=None                   #i usuwa z pokoju obiekt przedmiotu
            self.gdzie.mapa[self.wx][self.wy].przedm=0
            self.gdzie.obrazuj()
            
    def pokaz(self):                                #pokazuje zawartosc plecaka i liczy punkty
        print("zawartosc plecaka ",self.plecak)
        skarby=0
        smieci=0
        for i in self.plecak:
            if i.jaki==str("D"):
                skarby+=1
            if i.jaki==str("Z"):
                smieci+=1
                    
        print("Zebrałeś ",skarby,"skarbów i ",smieci,"smieci. ")
        print("Ilość skarbów odjąc ilośc śmieci, czyli masz punktów: ",skarby-smieci)
        print("Wykonałeś ",licznik,"ruchów")
        print("Za każdy punkt dostajesz 10 ale tracisz po punkcie za każdy ruch")
        print("Punkty razy 10 i odjąć ilość twoich ruchów, czyli ",(skarby-smieci),"x 10 odjąc ",licznik)
        print("Twój ostateczny wynik to: ",10*(skarby-smieci)-licznik)
        print("Gratuluje !!!")
        input("naciśnij klawisz na zakonczenie")
              
        
        


print("Podaj wielkosc mapy")
incorrect_answer =True
while incorrect_answer:
    szerokosc=int(input("Szerokosc 5-20: "))    
    if szerokosc <5 or szerokosc > 20:
        print("wykonuj polecenia albo nie ma zabawy")
    else:
        incorrect_answer=False

incorrect_answer =True
while incorrect_answer:
    dlugosc=int(input("Dlugosc 5-20: "))    
    if dlugosc <5 or szerokosc > 20:
        print("wykonuj polecenia albo nie ma zabawy")
    else:
        incorrect_answer=False


teren=Mapa(dlugosc,szerokosc)
ilosc=szerokosc*dlugosc


podroznik=Czlowiek(teren)

#tworzenie listy pokoi
objects=[]
for i in range(0,ilosc):
    objects.append(Pokoj())

#tworzenie przedmiotów 
jaki=["D","Z"]
przedmioty=[]
for i in range(0,ilosc):
    przedmioty.append(Przedmiot(jaki[random.randint(0, 1)]))
    
#i dodawanie ich do pokoi
for i in range(0,ilosc):
    objects[i].dodaj(przedmioty[i])


#wstawianie kolejnych pokoi do mapy
dd=0
for i in range(0,szerokosc):
    for j in range(0,dlugosc):
        teren.ustaw(i,j,objects[dd])
        dd+=1


print("********************************************************")
print("zaczynasz w lewym górnym rogu")
print("dobre przedmioty to D")
print("zle przedmioty to Z")
print("Dojdz w prawy dolny róg jak najmniejszą ilością ruchów ")
#wyswietla obiekt mapy
teren.obrazuj()

x=0
y=0
cc=0
licznik=0

while True:
    licznik+=1
    print("rusz sie klawisz:     w-góra     s-dół     a-lewo    d-prawo  + Enter")
    cc=input()
    
    if x==(szerokosc-1) and y==(dlugosc-1):
        break

    elif cc=="d":
        y+=1
        if y>(dlugosc-1):
            print("sciana tam nie pójdziesz")
            y-=1
            podroznik.pozycja(x,y)
        else:
            podroznik.pozycja(x,y)
    elif cc=="a":
        y-=1
        if y<0:
            print("sciana tam nie pójdziesz")
            y+=1
            podroznik.pozycja(x,y)
        else:
            podroznik.pozycja(x,y)
    elif cc=="s":
        x+=1
        if x>(szerokosc-1):
            print("sciana tam nie pójdziesz")
            x-=1
            podroznik.pozycja(x,y)
        else:
            podroznik.pozycja(x,y)
    elif cc=="w":
        x-=1
        if x<0:
            print("sciana tam nie pójdziesz")
            x+=1
            podroznik.pozycja(x,y)
        else:
            podroznik.pozycja(x,y)
        

podroznik.pokaz()











