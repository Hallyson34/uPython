d=6
s=0
m=1
print("   Calendário 2021")
while m<=12: 
    print("Legenda: 1=Domingo, 2=Segunda-Feira, 3=Terça-Feira, 4=Quarta-Feira, 5=Quinta-Feira, 6=Sexta-Feira, 7=Sábado")
    print(f"MÊS  0{m}")
    for i in range(1,32):
        i=str(i)
        s+=1
        if s%7==0 and s!=0:
            if m==2 and i=="28":
                print(end=f"{i}({d}) \n\n")
                d+=1
                break
            else:
                print(end=f"{i}({d})\n")
        elif i=="31":
            print(end=f"{i}({d}) \n\n")
        elif (m==4 or m==6 or m==9 or m==11) and i=="30":
            print(end=f"{i}({d}) \n\n")
            d+=1
            break            
        else:
            print(end=f"{i}({d}) ")
        d+=1
        if d==8:
            d=1
    if d==8:
        d=1
    s=0
    m+=1
    
     