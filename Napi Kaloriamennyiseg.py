#Mit tud? Nemre és korra lebontva megtudhatjuk, hogy mennyi kalóriát ajánlott fogyasztanunk naponta.


#Adatok
print("Mi a nemed?")
nem = input()
print("Hány éves vagy?")
kor = int(input())
print("Rendszeresen sportolsz?(Minimum heti 3-szor)")
mozgas = input()



#Férfi
if nem == "férfi" and kor in range(9,13) and mozgas == "igen":
    print("A napi ajánlott kalóriabeviteled: 2600")

if nem == "férfi" and kor in range(9,13) and mozgas == "nem":
    print("A napi ajánlott kalóriabeviteled: 2200")



if nem == "férfi" and kor in range(14,18) and mozgas == "igen":
    print("A napi ajánlott kalóriabeviteled: 3200")

if nem == "férfi" and kor in range(14,18) and mozgas == "nem":
    print("A napi ajánlott kalóriabeviteled: 2800")




if nem == "férfi" and kor in range(19,30) and mozgas == "igen":
    print("A napi ajánlott kalóriabeviteled: 3000")

if nem == "férfi" and kor in range(19,30) and mozgas == "nem":
    print("A napi ajánlott kalóriabeviteled: 2700")



if nem == "férfi" and kor in range(31,50) and mozgas == "igen":
    print("A napi ajánlott kalóriabeviteled: 2800")

if nem == "férfi" and kor in range(31,50) and mozgas == "nem":
    print("A napi ajánlott kalóriabeviteled: 2500")




if nem == "férfi" and kor>=50 and mozgas == "igen":
    print("A napi ajánlott kalóriabeviteled: 2600")

if nem == "férfi" and kor>=50 and mozgas == "nem":
    print("A napi ajánlott kalóriabeviteled: 2400")  








#NŐ
if nem == "nő" and kor in range(9,13) and mozgas == "igen":
    print("A napi ajánlott kalóriabeviteled: 2200")

if nem == "nő" and kor in range(9,13) and mozgas == "nem":
    print("A napi ajánlott kalóriabeviteled: 1900")




if nem == "nő" and kor in range(14,18) and mozgas == "igen":
    print("A napi ajánlott kalóriabeviteled: 2500")

if nem == "nő" and kor in range(14,18) and mozgas == "nem":
    print("A napi ajánlott kalóriabeviteled: 2300")




if nem == "nő" and kor in range(19,30) and mozgas == "igen":
    print("A napi ajánlott kalóriabeviteled: 2300")

if nem == "nő" and kor in range(19,30) and mozgas == "nem":
    print("A napi ajánlott kalóriabeviteled: 2100")




if nem == "nő" and kor in range(31,50) and mozgas == "igen":
    print("A napi ajánlott kalóriabeviteled: 2200")

if nem == "nő" and kor in range(31,50) and mozgas == "nem":
    print("A napi ajánlott kalóriabeviteled: 2000")




if nem == "nő" and kor>=50 and mozgas == "igen":
    print("A napi ajánlott kalóriabeviteled: 2100")

if nem == "nő" and kor>=50 and mozgas == "nem":
    print("A napi ajánlott kalóriabeviteled: 1900")
    
    
    
    



