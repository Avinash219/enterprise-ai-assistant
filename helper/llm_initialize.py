from langchain_anthropic import ChatAnthropic

def llm_init(api_key: str,model_name: str):
    return ChatAnthropic(
        api_key= api_key,
        model_name= model_name
    )
    