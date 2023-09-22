# Função para somar dois números

def somar(a,b):
    return a + b

# Função para subtrair dois números
def subtrair(a,b):
    return a - b


# Função para multiplicar dois números
def multiplicar(a,b):
    return a * b



# Função para dividir dois números
def dividir(a,b):
    if b == 0:
        return "Erro"
    else:
        return a / b



# Função principal
def main():
    while True:
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")
        opcao = int(input("Digite a opção: "))
        if opcao == 0:
            break
        elif opcao == 1:
            a = int(input("Digite o primeiro valor: "))
            b = int(input("Digite o segundo valor: "))
            print(somar(a,b))
        elif opcao == 2:
            a = int(input("Digite o primeiro valor: "))
            b = int(input("Digite o segundo valor: "))
            print(subtrair(a,b))
        elif opcao == 3:
            a = int(input("Digite o primeiro valor: "))
            b = int(input("Digite o segundo valor: "))
            print(multiplicar(a,b))
        elif opcao == 4:
            a = int(input("Digite o primeiro valor: "))
            b = int(input("Digite o segundo valor: "))
            print(dividir(a,b))


if __name__ == "__main__":
    main()
