from typing import List, Dict


def listar_temas(collection) -> Dict[str, int]:
    """
    Recupera os temas de cada questão, conta e atribui um número a cada um deles,
    Armazenando num dicionário. Só lista questões não utilizadas.

    Returns:
        temas_count: quantidade de questões disponíveis para cada tema.
    """
    temas = collection.distinct('tema')
    temas_count = {tema: collection.count_documents({'tema': tema, 'utilizada': False}) for tema in temas}
    return temas_count


def selecionar_temas(temas_count: Dict[str, int]) -> List[str]:
    """
    Seleciona os temas que o usuário deseja utilizar.

    Returns:
        temas_selecionados: lista de temas selecionados pelo usuário.
    """
    print("\nTemas disponíveis:")
    for i, (tema, count) in enumerate(temas_count.items(), 1):
        print(f"{i}. {tema} ({count} questões)")
    
    selecionados = input("Digite os números dos temas desejados (separados por vírgula): ")
    indices_selecionados = [int(i.strip()) for i in selecionados.split(',')]
    return [list(temas_count.keys())[i-1] for i in indices_selecionados]


def solicitar_numero(prompt: str, min_value: int = 1) -> int:
    """
    Solicita ao usuário um número inteiro.

    Returns:
        numero: número inteiro inserido pelo usuário.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            print(f"Por favor, insira um número maior ou igual a {min_value}.")
        except ValueError:
            print("Por favor, insira um número válido.")