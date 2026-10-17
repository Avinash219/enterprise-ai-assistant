from langchain_text_splitters import RecursiveCharacterTextSplitter


def doc_chunk_list(text: str,chunkSize: int,chunkOverlapSize: int):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunkSize,chunk_overlap=chunkOverlapSize)
    return text_splitter.create_documents([text])
""" 
def embed_doc(text: str,chunkSize: int,chunkOverlapSize: int):
    embedDoc = doc_chunk_list(text,chunkSize,chunkOverlapSize)
    return embeddings.embed_documents(embedDoc) """
    
    