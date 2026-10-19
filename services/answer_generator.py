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
    print("Result" , result)
    response = []
    citation = []
    for content in result:
        response.append(content.page_content)
        citation.append(content.metadata['source'])
        
    
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
    
    