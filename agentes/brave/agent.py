from pydantic_ai import Agent
from utils.models import get_model
from utils.server_manager import create_brave_server

async def create_brave_agent(exit_stack):
    """Cria o agente especializado em pesquisas Brave.
    
    Args:
        exit_stack: AsyncExitStack para gerenciar o ciclo de vida do servidor MCP.
        
    Returns:
        Agent: Instância configurada do agente Brave.
    """
    # Cria o servidor MCP para o Brave
    brave_server = create_brave_server()
    await exit_stack.enter_async_context(brave_server)
    
    # Cria o agente Brave
    brave_agent = Agent(
        get_model(),
        system_prompt="""Você é um agente especializado em pesquisas na web usando o Brave Search.
        Seu objetivo é fornecer informações precisas e úteis com base nas consultas dos usuários.
        Use as ferramentas de pesquisa Brave disponíveis para obter informações atualizadas da web.
        Formatando suas respostas com estrutura clara quando apropriado.
        
        Quando realizar pesquisas:
        1. Compreenda o contexto completo da pergunta
        2. Formule consultas eficazes que capturam a essência da pergunta
        3. Analise os resultados e extraia as informações mais relevantes
        4. Apresente a informação de maneira estruturada e fácil de compreender
        5. Cite fontes quando apropriado"""
    )
    
    # Registra as ferramentas do Brave
    brave_agent.use_mcp_server(brave_server)
    
    return brave_agent
