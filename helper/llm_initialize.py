from anthropic import AsyncAnthropic

def llm_init(api_key: str):
    return AsyncAnthropic(
        api_key= api_key
    )
    