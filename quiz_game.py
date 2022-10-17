import random
puan =0
caps = ["Ankara","Pekin","Berlin","Paris","Washington","Lizbon","Tokyo","Fas","Cape Town"]
cont = ["Türkiye","Çin","Almnaya","Fransa","ABD","Portekiz","Japonya","Fas","Güney Afrika"]
x=0

while x < 9:
    b = random.randint(0,len(cont))
    g = cont[b]
    print(f"Bu Ülkenin başkenti neresidir {g} ? : ")
    z = input("Cevap: ")
    if z == caps[b]:
        print("Cevabınız doğru !")
        x +=1
        puan +=1
    else:
        print("Cevabınız yanlış !")
        x+=1
    
    cont.pop(b)
    caps.pop(b)
    if x == 5: 
        break
print(f"Oyun Bitti Puanınız : {puan*10}")



