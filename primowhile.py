n = int(input())
i=2
primo = True
while i<n and primo !=False:
    if n % i == 0:
        primo = False
    i+=1
if primo:
    print("Primo")
else:
    print("Composto")
        
    
    

