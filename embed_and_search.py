from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def initialize_faiss(chunks):
    embeddings = model.encode(chunks)
    dimension = embeddings[0].shape[0]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    return index, chunks

def get_most_relevant_chunk(question, index, chunks, top_k=3):
    question_embedding = model.encode([question])
    _, I = index.search(np.array(question_embedding), k=top_k)
    return " ".join([chunks[i] for i in I[0]])
