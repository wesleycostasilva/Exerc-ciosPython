import this
import ExerciciosModel
this.opcao = -1


def Menu():
    print('Menu\n\n' +
          '\n1. Exercicio 01' +
          '\n2. Exercicio 02' +
          '\n3. exercicio 03' +
          '\n0. Sair'         +
          '\nEscolha uma das opções acima:')
    this.opcao = int(input())

def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print('Obrigado!')
        elif this.opcao == 1:
            print(ExerciciosModel.exercicios01())
        elif this.opcao == 2:
            print('Escreva aqui a solução para o exercício 02')
            num1 = int(input())
            print(ExerciciosModel.exercicios02(num1))
        elif this.opcao == 3:
            print('informe a base do retângulo')
            bas = float(input())
            print('informe a altura do retângulo')
            altura = float(input())
            print(ExerciciosModel.exercicios03(bas, altura))
        else:
            print('Opção informada não é válida!')








