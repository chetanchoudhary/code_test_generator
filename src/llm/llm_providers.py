from langchain_openai import OpenAI
from langchain_anthropic import Anthropic
from configuration.settings import Config

def get_llm_provider(config: Config):
    provider = config.llm_provider.lower()
    if provider == "openai":
        return OpenAI(openai_api_key=config.openai_api_key)
    elif provider == "anthropic":
        return Anthropic(anthropic_api_key=config.anthropic_api_key)
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")

def register_llm_provider(container, config: Config):
    container.register('llm', lambda: get_llm_provider(config))