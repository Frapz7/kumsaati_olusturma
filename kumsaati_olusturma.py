sayi= int(input("Sayı giriniz ="))
dongu= int(1)
for i in range (2*(sayi+1)):
    
    if dongu==1:
        bosluk = int(i)
        yildiz = int((2*sayi+1)-2*i)
        if yildiz==1:
            dongu=2
    else:
        yildiz = int(2*(i-(sayi+1))+1)
        bosluk = int(i-((2*(i-(sayi+1)))+1))
        
    print(" "*bosluk+"*"*yildiz)
