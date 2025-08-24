from Data_Sistemas import SISTEMAS
import os

def clear_screen():
    cmd = 'cls' if os.name=='nt' else 'clear'
    os.system(cmd)
    print('\n' * 100)

def escolher_opção(lista, prompt):
    print(f"\n{prompt}")
    for i, item in enumerate(lista, 1):
        print(f"  {i}. {item}")
    while True:
        escolha = input(">> ").strip()
        if escolha.isdigit():
            idx = int(escolha) - 1
            if 0 <= idx < len(lista):
                return lista[idx]
        print("Opção inválida. Tente de novo.")

def escolher_sistema():
    nomes = list(SISTEMAS.keys())
    return escolher_opção(nomes, 'Escolha o sistema da sua ficha!')

def escolher_raça(sistema):
    lista = SISTEMAS[sistema]['raças']
    prompt = f'Escolha a raça do seu personagem {sistema}!'
    return escolher_opção(lista, prompt)

def escolher_classe(sistema):
    lista = SISTEMAS[sistema].get('classes')
    prompt = f'Escolha a classe do seu personagem {sistema}!'
    return escolher_opção(lista, prompt)

def criar_ficha():
    clear_screen()
    sistema = escolher_sistema()
    raça = escolher_raça(sistema)
    classe = escolher_classe(sistema)
    atributos = {}

    for atr in SISTEMAS[sistema] ['atributos']:
        while True:
            val = input(f"Defina o valor de {atr}: ").strip()
            if val.isdigit():
                atributos[atr] = int(val)
                break
            print("Por favor, digite um número inteiro.")

    ficha = {
        'sistema':   sistema,
        'raça':      raça,
        'classe':    classe,
        'atributos': atributos
    }

    return ficha

def imprimir_ficha(dados):
    print('\n' + '-=' * 12)
    print('   Ficha de Personagem')
    print('-=' * 12)

    for campo in ('sistema', 'raça', 'classes'):
        if campo in dados:
            print(f'{campo.capitalize():12}: {dados[campo]}')

    if 'atributos' in dados:
        print('\nAtributos:')
        for nome, valor in dados['atributos'].items():
            print(f"  {nome:12}: {valor}")

    print('-=' * 12 + '\n')

if __name__ == "__main__":
    print('-=' * 20)
    print('Bem vindo ao sistema de fichas de RPG!')
    print('-=' * 20)
    clear_screen()
    ficha = criar_ficha()
    imprimir_ficha(ficha)