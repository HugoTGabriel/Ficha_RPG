from Data_Sistemas import SISTEMAS

def escolher_opcao(lista, mensagem):
    print(f"\n{mensagem}")
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")

    while True:
        escolha = input(">> ").strip()
        if escolha.isdigit():
            idx = int(escolha) - 1
            if 0 <= idx < len(lista):
                return lista[idx]
        print("Opção inválida.")

def escolher_multiplas(lista, mensagem):
    print(f"\n{mensagem}")
    for i, item in enumerate(lista, 1):
        print(f"{i}. {item}")

    entrada = input(">> ").split(',')
    escolhidas = []

    for e in entrada:
        e = e.strip()
        if e.isdigit():
            idx = int(e) - 1
            if 0 <= idx < len(lista):
                if lista[idx] not in escolhidas:
                    escolhidas.append(lista[idx])

    return escolhidas

def criar_ficha():
    dados = SISTEMAS["Dungeons and Dragons"]

    raca = escolher_opcao(dados["raças"], "Escolha sua raça:")
    classe = escolher_opcao(dados["classes"], "Escolha sua classe:")

    atributos = {}
    print("\nDefina seus atributos:")
    for atr in dados["atributos"]:
        while True:
            valor = input(f"{atr}: ")
            if valor.isdigit():
                atributos[atr] = int(valor)
                break

    pericias = escolher_multiplas(
        dados["pericias"],
        "Escolha suas perícias (separadas por vírgula):"
    )

    return {
        "raça": raca,
        "classe": classe,
        "atributos": atributos,
        "pericias": pericias,
        "nivel": 1,
        "xp": 0
    }


def imprimir_ficha(ficha):
    print("\n=== FICHA DO PERSONAGEM ===")
    print(f"Raça: {ficha['raça']}")
    print(f"Classe: {ficha['classe']}")
    print(f"Nível: {ficha['nivel']} | XP: {ficha['xp']}")

    print("\nAtributos:")
    for k, v in ficha["atributos"].items():
        print(f"- {k}: {v}")

    if ficha["pericias"]:
        print("\nPerícias:")
        for p in ficha["pericias"]:
            print(f"- {p}")

if __name__ == "__main__":
    ficha = criar_ficha()
    imprimir_ficha(ficha)