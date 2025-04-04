import asyncio
import os
from dotenv import load_dotenv
from contextlib import AsyncExitStack
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live

# Importar agente central
from agente_central.agent import create_central_agent

load_dotenv()

async def main():
    """Função principal que inicia o sistema de agentes."""
    print("🤖 Sistema Hierárquico de Agentes IA")
    print("Digite 'sair' para encerrar o programa.\n")
    
    # Cria o agente central (que por sua vez criará os agentes especializados)
    central_agent, exit_stack = await create_central_agent()
    
    # Inicializa console para renderização formatada
    console = Console()
    
    # Histórico de mensagens
    messages = []
    
    # Loop principal de interação
    async with exit_stack:
        print("Sistema inicializado e pronto para receber consultas!\n")
        
        while True:
            # Entrada do usuário
            user_input = input("\n[Você] ")
            
            # Verifica se o usuário quer sair
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print("Até mais! 👋")
                break
            
            try:
                # Processa a entrada e obtém a resposta
                print("\n[Assistente]")
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
                print(f"\n[Erro] Ocorreu um erro: {str(e)}")
                print("Tente novamente ou verifique as configurações.")

if __name__ == "__main__":
    asyncio.run(main())
