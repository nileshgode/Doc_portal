from models.ai_model import SimpleVectorStore, dummy_embedding
from typing import List

vector_store = SimpleVectorStore()

def process_text_file(file_content: bytes) -> str:
    # Decode bytes to string, simple text extraction
    text = file_content.decode('utf-8')
    return text

def add_document_to_store(text: str):
    emb = dummy_embedding(text)
    vector_store.add(text, emb)

def search_documents(query: str, top_k: int = 3) -> List[str]:
    query_emb = dummy_embedding(query)
    results = vector_store.search(query_emb, top_k)
    return results
