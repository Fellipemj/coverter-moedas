import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_text():
    text = r""" 
 /$$$$$$                                                       /$$                                                                       /$$                    
 /$$__  $$                                                     | $$                                                                      | $$                    
| $$  \__/  /$$$$$$  /$$$$$$$  /$$    /$$  /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$        /$$$$$$/$$$$   /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$$
| $$       /$$__  $$| $$__  $$|  $$  /$$/ /$$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$      | $$_  $$_  $$ /$$__  $$ /$$__  $$ /$$__  $$ |____  $$ /$$_____/
| $$      | $$  \ $$| $$  \ $$ \  $$/$$/ | $$$$$$$$| $$  \__/  | $$    | $$$$$$$$| $$  \__/      | $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  | $$  /$$$$$$$|  $$$$$$ 
| $$    $$| $$  | $$| $$  | $$  \  $$$/  | $$_____/| $$        | $$ /$$| $$_____/| $$            | $$ | $$ | $$| $$  | $$| $$_____/| $$  | $$ /$$__  $$ \____  $$
|  $$$$$$/|  $$$$$$/| $$  | $$   \  $/   |  $$$$$$$| $$        |  $$$$/|  $$$$$$$| $$            | $$ | $$ | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$$$$$$/
 \______/  \______/ |__/  |__/    \_/     \_______/|__/         \___/   \_______/|__/            |__/ |__/ |__/ \______/  \_______/ \_______/ \_______/|_______/ 
"""
    print(text)

def exibir_menu():
    menu = r"""    -----------------
    (1) Real em dólar
    -----------------
    (2) Real em euro
    -----------------
"""
    print(menu)  


def main():
    limpar_tela()
    exibir_text()

    while True:
        exibir_menu()
        try:
            converter = int(input('Digite o número que corresponde às moedas que deseja converter (1 ou 2, ou 0 para sair): '))
            limpar_tela()

            if converter == 0:
                print('Saindo...')
                break
            elif converter < 1 or converter > 2:
                print('Digite um valor válido!!!')
            else:
               
                while True:
                    if converter == 1:
                        real = float(input('Digite o valor em real ou 0 para voltar ao menu: '))
                        limpar_tela()
                        if real == 0:
                            print("Voltando ao menu...")
                            break
                        else:
                            print('O valor {} em dólar é: {:.2f}'.format(real, real / 5.52))
                    elif converter == 2:
                        real = float(input('Digite o valor em real ou 0 para voltar ao menu: '))
                        if real == 0:
                            print("Voltando ao menu...")
                            break
                        else:
                            print('O valor {} em euro é: {:.2f}'.format(real, real / 6.15))

        except ValueError:
            print('Por favor, digite um número válido!')


main()
