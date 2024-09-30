from .questions import embaralhar_alternativas
import random


def gerar_provas(questoes, num_versoes, num_alternativas):
    """
    Gera provas a partir de uma lista de questões.

    Args:
        questoes: uma lista de questões.
        num_versoes: o número de provas a serem geradas.
        num_alternativas: o número de alternativas por questão.

    Returns:
        uma tupla contendo duas listas: a primeira lista contém as provas, e a segunda lista contém os gabaritos.
    """
    provas = []
    gabaritos = []
    
    for _ in range(num_versoes):
        prova = []
        gabarito = []
        questoes_embaralhadas = random.sample(questoes, len(questoes))
        
        for i, questao in enumerate(questoes_embaralhadas, 1):
            alternativas_embaralhadas = embaralhar_alternativas(questao, num_alternativas)
            prova.append({
                'numero': i,
                'enunciado': questao['enunciado'],
                'alternativas': alternativas_embaralhadas
            })
            
            # Encontrar a posição da alternativa correta
            posicao_correta = alternativas_embaralhadas.index(questao['alternativa_correta'])
            gabarito.append(f"{i}-{chr(65 + posicao_correta)}")
        
        provas.append(prova)
        gabaritos.append(gabarito)
    
    return provas, gabaritos