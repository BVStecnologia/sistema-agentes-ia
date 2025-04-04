# Sistema de Agentes IA Hierárquico

Este é um sistema hierárquico de agentes de IA que usa o Model Context Protocol (MCP) para integração com serviços externos. A versão atual inclui apenas o agente Brave Search, com planos para expandir para YouTube, Reddit e Supabase no futuro.

## Características

- **Arquitetura Hierárquica**: Um agente central que coordena agentes especializados
- **Integração com Brave Search**: Permite realizar pesquisas na web através da API do Brave
- **Facilmente Extensível**: Estrutura modular para adicionar novos agentes
- **Baseado em MCP**: Utiliza o Model Context Protocol para comunicação padronizada

## Requisitos

- Python 3.9+
- Node.js 14+ e npm
- Chave de API do OpenAI (ou outro provedor LLM compatível)
- Chave de API do Brave Search

## Instalação Rápida

1. Clone este repositório:
```bash
git clone https://github.com/BVStecnologia/sistema-agentes-ia.git
cd sistema-agentes-ia
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv

# No Windows
venv\Scripts\activate

# No macOS/Linux
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure suas variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas chaves de API
```

5. Instale o pacote Node.js necessário:
```bash
npm install -g @modelcontextprotocol/server-brave-search
```

## Uso

### Iniciando o Sistema

Para iniciar o sistema:

```bash
python main.py
```

Isso abrirá uma interface de linha de comando onde você pode fazer perguntas e receber respostas baseadas em pesquisas na web através do Brave Search.

### Comandos Disponíveis

- Digite qualquer pergunta para pesquisar na web
- `ajuda` ou `help` - Mostra instruções de uso
- `debug` - Mostra informações de diagnóstico do sistema
- `sair`, `exit` ou `quit` - Encerra o programa

## Solução de Problemas

Se encontrar problemas ao iniciar o sistema, verifique:

1. Se o Node.js está instalado e funcionando
2. Se o servidor MCP do Brave foi instalado corretamente
3. Se as chaves de API estão configuradas no arquivo .env

Veja o arquivo [GETTING_STARTED.md](GETTING_STARTED.md) para instruções detalhadas de solução de problemas.

## Estrutura do Projeto

```
sistema-agentes-ia/
│
├── main.py                 # Arquivo principal que inicia o sistema
├── requirements.txt        # Dependências do projeto
├── .env.example           # Exemplo de variáveis de ambiente
├── GETTING_STARTED.md     # Guia detalhado de inicialização
│
├── agente_central/         # Agente coordenador principal
│   ├── __init__.py
│   └── agent.py            # Implementação do agente central
│
├── agentes/                # Pasta com todos os agentes especializados
│   │
│   └── brave/              # Agente para Brave Search
│       ├── __init__.py
│       ├── agent.py        # Implementação do agente Brave
│       ├── tools.py        # Ferramentas específicas do Brave
│       └── README.md       # Documentação do agente Brave
│
└── utils/                  # Utilitários compartilhados
    ├── __init__.py
    ├── models.py           # Função de acesso aos modelos
    └── server_manager.py   # Gerenciador de servidores MCP
```

## Guia Detalhado

Para instruções mais detalhadas sobre configuração, solução de problemas e como expandir o sistema, consulte o arquivo [GETTING_STARTED.md](GETTING_STARTED.md).

## Plano de Desenvolvimento Futuro

1. **Fase 1**: Agente Brave Search (Atual)
2. **Fase 2**: Adicionar agente YouTube
3. **Fase 3**: Adicionar agente Reddit
4. **Fase 4**: Adicionar agente Supabase
5. **Fase 5**: Melhorias na interface e experiência do usuário

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

MIT
