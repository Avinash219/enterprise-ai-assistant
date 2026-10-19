from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

from services.vector_store import search_documents

def llm_init(api_key: str,model_name: str):
    return ChatAnthropic(
        api_key= api_key,
        model_name= model_name
    )
    

async def answer_question(model: ChatAnthropic,question: str):
    result = search_documents(question)
    if len(result) == 0:
            return {
                "res" : "I couldn't find relevant information in the uploaded documents.",
                "citation" : []
            }
    score = result[0][-1]
    if score >= 1:
        return {
            "res" : "I couldn't find relevant information in the uploaded documents.",
            "citation" : []
        }
    response = []
    citation = []
    for document,score in result:
        response.append(document.page_content)
        citation.append(document.metadata['source'])
        
    
    prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Answer the user's question based only on the provided context.

        Context:
        {context}

        Instructions:
        1. Answer only using information explicitly available in the context.
        2. If the context answers only part of the question, answer that part.
        3. Clearly state when information required for another part is not available in the context.
        4. Do not use your general knowledge or invent information to fill gaps.
        5. If none of the question can be answered from the context, say that you don't have enough information."""
    ),
    ("human", "{question}")
])
    
    chain = prompt | model
    
    res= await chain.ainvoke({
        "context" : "\n".join(response),
        "question" : question
    })
    
    return {
        "res" : res,
        "citation" : list(dict.fromkeys(citation))
    }
    
    