from Calculadora import Calculadora

class controlCalculadora:
    def __init__(self):
        self.calc = Calculadora()
        self.opcao = -1

    def menu(self):
        print("Escolha uma das opções abaixo:\n\n" +
              "0.Sair\n" +
              "1.Somar\n" +
              "2.Subtrair\n" +
              "3.Multiplicar\n" +
              "4.Dividir")
        self.opcao = int(input())

    def operacao(self):
        while(self.opcao !=0):
            self.menu()
            if self.opcao == 0:
                print("Obrigado")
            elif self.opcao == 1:
                print("Informe o primeiro número: \n")
                num1 = int(input())
                print("Informe o segundo número: \n")
                num2 = int(input())
                print("O resultado da soma é: \n")
                print(self.calc.soma(num1, num2))

            elif self.opcao == 2:
                print("Informe o primeiro número: \n")
                num1 = int(input())
                print("Informe o segundo número: \n")
                num2 = int(input())
                print("O resultado da subtração é: \n")
                print(self.calc.subtracao(num1, num2))

            elif self.opcao == 3:
                print("Informe o primeiro número: \n")
                num1 = int(input())
                print("Informe o segundo número: \n")
                num2 = int(input())
                print("O resultado da multiplicação é: \n")
                print(self.calc.multiplicar(num1, num2))

            elif self.opcao == 4:
                print("Informe o primeiro número: \n")
                num1 = int(input())
                print("Informe o segundo número: \n")
                num2 = int(input())
                print("O resultado da divisão é: \n")
                print(self.calc.dividir(num1, num2))


            else:
                print("Opção Inválida!")