from dotenv import load_dotenv
import os
from dataclasses import dataclass

@dataclass
class Config:
    llm_provider: str
    openai_api_key: str
    anthropic_api_key: str
    huggingface_api_key: str

def load_config() -> Config:
    load_dotenv()
    
    config = Config(
        llm_provider=os.environ.get('LLM_PROVIDER', 'openai'),
        openai_api_key=os.environ.get('OPENAI_API_KEY'),
        anthropic_api_key=os.environ.get('ANTHROPIC_API_KEY'),
        huggingface_api_key=os.environ.get('HUGGINGFACE_API_KEY'),
    )
    
    if not getattr(config, f"{config.llm_provider}_api_key"):
        raise Exception(f"API key for {config.llm_provider} is not provided in the environment variables.")
    
    return config