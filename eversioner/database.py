import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_database():
    """
    Obtém a conexão com o MongoDB.

    Returns:
        db: Conexão com o MongoDB.
    """
    mongo_uri = os.getenv('MONGO_URI')
    mongo_db = os.getenv('MONGO_DB')
    mongo_collection = os.getenv('MONGO_COLLECTION')
    
    # Verifica se as variáveis de ambiente estão definidas
    if not all([mongo_uri, mongo_db, mongo_collection]):
        raise ValueError("Configurações do MongoDB não encontradas no arquivo .env")
    
    # Exibe as configurações do MongoDB
    print(f"Conectando ao banco de questões: {mongo_uri}")
    
    # Cria a conexão com o MongoDB
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    return db[mongo_collection]