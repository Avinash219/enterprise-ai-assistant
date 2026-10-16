from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def doc_chunk_list(text: str,chunkSize: int,chunkOverlapSize: int):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunkSize,chunk_overlap=chunkOverlapSize)
    return text_splitter.split_text(text)

def embed_doc(text: str,chunkSize: int,chunkOverlapSize: int):
    embedDoc = doc_chunk_list(text,chunkSize,chunkOverlapSize)
    return embeddings.embed_documents(embedDoc)
    
    