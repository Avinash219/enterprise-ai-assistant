from langchain_text_splitters import RecursiveCharacterTextSplitter

def doc_chunk_list(text: str,chunkSize,chunkOverlapSize):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunkSize,chunk_overlap=chunkOverlapSize)
    return text_splitter.split_text(text)
    