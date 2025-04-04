import os
import subprocess
from typing import List, Dict, Any, Optional
from pydantic_ai.mcp import MCPServerStdio

def check_npx_installed():
    """Verifica se o npx está instalado no sistema."""
    try:
        subprocess.run(['npx', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def check_mcp_package_installed(package_name):
    """Verifica se um pacote MCP específico está instalado."""
    try:
        # Tenta listar informações do pacote para ver se está instalado
        result = subprocess.run(['npx', package_name, '--help'],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              text=True,
                              check=False)
        # Se o comando não retornar erro, o pacote está instalado
        return result.returncode == 0
    except Exception:
        return False

def create_brave_server() -> MCPServerStdio:
    """Cria um servidor MCP para o Brave Search.
    
    Verifica se a variável de ambiente BRAVE_API_KEY está definida e
    lança um erro de ValueError se não estiver.
    
    Returns:
        MCPServerStdio: Instância configurada do servidor MCP para Brave Search.
        
    Raises:
        ValueError: Se a chave de API do Brave não estiver configurada.
        RuntimeError: Se npx não estiver instalado ou o pacote MCP não for encontrado.
    """
    # Verificar dependências
    if not check_npx_installed():
        raise RuntimeError(
            "npx não encontrado. Por favor, instale o Node.js e o npm: " 
            "https://nodejs.org/en/download/"
        )
    
    package_name = '@modelcontextprotocol/server-brave-search'
    if not check_mcp_package_installed(package_name):
        raise RuntimeError(
            f"Pacote {package_name} não encontrado. " 
            f"Por favor, instale-o com: npm install -g {package_name}"
        )
    
    # Verificar variáveis de ambiente
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
    
    # Verificar dependências externas
    if not check_npx_installed():
        problems.append("Node.js/npx não encontrado - necessário para os servidores MCP")
    else:
        # Só verifica o pacote se npx estiver instalado
        if not check_mcp_package_installed('@modelcontextprotocol/server-brave-search'):
            problems.append("Pacote MCP do Brave não encontrado - execute: npm install -g @modelcontextprotocol/server-brave-search")
        
    return problems
