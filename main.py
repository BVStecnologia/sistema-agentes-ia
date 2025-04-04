import asyncio
import os
import sys
import traceback
from dotenv import load_dotenv
from contextlib import AsyncExitStack
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

# Importar agente central
from agente_central.agent import create_central_agent
from utils.server_manager import validate_environment

# Carregar variáveis de ambiente
load_dotenv()

async def main():
    """Função principal que inicia o sistema de agentes."""
    console = Console()
    
    # Banner de boas-vindas
    console.print(Panel.fit(
        Text("Sistema Hierárquico de Agentes IA", style="bold cyan"),
        subtitle="v0.1.0 - Agente Brave Search",
        border_style="cyan"
    ))
    
    # Verificar variáveis de ambiente
    problems = validate_environment()
    if problems:
        console.print("\n[bold red]⚠️  Problemas de configuração encontrados:[/bold red]")
        for problem in problems:
            console.print(f"[red]- {problem}[/red]")
        console.print("\n[yellow]Consulte GETTING_STARTED.md para instruções de configuração.[/yellow]")
        return
    
    try:
        # Criar agente central (que criará o agente Brave)
        console.print("\n[yellow]Inicializando agentes... (isso pode levar alguns segundos)[/yellow]")
        central_agent, exit_stack = await create_central_agent()
        console.print("[green]✓ Agentes inicializados com sucesso![/green]")
    except Exception as e:
        console.print(f"\n[bold red]❌ Erro ao inicializar agentes:[/bold red] {str(e)}")
        console.print("\n[dim]Detalhes técnicos do erro:[/dim]")
        console.print(f"[dim]{traceback.format_exc()}[/dim]")
        console.print("\n[yellow]Verifique:\n1. Se o Node.js está instalado\n2. Se o servidor MCP do Brave foi instalado com: npm install -g @modelcontextprotocol/server-brave-search\n3. Se as chaves de API estão configuradas corretamente no arquivo .env[/yellow]")
        return
    
    # Instruções de uso
    console.print("\n[cyan]Instruções:[/cyan]")
    console.print("• Digite suas perguntas para pesquisar na web usando o Brave Search")
    console.print("• Digite [bold]'sair'[/bold], [bold]'exit'[/bold] ou [bold]'quit'[/bold] para encerrar")
    console.print("• Digite [bold]'ajuda'[/bold] ou [bold]'help'[/bold] para ver estas instruções novamente")
    console.print("• Digite [bold]'debug'[/bold] para ver informações de diagnóstico")
    
    # Histórico de mensagens
    messages = []
    
    # Loop principal de interação
    async with exit_stack:
        console.print("\n[green]Sistema pronto para receber consultas![/green]")
        
        while True:
            # Entrada do usuário
            user_input = console.input("\n[bold cyan][Você][/bold cyan] ")
            
            # Verificar comandos especiais
            if user_input.lower() in ['sair', 'exit', 'quit']:
                console.print("\n[yellow]Encerrando sistema... Até mais! 👋[/yellow]")
                break
            
            if user_input.lower() in ['ajuda', 'help', '?']:
                console.print("\n[cyan]Instruções:[/cyan]")
                console.print("• Digite suas perguntas para pesquisar na web usando o Brave Search")
                console.print("• Digite [bold]'sair'[/bold], [bold]'exit'[/bold] ou [bold]'quit'[/bold] para encerrar")
                console.print("• Digite [bold]'ajuda'[/bold] ou [bold]'help'[/bold] para ver estas instruções")
                console.print("• Digite [bold]'debug'[/bold] para ver informações de diagnóstico")
                continue
            
            if user_input.lower() in ['debug', 'diagnóstico', 'diagnostico']:
                console.print("\n[cyan]Informações de Diagnóstico:[/cyan]")
                console.print(f"• Modelo LLM: {os.getenv('MODEL_CHOICE', 'gpt-4o-mini')}")
                console.print(f"• API Base URL: {os.getenv('BASE_URL', 'https://api.openai.com/v1')}")
                console.print(f"• API Key configurada: {'Sim' if os.getenv('LLM_API_KEY') else 'Não'}")
                console.print(f"• Brave API Key configurada: {'Sim' if os.getenv('BRAVE_API_KEY') else 'Não'}")
                try:
                    from pydantic_ai import __version__ as pydantic_ai_version
                    console.print(f"• Versão pydantic-ai: {pydantic_ai_version}")
                except ImportError:
                    console.print("• pydantic-ai: Não foi possível determinar a versão")
                continue
            
            if not user_input.strip():
                continue
            
            try:
                # Processa a entrada e obtém a resposta
                console.print("\n[bold green][Assistente][/bold green]")
                with Live('', console=console, vertical_overflow='visible') as live:
                    async with central_agent.run_stream(
                        user_input, message_history=messages
                    ) as result:
                        current_message = ""
                        async for message in result.stream_text(delta=True):
                            current_message += message
                            live.update(Markdown(current_message))
                        
                        # Adiciona mensagens ao histórico
                        messages.extend(result.all_messages())
                
            except Exception as e:
                console.print(f"\n[bold red][Erro][/bold red] Ocorreu um problema: {str(e)}")
                console.print("[yellow]Tente novamente ou digite 'debug' para ver informações de diagnóstico.[/yellow]")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário. Até mais! 👋")
        sys.exit(0)
