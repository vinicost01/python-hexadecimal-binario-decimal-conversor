#vini.cost

while True:
    
    op1=int(input("escolha uma opcao:\n[1]binario/decimal\n[2]hexadecimal/decimal\n[3]decimal/binario\n[4]decimal/hexadecimal\n[5]binario/hexadecimal\n[6]hexadecimal/binario\n:"))  
    
    if op1==1:
        binario=input("digite o numero binario a ser convertido: ")
        decimal=int(binario,2)
        print("o numero binario: {} em decimal e: {}".format(binario,decimal))
        
    if op1==2:
        hexa=input("digite o numero hexadecimal a ser convertido: ") 
        decimal=int(hexa,16)
        print("o numero hexadecimal: {} em decimal e: {}".format(hexa,decimal))
    
    if op1==3:
        decimal=int(input("digite um numero decimal para ser convertido para binario: "))
        binario=format(decimal,'b')
        print("o numero decimal: {} em binario e: {}".format(decimal,binario))
        
    if op1==4:
        decimal=int(input("digite um numero decimal para ser convertido para hexadecimal: "))
        hexa=format(decimal,'x')
        print("o numero decimal: {} em hexadecimal e: {}".format(decimal,hexa))

    if op1==5:
        binario=input("digite o numero binario a ser convertido: ")
        decimal=int(binario,2)
        hexa=format(decimal,'x')
        print("o numero binario: {} em hexadecimal e: {}".format(binario,hexa))
        
    if op1==6:
        hexa=input("digite o numero hexadecimal a ser convertido: ") 
        decimal=int(hexa,16)
        binario=format(decimal,'b')
        print("o numero hexadecimal: {} em binario e: {}".format(hexa,binario))
        
    else:print("opcao invalida")
    
    ext=str(input("deseja converter outro numero? s/n :"))
    if ext=="n":
        break