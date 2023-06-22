import time
import os

program_running = True

# Criação de função para encurtar e otimizar o código
def clear():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')

# Criação de função para redução de poluição visual no código
def makeiteasy():
    time.sleep(2)
    input("Pressione a tecla ENTER para continuar \n")
    clear()

while program_running:

    print("-=" * 40)

    try:
        anos = float(input("Insira a quantidade de tempo, em anos, que você fuma: "))
        total_dias = anos * 360
        valor = float(input("Insira o valor atual do maço de cigarro, em reais: R$"))
        quantidade = float(input("Insira a quantidade de maços que você fuma por dia: "))
        
    ####################################################################################################
    # VALIDAÇÃO DE ERROS E ENTRADAS INVÁLIDAS

    # Validação de erro para inserção de classe str na variável float
    except ValueError:
        clear()
        print("-=" * 45)
        print("Entrada inválida. Insira apenas números. Verifique, também, a inserção do valor do maço.")
        print("Para inserção do valor, deve-se inserir ponto ao invés de vírgula, como por exemplo: R$9.90")
        print("-=" * 45)
        makeiteasy()
        continue

    print("-=" * 40)

    # Condição para a entrada inválida: não é possivel fumar há determinada quantidade de anos e não ter um valor para o maço ou a quantidade de maços por dia ser 0 ou negativo.
    if anos != 0 and (((valor or quantidade) <= 0) or ((valor and quantidade) <= 0)):
        print("Entrada inválida. Insira um valor válido (maior que 0) para o valor do maço ou para a quantidade.")
        makeiteasy()
        continue

    # Validação de erro no valor da quantidade de anos inserida: a quantidade não pode ser negativa.
    elif anos < 0:
        clear()
        print("-=" * 40)
        print("Entrada inválida. O tempo de vício no tabagismo não pode ser menor que 0.")
        makeiteasy()
        continue

    # Validação para quantidade de anos == 0 e entrada de valores para preço do maço e/ou quantidade de maços consumidos por dia.
    elif anos == 0 and (valor or quantidade) != 0:
        clear()
        print("-=" * 40)
        print("Entrada inválida. Se a quantidade de anos é 0, entende-se que você não consumiu cigarros!")
        makeiteasy()
        continue

    # Validação para entrada de valores irreais e grandes demais
    elif anos > 100 or valor > 150 or quantidade > 20:
        clear()
        print("-=" * 45)
        print("Entrada inválida. Um ou mais valores inseridos estão em quantidades irreais.")
        makeiteasy()
        continue

    # FIM DA VALIDAÇÃO DE ERROS E ENTRADAS INVÁLIDAS
    ####################################################################################################

    # Cálculo do valor total gasto com tabagismo
    calculo = (total_dias * quantidade) * valor

    ####################################################################################################
    # PROSSEGUIMENTO COM AS SOLUÇÕES PARA A ATIVIDADE - SAÍDAS

    if calculo > 0 and calculo < 20000:
        print("Com o valor de R${:.2f}, você poderia ter dado entrada em um carro.".format(
            calculo))

    elif calculo >= 20000 and calculo <= 50000:
        print("Com o valor de R${:.2f}, você poderia ter comprado um carro popular usado.".format(
            calculo))

    elif calculo == 0:
        print("Você não gastou dinheiro com tabagismo. Parabéns, continue promovendo saúde!")

    else:
        print("Com o valor de R${:.2f}, você poderia ter comprado um carro zero.".format(
            calculo))

    # Bloco para o prosseguimento no programa
    print("-=" * 40)
    makeiteasy()

    # FIM DO BLOCO DAS SAÍDAS
    ####################################################################################################

    ####################################################################################################
    # CRIAÇÃO DO MENU DE FINALIZAÇÃO DO PROGRAMA, ONDE O USUÁRIO DECIDE SE VAI SAIR OU VOLTAR AO INÍCIO
  
    while True:

        print("O que deseja fazer?\n", "-=" * 10,
            "\n1 - Voltar ao início",
            "\n2 - Sair")
        print("-=" * 10)

        try:
            menu_fim = int(input("Insira a opção desejada: "))

            if menu_fim == 1:
                # Voltar para o começo do programa, saindo do loop criado para este menu.
                clear()
                print("-=" * 15)
                print("Voltando ao início...")
                time.sleep(2)
                clear()
                program_running = True
                break

            elif menu_fim == 2:
                # Sair do programa
                clear()
                print("Saindo...")
                time.sleep(1)
                quit()

            else:
                # Validação de opção inválida com volta para este menu
                clear()
                print("-=" * 20, "\nOpção inválida. \nVoltando ao menu...")
                time.sleep(2)
                clear()
                continue

        except ValueError:
            # Validação para inserção de caracteres inválidos na variável int
            clear()
            print("-=" * 10, "\nOpção inválida. Insira apenas números.\nVoltando ao menu...")
            time.sleep(2)
            clear()
            continue

     # FIM DO PROGRAMA
    ####################################################################################################   
