import random
from typing import List, Dict
from pymongo import UpdateOne


def recuperar_questoes(collection, temas: List[str]) -> List[Dict]:
    """
    Recupera questões não utilizadas de uma coleção de questões.

    Args:
        collection: a coleção de questões.
        temas: uma lista de temas para filtrar as questões.

    Returns:
        uma lista de questões não utilizadas que correspondem aos temas fornecidos.
    """
    print(f"Tentando recuperar questões da coleção: {collection.name}")
    print(f"Total de questões no banco de dados: {collection.count_documents({})}")
    print(f"Questões marcadas como utilizadas: {collection.count_documents({'utilizada': True})}")
    print(f"Questões não utilizadas: {collection.count_documents({'utilizada': False})}")
    
    questoes = list(collection.find({"tema": {"$in": temas}, "utilizada": False}))
    print(f"Número de questões recuperadas: {len(questoes)}")
    
    if not questoes:
        print("Nenhuma questão não utilizada encontrada no banco de dados.")
    
    return questoes


def embaralhar_alternativas(questao, num_alternativas):
    """
    Embaralha as alternativas de uma questão.

    Args:
        questao: a questão a ser embaralhada.
        num_alternativas: o número de alternativas a serem embaralhadas.

    Returns:
        uma lista de alternativas embaralhadas.
    """
    alternativas = [
        questao['alternativa_correta'],
        questao['alternativa_1'],
        questao['alternativa_2'],
        questao['alternativa_3']
    ][:num_alternativas]
    random.shuffle(alternativas)
    return alternativas


def marcar_questoes_como_utilizadas(collection, questoes: List[Dict], ano: int):
    """
    Marca as questões como utilizadas.

    Args:
        collection: a coleção de questões.
        questoes: uma lista de questões.
        ano: o ano em que as questões foram utilizadas.
    """
    if not questoes:
        print("Nenhuma questão para marcar como utilizada.")
        return 0
    operacoes = [
        UpdateOne(
            {"_id": questao["_id"]},
            {"$set": {"utilizada": True, "ano_utilizacao": ano}}
        )
        for questao in questoes
    ]
    resultado = collection.bulk_write(operacoes)
    return resultado.modified_count
