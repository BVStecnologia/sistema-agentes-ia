import os
from typing import List, Dict, Any, Optional
from pydantic_ai.mcp import MCPServerStdio

def create_brave_server() -> MCPServerStdio:
    """Cria um servidor MCP para o Brave Search.
    
    Verifica se a variável de ambiente BRAVE_API_KEY está definida e
    lança um erro de ValueError se não estiver.
    
    Returns:
        MCPServerStdio: Instância configurada do servidor MCP para Brave Search.
        
    Raises:
        ValueError: Se a chave de API do Brave não estiver configurada.
    """
    brave_api_key = os.getenv("BRAVE_API_KEY")
    if not brave_api_key:
        raise ValueError(
            "BRAVE_API_KEY não configurada. " 
            "Por favor, configure esta variável de ambiente no arquivo .env"
        )
        
    return MCPServerStdio(
        'npx', 
        ['-y', '@modelcontextprotocol/server-brave-search', 'stdio'], 
        env={"BRAVE_API_KEY": brave_api_key}
    )

# Funções para servidores que serão implementados no futuro
'''
def create_youtube_server() -> MCPServerStdio:
    """Cria um servidor MCP para o YouTube."""
    return MCPServerStdio(
        'npx', 
        ['-y', '@modelcontextprotocol/server-youtube', 'stdio'], 
        env={"YOUTUBE_API_KEY": os.getenv("YOUTUBE_API_KEY")}
    )

def create_reddit_server() -> MCPServerStdio:
    """Cria um servidor MCP para o Reddit."""
    return MCPServerStdio(
        'npx', 
        ['-y', '@modelcontextprotocol/server-reddit', 'stdio'], 
        env={
            "REDDIT_CLIENT_ID": os.getenv("REDDIT_CLIENT_ID"),
            "REDDIT_CLIENT_SECRET": os.getenv("REDDIT_CLIENT_SECRET"),
            "REDDIT_USER_AGENT": os.getenv("REDDIT_USER_AGENT")
        }
    )

def create_supabase_server() -> MCPServerStdio:
    """Cria um servidor MCP para o Supabase."""
    return MCPServerStdio(
        'npx', 
        ['-y', '@modelcontextprotocol/server-supabase', 'stdio'], 
        env={
            "SUPABASE_URL": os.getenv("SUPABASE_URL"),
            "SUPABASE_KEY": os.getenv("SUPABASE_KEY")
        }
    )
'''

def validate_environment() -> List[str]:
    """Valida as variáveis de ambiente e retorna uma lista de problemas encontrados."""
    problems = []
    
    # Verificar variáveis essenciais
    if not os.getenv("LLM_API_KEY"):
        problems.append("LLM_API_KEY não configurada")
        
    # Verificar variável para o Brave Search
    if not os.getenv("BRAVE_API_KEY"):
        problems.append("BRAVE_API_KEY não configurada")
        
    return problems
