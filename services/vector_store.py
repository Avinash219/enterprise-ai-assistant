from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from services.document_chunker import doc_chunk_list

persist_directory = "./my_chroma_db"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_doc_vector(filename: str,text: str,chunkSize: int,chunkOverlapSize: int):
    return Chroma.from_documents(
        documents= doc_chunk_list(text,chunkSize,chunkOverlapSize),
        embedding= embeddings,
        persist_directory=persist_directory,
        collection_name=filename
    )
    