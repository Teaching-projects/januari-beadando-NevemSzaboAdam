#Cél: Egy működöképes kalóriakalkulátort készíteni

#Adatok
tömeg=float(input("Hány kg vagy?"))
méret=float(input("Hány cm vagy?"))
#BMI kiszámítása
bmi=tömeg/(méret/100)**2 
if bmi<=16:
    print("Súlyosan sovány vagy! Keress fel egy orvost minél hamarabb!")
elif 17<=bmi<=18.5:
    print(" Mérsélkelten vékony vagy, kicsit dolgozd fel azokat a kalóriákat!")
elif 18.5<bmi<=25:
    print("Ideális testtömeggel rendelkezel! Próbéld meg megtartani!")
elif 25<bmi<=30:
    print("Enyhén túlsúlyos vagy! Dobj le egy-két kilót! Hidd el sokkal jobban fogod érezni magad!")
elif 30<bmi<=35: 
    print("El vagy hízva! Diétára, és edzésre van szükséged!")
elif 35<bmi:
    print("Súlyosan el vagy hízva! Keress fel egy fitness gurut!")





