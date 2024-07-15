# Verificar se um número é positivo, negativo ou neutro
def verificarNumero():
    numero = int(input("Digite um número: "))
    
    if numero > 0:
        print(f"{numero} é um número positivo.")
    elif numero < 0:
        print(f"{numero} é um número negativo.")
    else: 
        print(f"{numero} é um número neutro.")
     
# Resultado
verificarNumero()
