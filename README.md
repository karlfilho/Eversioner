# Gerador de Provas

Este projeto é um gerador automatizado de provas para o curso de Medicina da Universidade de Santo Amaro, focado no Núcleo de Saúde da Mulher.

## Funcionalidades

- Conexão com banco de dados MongoDB para recuperação de questões
- Seleção de temas para a prova
- Geração de múltiplas versões da prova com questões e alternativas embaralhadas
- Criação de gabaritos para cada versão da prova
- Exportação das provas e gabaritos em formato .docx
- Marcação de questões utilizadas no banco de dados

## Requisitos

- Python 3.7+
- MongoDB
- Bibliotecas Python: pymongo, python-dotenv, python-docx

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/karlfilho/eversioner.git
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente no arquivo `.env`:
   ```
   MONGO_URI=sua_uri_do_mongodb
   MONGO_DB=nome_do_seu_banco
   MONGO_COLLECTION=nome_da_sua_colecao
   ```

## Uso

Execute o script principal:

```
python main.py
```


Siga as instruções no terminal para selecionar temas, número de versões e alternativas por questão.

## Estrutura do Projeto

- `main.py`: Script principal que coordena o fluxo do programa
- `database.py`: Gerencia a conexão com o MongoDB
- `questions.py`: Lida com a recuperação e manipulação das questões
- `exam.py`: Gera as provas e gabaritos
- `docx.py`: Cria os arquivos .docx das provas e gabaritos
- `utils.py`: Funções utilitárias

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue para discutir mudanças maiores antes de submeter um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
