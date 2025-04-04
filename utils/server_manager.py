import os
from typing import List, Dict, Any, Optional
from pydantic_ai.mcp import MCPServerStdio

def create_brave_server() -> MCPServerStdio:
    """Cria um servidor MCP para o Brave Search."""
    return MCPServerStdio(
        'npx', 
        ['-y', '@modelcontextprotocol/server-brave-search', 'stdio'], 
        env={"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
    )

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

def validate_environment() -> List[str]:
    """Valida as variáveis de ambiente e retorna uma lista de problemas encontrados."""
    problems = []
    
    # Verificar variáveis essenciais
    if not os.getenv("LLM_API_KEY"):
        problems.append("LLM_API_KEY não configurada")
        
    # Verificar variáveis para cada serviço
    if not os.getenv("BRAVE_API_KEY"):
        problems.append("BRAVE_API_KEY não configurada")
        
    if not os.getenv("YOUTUBE_API_KEY"):
        problems.append("YOUTUBE_API_KEY não configurada")
        
    if not all([os.getenv("REDDIT_CLIENT_ID"), os.getenv("REDDIT_CLIENT_SECRET"), os.getenv("REDDIT_USER_AGENT")]):
        problems.append("Configuração do Reddit incompleta")
        
    if not all([os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")]):
        problems.append("Configuração do Supabase incompleta")
        
    return problems
