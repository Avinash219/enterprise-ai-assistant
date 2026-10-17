from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from services.document_chunker import doc_chunk_list

persist_directory = "./my_chroma_db"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_doc_vector(filename: str,text: str,chunkSize: int,chunkOverlapSize: int):
    chunks = doc_chunk_list(text,chunkSize,chunkOverlapSize)
    
    for chunk in chunks:
        chunk.metadata['source'] = filename
    
    return Chroma.from_documents(
        documents= chunks,
        embedding= embeddings,
        persist_directory=persist_directory,
        collection_name="knowledge_documents"
    )
    

def get_stored_documents():
    vector_store = Chroma(
        collection_name="knowledge_documents",
        embedding_function=embeddings,
        persist_directory=persist_directory
    )

    return vector_store.get(limit=5)

def search_documents(question: str):
     vector_store = Chroma(
            collection_name="knowledge_documents",
            embedding_function=embeddings,
            persist_directory=persist_directory
        )
     vector_store.similarity_search(question,k=3)
    