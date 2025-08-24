from typing import List
import numpy as np

class SimpleVectorStore:
    def __init__(self):
        self.vectors = []
        self.documents = []

    def add(self, doc: str, vector: np.ndarray):
        self.documents.append(doc)
        self.vectors.append(vector)

    def search(self, query_vector: np.ndarray, top_k: int = 3) -> List[str]:
        if not self.vectors:
            return []
        vectors = np.array(self.vectors)
        scores = np.dot(vectors, query_vector)
        top_indices = scores.argsort()[-top_k:][::-1]
        return [self.documents[i] for i in top_indices]

def dummy_embedding(text: str) -> np.ndarray:
    # Dummy embedding: convert characters to their ASCII sums normalized
    vec = np.array([ord(c) for c in text])
    return vec / np.linalg.norm(vec)

# Example usage:
# store = SimpleVectorStore()
# emb = dummy_embedding("example doc text")
# store.add("example doc text", emb)
# results = store.search(dummy_embedding("search query"))
