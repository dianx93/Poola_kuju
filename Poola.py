__author__ = 'Diana'
#Poola.py Diana Algma 7.10.2014

import math                                 #et astendada
t = {'+':2, '-':2, '*':3, '/':3, '^':4}     #tehtemärkide prioriteedid, samuti saab selle abil kontrollida, kas sümbol
                                            #on tehtemärk

def arvutus(poola):     #funktsioon, mis arvutab LIFO stäki abil inverteeritud Poola kujul oleva avaldise väärtuse
    jada = poola.split(" ")     #lahutab argumendiks antud sõne arvude ja märkide jadaks
    stack = []
    for i in jada:
        if i.replace(".", "", 1).isdigit():              #kui i on arv, lisab stäkki
            stack.append(float(i))
        elif i in t:                        #kui on tehtemärk, siis kõigepealt võtab stäkist 2 viimast arvu
            if len(stack)<2:                #kui stäkis pole piisavalt arve, siis on sisestatud vigane avaldis ja
                return "Vigane avaldis"     #vastust ei saa arvutada
            a = stack.pop()
            b = stack.pop()
            if i == "+":            #siis teeb teeb nende arvudega soovitud tehte ja lisab tulemuse stäkki
                stack.append(a+b)
            elif i == "-":
                stack.append(b-a)
            elif i == "*":
                stack.append(a*b)
            elif i == "/":
                stack.append(b/a)
            elif i == "^":
                stack.append(math.pow(b, a))
    if len(stack) != 1:             #kui stäkis pole 1 element, siis on sisestatud vigane avaldis, vastust pole leitud
        return "Vigane avaldis"
    return round(stack[0], 2)       #kui kõik elemendid on läbitud, siis tagastab stäki esimese (ainukese) väärtuse,
                                    #mis on ümardatud sajandikeni

def jadaks(aritm):                  #funktsioon, mis teeb sõnena antud aritmeetilise avaldise jadaks
    jada = []
    nr = ""                         #muutuja, mis jätab meelde numbrid peale viimast märki
    for i in aritm:
        if i.isdigit():             #kui i on number, siis lisada muutujasse nr
            nr = nr + i
        elif i ==".":               #kui i on punkt, siis lisada numbrisse
            nr = nr + i
        else:                       #kui on märk
            if nr != "":            #kui mingi arv on salvestatud, siis lisada jadasse ja tühjendada muutuja
                jada.append(nr)
                nr = ""
            jada.append(i)          #lisada märk jadasse
    if nr != "":                    #lisada viimane salvestatud arv jadasse
        jada.append(nr)
    return jada

def poolakujule(aritm):     #funktsioon, mis teisendab aritmeetilise avaldise inverteeritud Poola kujule
    jada = jadaks(aritm)    #kõigepealt teha sõne jadaks
    poola = ""              #sõne, mille lõpus tagastame
    stack = []              #stäkk, mis hoiab tehtemärke, mida sõnesse hiljem lisada
    for i in jada:
        if i.replace(".", "", 1).isdigit():     #kui i on arv, siis lisada sõnesse
            poola = poola + " " + i
        elif i == ")":      #kui i on lõpetav sulg, siis lisatakse sõnesse märke seni, kuni jõutakse alustava suluni
            while len(stack) != 0:
                märk = stack.pop()
                if märk != "(":
                    poola = poola + " " + märk
                else:
                    break
        elif i == "(":      #kui i on alustav sulg, siis lisatakse stäkki
            stack.append(i)
        elif i in t:        #kui i on tehtemärk:
            if len(stack) == 0:     #kui stäkis märke pole, siis lisatakse i
                stack.append(i)
            else:
                märk = stack.pop()  #kui stäkis on märke, võetakse sealt viimane
                if märk in t:       #kui see on tehtemärk
                    if t[i] > t[märk]:      #kui i prioriteet on suurem, siis lisatakse mõlemad stäkki
                        stack.append(märk)
                        stack.append(i)
                    else:                   #kui viimane märk oli suurema prioriteediga, siis lisatakse märk sõnesse ja
                        poola = poola + " " + märk      #ja i lisatakse stäkki
                        stack.append(i)
                else:               #kui märk pole tehtemärk, siis lisatakse märk ja i stäkki
                    stack.append(märk)
                    stack.append(i)
    while len(stack) != 0:              #seni kuni stäkk pole tühi, siis lisatakse märgid, mis pole sulud, sõnesse
        märk = stack.pop()
        if märk not in ["(", ")"]:
            poola = poola + " " + märk
    return poola[1:]                    #tagastatakse sõne ilma esimese märgita, sest see on tühik


while True:
    aritm = input("Aritmeetiline avaldis: ")
    print("Inverteeritud Poola kuju:", poolakujule(aritm))
    print("Avaldise väärtus:", arvutus(poolakujule(aritm)))
