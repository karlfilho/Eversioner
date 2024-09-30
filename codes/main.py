from .database import get_database
from .questions import recuperar_questoes, marcar_questoes_como_utilizadas
from .utils import solicitar_numero, selecionar_temas, listar_temas
from .exam import gerar_provas
from .docx import salvar_prova, salvar_gabaritos
from datetime import datetime


def main():
    """
    Função principal que inicia o programa.
    """
    # Conectar ao banco de dados
    print("Iniciando o programa...")
    collection = get_database()
    print("Conexão com o banco de dados estabelecida.")
    
    # Listar e selecionar temas
    temas_count = listar_temas(collection)
    temas_selecionados = selecionar_temas(temas_count)
    
    # Solicitar número de versões e alternativas
    num_versoes = solicitar_numero("Quantas versões da prova deseja gerar? ")
    num_alternativas = solicitar_numero("Quantas alternativas por questão? ", 2)
    
    questoes = recuperar_questoes(collection, temas_selecionados)
    
    # Exibir resumo da prova a ser confeccionada
    print("\nResumo da prova a ser confeccionada:")
    for tema in temas_selecionados:
        print(f"- {tema}: {temas_count[tema]} questões")
    print(f"Total de questões: {len(questoes)}")
    print(f"Total de alternativas por questão: {num_alternativas}")
    print(f"Número de versões: {num_versoes}")
    
    # Solicitar confirmação para prosseguir com a geração
    confirmacao = input("\nDeseja prosseguir com a geração das provas? (s/n): ")
    if confirmacao.lower() != 's':
        print("Operação cancelada.")
        return
    
    # Obter avc_numero e data_prova
    avc_numero = input("Digite o número da AVC: ")
    data_prova = input("Digite a data da prova (ex: 15 de Maio de 2024): ")

    # Gerar provas
    provas, gabaritos = gerar_provas(questoes, num_versoes, num_alternativas)
    
    for i, (prova, gabarito) in enumerate(zip(provas, gabaritos), 1):
        salvar_prova(prova, gabarito, i, avc_numero, data_prova)
    
    salvar_gabaritos(gabaritos, avc_numero, data_prova)
    
    # Marcar questões como utilizadas
    ano_atual = datetime.now().year
    marcar_questoes_como_utilizadas(collection, questoes, ano_atual)
    print("Questões marcadas como utilizadas no banco de dados.")

if __name__ == "__main__":
    main()