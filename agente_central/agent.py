from contextlib import AsyncExitStack
from pydantic_ai import Agent
from utils.models import get_model

# Importar apenas o agente Brave
from agentes.brave.agent import create_brave_agent

async def create_central_agent():
    """Cria o agente central e o agente especializado Brave."""
    # Criar stack de contexto para gerenciar o servidor MCP
    exit_stack = AsyncExitStack()
    
    # Criar apenas o agente Brave
    brave_agent = await create_brave_agent(exit_stack)
    
    # Criar agente central simplificado
    central_agent = Agent(
        get_model(),
        system_prompt="""Você é um agente coordenador que utiliza o agente especializado Brave.
        Analise a consulta do usuário e use o agente Brave para pesquisas na web e informações gerais.
        Coordene as respostas e forneça uma resposta clara e útil ao usuário."""
    )
    
    # Registrar apenas a ferramenta para o agente Brave
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
    
    return central_agent, exit_stack
