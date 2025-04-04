import os
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.anthropic import AnthropicProvider
from pydantic_ai.models.anthropic import AnthropicModel

def get_model():
    """Retorna uma instância configurada do modelo de linguagem."""
    model_name = os.getenv('MODEL_CHOICE', 'gpt-4o-mini')
    base_url = os.getenv('BASE_URL', 'https://api.openai.com/v1')
    api_key = os.getenv('LLM_API_KEY', 'no-api-key-provided')

    if api_key == 'no-api-key-provided':
        print("⚠️  Aviso: Chave de API não configurada. Configure suas variáveis de ambiente.")
    
    # Verificar se estamos usando o modelo Claude
    if "claude" in model_name.lower():
        return AnthropicModel(
            model_name,
            provider=AnthropicProvider(api_key=api_key)
        )
    else:
        return OpenAIModel(
            model_name, 
            provider=OpenAIProvider(base_url=base_url, api_key=api_key)
        )
