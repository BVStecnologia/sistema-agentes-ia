# Sistema de Agentes IA Hierárquico

Este é um sistema hierárquico de agentes de IA que usa o Model Context Protocol (MCP) para integração com vários serviços, incluindo Brave Search, YouTube, Reddit e Supabase.

## Características

- **Arquitetura Hierárquica**: Um agente central que coordena agentes especializados
- **Integração com APIs**: Brave Search, YouTube, Reddit e Supabase
- **Facilmente Extensível**: Estrutura modular para adicionar novos agentes
- **Testabilidade Individual**: Cada agente pode ser testado separadamente

## Estrutura do Projeto

```
sistema-agentes-ia/
│
├── main.py                 # Arquivo principal que inicia o sistema
├── requirements.txt        # Dependências do projeto
├── .env.example           # Exemplo de variáveis de ambiente
│
├── agente_central/         # Agente coordenador principal
│   ├── __init__.py
│   ├── agent.py            # Implementação do agente central
│   └── README.md           # Documentação do agente central
│
├── agentes/                # Pasta com todos os agentes especializados
│   │
│   ├── brave/              # Agente para Brave Search
│   │   ├── __init__.py
│   │   ├── agent.py        # Implementação do agente Brave
│   │   ├── tools.py        # Ferramentas específicas do Brave
│   │   └── README.md       # Documentação do agente Brave
│   │
│   ├── youtube/            # Agente para YouTube
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── tools.py
│   │   └── README.md
│   │
│   ├── reddit/             # Agente para Reddit
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── tools.py
│   │   └── README.md
│   │
│   └── supabase/           # Agente para Supabase
│       ├── __init__.py
│       ├── agent.py
│       ├── tools.py
│       └── README.md
│
└── utils/                  # Utilitários compartilhados
    ├── __init__.py
    ├── models.py           # Função de acesso aos modelos
    └── server_manager.py   # Gerenciador de servidores MCP
```

## Instalação

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

5. Instale os pacotes Node.js necessários (requer Node.js e npm):
```bash
npm install -g @modelcontextprotocol/server-brave-search
npm install -g @modelcontextprotocol/server-youtube
npm install -g @modelcontextprotocol/server-reddit
```

## Uso

### Iniciando o Sistema Completo

Para iniciar o sistema completo com todos os agentes:

```bash
python main.py
```

### Testando Agentes Individuais

Cada agente pode ser testado individualmente usando seus scripts de teste:

```bash
# Testar apenas o agente Brave
python agentes/brave/test.py

# Testar apenas o agente YouTube
python agentes/youtube/test.py

# E assim por diante...
```

## Adicionando Novos Agentes

Para adicionar um novo agente ao sistema:

1. Crie uma nova pasta na estrutura de `agentes/`
2. Implemente os arquivos `agent.py`, `tools.py` e `README.md`
3. Atualize o agente central para incluir seu novo agente

Consulte o README de cada pasta de agente para obter detalhes específicos de implementação.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

MIT