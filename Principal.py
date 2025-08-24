# --- Importações ---
# A variável SISTEMAS é importada de um arquivo separado para manter os dados organizados.
from Data_Sistemas import SISTEMAS 
import time
import json

# --- Funções de Interface com o Usuário ---

def escolherOpção(lista, prompt):
    """
    Exibe uma lista de opções numeradas para o usuário e garante que ele escolha uma válida.

    Args:
        lista (list): A lista de itens a serem exibidos como opções.
        prompt (str): A mensagem a ser exibida para o usuário antes da lista.

    Returns:
        any: O item da lista que foi escolhido pelo usuário.
    """
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

# --- Funções de Criação da Ficha ---

def escolherSistema():
    """Mostra os sistemas de RPG disponíveis e retorna a escolha do usuário."""
    nomes = list(SISTEMAS.keys())
    return escolherOpção(nomes, 'Escolha o sistema da sua ficha!')

def escolherCaracteristica(sistema, caracteristica_plural, caracteristica_singular):
    """
    Função genérica para escolher uma característica (raça, classe, etc.) de um sistema.
    """
    lista = SISTEMAS[sistema].get(caracteristica_plural)
    prompt = f'Escolha a {caracteristica_singular} do seu personagem.'
    return escolherOpção(lista, prompt)

def escolherPericias(sistema):
    """
    Permite ao usuário escolher múltiplas perícias a partir de uma lista,
    digitando os números separados por vírgula.
    """
    lista = SISTEMAS[sistema].get('pericias')
    prompt = f'Escolha as perícias (números separados por vírgula):'
    print(f'\n{prompt}')
    for i, nome in enumerate(lista, 1):
        print(f' {i}. {nome}')
    
    entrada = input(">> ")
    partes = entrada.split(',')
    indices = []
    for pedaço in partes:
        numero_str = pedaço.strip()
        if numero_str.isdigit():
            idx = int(numero_str) - 1
            if 0 <= idx < len(lista):
                indices.append(idx)
            else:
                print(f"Número '{numero_str}' fora do intervalo.")
        else:
            print(f"Entrada '{numero_str}' não é um número.")
    
    periciasEscolhidas = [lista[i] for i in indices]
    
    # Remove duplicatas mantendo a ordem de escolha
    unicas = []
    for p in periciasEscolhidas:
        if p not in unicas:
            unicas.append(p)
    
    return unicas

def criarFicha():
    """
    Guia o usuário através de todo o processo de criação de uma nova ficha.
    """
    sistema = escolherSistema()
    raça = escolherCaracteristica(sistema, 'raças', 'raça')
    classe = escolherCaracteristica(sistema, 'classes', 'classe')
    
    atributos = {}
    print("\n--- Defina seus Atributos ---")
    for atr in SISTEMAS[sistema]['atributos']:
        while True:
            val = input(f"Valor de {atr}: ").strip()
            if val.isdigit():
                atributos[atr] = int(val)
                break
            print("Por favor, digite um número inteiro.")
            
    pericias = escolherPericias(sistema)
    
    ficha = {
        'sistema':   sistema,
        'raça':      raça,
        'classe':    classe,
        'atributos': atributos,
        'pericias':  pericias
    }
    return ficha

# --- Funções de Exibição e Arquivo ---

def imprimirFicha(dados):
    """Imprime uma ficha formatada no terminal."""
    if dados is None:
        return # Não faz nada se a ficha for inválida
        
    print('\n' + '-=' * 15)
    print('     Ficha de Personagem')
    print('-=' * 15)
    
    # Imprime os campos principais
    print(f"{'Sistema:':<12} {dados.get('sistema', 'N/A')}")
    print(f"{'Raça:':<12} {dados.get('raça', 'N/A')}")
    print(f"{'Classe:':<12} {dados.get('classe', 'N/A')}")
    
    # Imprime os atributos
    if 'atributos' in dados:
        print('\n--- Atributos ---')
        for nome, valor in dados['atributos'].items():
            print(f"  {nome:<12}: {valor}")
            
    # Imprime as perícias
    if 'pericias' in dados and dados['pericias']:
        print('\n--- Perícias ---')
        # Junta todas as perícias em uma única string separada por vírgula
        print("  " + ", ".join(dados['pericias']))
        
    print('-=' * 15 + '\n')

def salvarFicha(dados):
    """Salva o dicionário de uma ficha em um arquivo .json."""
    nomeArquivo = input('Digite um nome para o arquivo da sua ficha (ex: Gandalf): ') + '.json'
    with open(nomeArquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print(f"Ficha salva com sucesso em {nomeArquivo}!")

def carregarFicha():
    """Carrega uma ficha de um arquivo .json e a retorna como um dicionário."""
    nomeArquivo = input("Digite o nome da ficha que deseja carregar (ex: Gandalf.json): ")
    try:
        with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            print("Ficha carregada com sucesso!")
            return dados
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro: O arquivo não é um JSON válido.")
        return None

def exportarTXT():
    """Carrega uma ficha .json e exporta seus dados para um arquivo .txt formatado."""
    nomeJson = input('Qual ficha (.json) você quer exportar? ')
    try:
        with open(nomeJson, 'r', encoding='utf-8') as arquivoJson:
            ficha = json.load(arquivoJson)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Não foi possível carregar o arquivo: {e}")
        return

    nomeTXT = nomeJson.replace('.json', '.txt')
    with open(nomeTXT, 'w', encoding='utf-8') as arquivo_txt:
        arquivo_txt.write("--- Ficha de Personagem ---\n\n")
        arquivo_txt.write(f"Sistema: {ficha.get('sistema', 'N/A')}\n")
        arquivo_txt.write(f"Raça: {ficha.get('raça', 'N/A')}\n")
        arquivo_txt.write(f"Classe: {ficha.get('classe', 'N/A')}\n")

        if 'atributos' in ficha:
            arquivo_txt.write('\n--- Atributos ---\n')
            for nome, valor in ficha['atributos'].items():
                arquivo_txt.write(f"{nome}: {valor}\n")

        if 'pericias' in ficha and ficha['pericias']:
            arquivo_txt.write('\n--- Perícias ---\n')
            for pericia in ficha['pericias']:
                arquivo_txt.write(f"- {pericia}\n")

    print(f'Ficha exportada com sucesso para {nomeTXT}!')

# --- Menus de Navegação ---

def menuFicha(fichaAtiva):
    """
    Menu de ações para uma ficha que já foi criada ou carregada.
    """
    while True:
        print("\n--- Opções da Ficha ---")
        print("1. Salvar (JSON)")
        print("2. Exportar para Bloco de Notas (TXT)")
        print("3. Voltar ao menu principal")
        
        escolha = input(">> ")
        if escolha == '1':
            salvarFicha(fichaAtiva)
        elif escolha == '2':
            exportarTXT()
        elif escolha == '3':
            break # Sai deste loop e volta para o menu principal
        else:
            print('Opção Inválida')

def menu():
    """
    Menu principal do programa. Controla o fluxo de criação e carregamento de fichas.
    """
    while True:
        print("\n--- Menu Principal ---")
        print("1. Criar nova ficha")
        print("2. Carregar ficha existente")
        print("3. Sair")
        
        escolha = input(">> ")
        if escolha == '1':
            fichaAtual = criarFicha()
            imprimirFicha(fichaAtual)
            menuFicha(fichaAtual)
        elif escolha == '2':
            fichaAtual = carregarFicha()
            if fichaAtual is not None:
                imprimirFicha(fichaAtual)
                menuFicha(fichaAtual)
        elif escolha == '3':
            print("Obrigado por utilizar o programa!")
            break
        else:
            print('Opção inválida!')

# --- Ponto de Entrada do Programa ---

if __name__ == "__main__":
    print('-=' * 20)
    print('Bem vindo ao sistema de fichas de RPG!')
    print('-=' * 20)
    
    time.sleep(1)
    menu()