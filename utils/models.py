import os
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIModel

# Tente importar os provedores Anthropic, mas não falhe se não estiverem disponíveis
try:
    from pydantic_ai.providers.anthropic import AnthropicProvider
    from pydantic_ai.models.anthropic import AnthropicModel
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

def get_model():
    """Retorna uma instância configurada do modelo de linguagem."""
    model_name = os.getenv('MODEL_CHOICE', 'gpt-4o-mini')
    base_url = os.getenv('BASE_URL', 'https://api.openai.com/v1')
    api_key = os.getenv('LLM_API_KEY', 'no-api-key-provided')

    if api_key == 'no-api-key-provided':
        print("⚠️  Aviso: Chave de API não configurada. Configure suas variáveis de ambiente.")
    
    # Verificar se estamos usando o modelo Claude e se o suporte a Anthropic está disponível
    if "claude" in model_name.lower() and ANTHROPIC_AVAILABLE:
        return AnthropicModel(
            model_name,
            provider=AnthropicProvider(api_key=api_key)
        )
    else:
        # Se solicitou Claude mas não está disponível, use OpenAI como fallback
        if "claude" in model_name.lower() and not ANTHROPIC_AVAILABLE:
            print("⚠️  Aviso: Modelo Claude solicitado, mas suporte não está disponível. Usando OpenAI.")
            model_name = "gpt-4o-mini"  # Fallback para modelo OpenAI
            
        return OpenAIModel(
            model_name, 
            provider=OpenAIProvider(base_url=base_url, api_key=api_key)
        )
