#Mit tud? Nemre és korra lebontva megtudhatjuk, hogy mennyi kalóriát ajánlott fogyasztanunk naponta.


#Adatok
print("Mi a nemed?")
nem = input()
print("Hány éves vagy?")
kor = int(input())
print("Rendszeresen sportolsz?(Minimum heti 3-szor)")
mozgas = input()



#Férfi
if nem == "Férfi" and kor in range(9,13) and mozgas == "Igen":
    print("A napi ajánlott kalóriabeviteled: 2600")

if nem == "Férfi" and kor in range(9,13) and mozgas == "Nem":
    print("A napi ajánlott kalóriabeviteled: 2200")



if nem == "Férfi" and kor in range(14,18) and mozgas == "Igen":
    print("A napi ajánlott kalóriabeviteled: 3200")

if nem == "Férfi" and kor in range(14,18) and mozgas == "Nem":
    print("A napi ajánlott kalóriabeviteled: 2700")




#NŐ
if nem == "Nő" and kor in range(9,13) and mozgas == "Igen":
    print("A napi ajánlott kalóriabeviteled: 2200")

if nem == "Nő" and kor in range(9,13) and mozgas == "Nem":
    print("A napi ajánlott kalóriabeviteled: 1900")


if nem == "Nő" and kor in range(14,18) and mozgas == "Igen":
    print("A napi ajánlott kalóriabeviteled: 2400")

if nem == "Nő" and kor in range(14,18) and mozgas == "Nem":
    print("A napi ajánlott kalóriabeviteled: 2100")



  





    
    
    
    



