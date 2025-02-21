vade = input("lutfen vade orani giriniz")

print(vade)

print(type(vade))

vad = int(vade)

print(type(vad))


# vade = int(input("lutfen vade orani giriniz"))

print(type(vade))

print("seçtiğiniz vade sonucu ortaya çıkan vade: "+ str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortataya çıkan vade: {vade}")

isim = "halit"
metin = "merhaba {name}".format(name=isim)

print(metin)

# f-string
metin = f"Hoşgeldiniz {metin}"

print(metin)

krediler = ["ihtiyaç","sahibi","espiri"]

print(type(krediler))

krediler.append(5) #ekleme
krediler.pop() # indexle siler, index verilmez ise sonuncuyu siler  
krediler.remove("sahibi") # değerle siler
print(krediler)

krediler.extend(["y kredisi","x kredisi"])

print(krediler)

for i in range(10):
    print(i)
print("----------------------------------------------")
for i in range(5,10):
    print(i)

print("******************")

for kredi in krediler:
    print(kredi)


while i <len(krediler):
    i+=1
    print(krediler[i])
    if krediler[i] == "espiri" : 
        break

def calculate():
    print(100-20)

def paramsCalculate(fiyat, indirim):
    print(fiyat-indirim)

calculate()
paramsCalculate(1,2)


def retCalculate(price,sale):
    return price - sale #istenmildiği kullnlması için (atama üzerinde oynama) return kullanıır 
    

