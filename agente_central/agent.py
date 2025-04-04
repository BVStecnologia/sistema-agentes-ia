from contextlib import AsyncExitStack
from pydantic_ai import Agent
from utils.models import get_model
import asyncio

# Importar agentes especializados
from agentes.brave.agent import create_brave_agent
from agentes.youtube.agent import create_youtube_agent
from agentes.reddit.agent import create_reddit_agent
from agentes.supabase.agent import create_supabase_agent

async def create_central_agent():
    """Cria o agente central e os agentes especializados."""
    # Criar stack de contexto para gerenciar todos os servidores MCP
    exit_stack = AsyncExitStack()
    
    # Criar agentes especializados
    brave_agent = await create_brave_agent(exit_stack)
    youtube_agent = await create_youtube_agent(exit_stack)
    reddit_agent = await create_reddit_agent(exit_stack)
    supabase_agent = await create_supabase_agent(exit_stack)
    
    # Criar agente central
    central_agent = Agent(
        get_model(),
        system_prompt="""Você é um agente coordenador principal que delega tarefas para agentes 
        especializados. Analise a consulta do usuário e escolha o agente mais adequado:
        
        - Use o agente Brave para pesquisas na web e informações gerais
        - Use o agente YouTube para buscar ou analisar vídeos
        - Use o agente Reddit para informações de comunidades e discussões
        - Use o agente Supabase para gerenciar dados e banco de dados
        
        Coordene as respostas e forneça uma resposta clara e útil ao usuário.
        Se a consulta exigir a combinação de informações de múltiplos agentes, não hesite em usar
        vários agentes para criar uma resposta completa."""
    )
    
    # Registrar ferramentas para o agente central chamar os especializados
    @central_agent.tool_plain
    async def use_brave_search(query: str) -> dict[str, str]:
        """Pesquisa na web usando o agente especializado em Brave Search.
        Use esta ferramenta quando o usuário precisa de informações da internet.
        
        Args:
            query: A consulta ou instrução para o agente Brave.
            
        Returns:
            Resultado da pesquisa.
        """
        print(f"Chamando agente Brave com a consulta: {query}")
        result = await brave_agent.run(query)
        return {"result": result.data}
    
    @central_agent.tool_plain
    async def use_youtube_agent(query: str) -> dict[str, str]:
        """Busca e analisa vídeos do YouTube usando o agente especializado.
        Use esta ferramenta quando o usuário precisa de informações sobre vídeos.
        
        Args:
            query: A consulta ou instrução para o agente YouTube.
            
        Returns:
            Resultado da busca ou análise de vídeos.
        """
        print(f"Chamando agente YouTube com a consulta: {query}")
        result = await youtube_agent.run(query)
        return {"result": result.data}
    
    @central_agent.tool_plain
    async def use_reddit_agent(query: str) -> dict[str, str]:
        """Busca informações em comunidades do Reddit usando o agente especializado.
        Use esta ferramenta quando o usuário precisa de informações de discussões ou comunidades.
        
        Args:
            query: A consulta ou instrução para o agente Reddit.
            
        Returns:
            Resultado da busca ou análise de posts do Reddit.
        """
        print(f"Chamando agente Reddit com a consulta: {query}")
        result = await reddit_agent.run(query)
        return {"result": result.data}
    
    @central_agent.tool_plain
    async def use_supabase_agent(query: str) -> dict[str, str]:
        """Gerencia dados no Supabase usando o agente especializado.
        Use esta ferramenta quando o usuário precisa armazenar, buscar ou analisar dados.
        
        Args:
            query: A consulta ou instrução para o agente Supabase.
            
        Returns:
            Resultado da operação no banco de dados.
        """
        print(f"Chamando agente Supabase com a consulta: {query}")
        result = await supabase_agent.run(query)
        return {"result": result.data}
    
    return central_agent, exit_stack
