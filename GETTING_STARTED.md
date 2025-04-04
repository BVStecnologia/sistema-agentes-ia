# Guia de Inicialização do Sistema de Agentes IA

Este guia fornece instruções detalhadas para configurar e executar o sistema de agentes IA, começando apenas com o agente Brave Search.

## Pré-requisitos

### Software Necessário

- Python 3.9 ou superior
- Node.js 14 ou superior
- npm (geralmente vem com o Node.js)
- Git

### Chaves de API

- **OpenAI API Key**: Para o modelo de linguagem (pode ser substituído por outro provedor)
- **Brave Search API Key**: Para o agente de pesquisa ([Obtenha aqui](https://brave.com/search/api/))

## Instalação Passo a Passo

### 1. Clone o Repositório

```bash
git clone https://github.com/BVStecnologia/sistema-agentes-ia.git
cd sistema-agentes-ia
```

### 2. Configure o Ambiente Python

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Instale o Servidor MCP do Brave

```bash
npm install -g @modelcontextprotocol/server-brave-search
```

### 4. Configure as Variáveis de Ambiente

Crie um arquivo `.env` com base no exemplo:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas chaves de API:

```
# Configuração do modelo de linguagem
MODEL_CHOICE=gpt-4o-mini
BASE_URL=https://api.openai.com/v1
LLM_API_KEY=sua_chave_openai_aqui

# Chave de API do Brave Search
BRAVE_API_KEY=sua_chave_brave_aqui
```

## Execução do Sistema

### Iniciar o Sistema

```bash
python main.py
```

Isso iniciará a interface de linha de comando onde você pode interagir com o sistema.

### Exemplos de Consultas

Experimente estas consultas para testar o sistema:

1. "Quais são as últimas notícias sobre tecnologia?"
2. "Busque informações sobre o clima em São Paulo"
3. "Me dê um resumo sobre inteligência artificial"

## Solução de Problemas

### Verificação da Instalação

Para verificar se o servidor MCP do Brave está instalado corretamente:

```bash
npx @modelcontextprotocol/server-brave-search --help
```

Deveria mostrar as opções disponíveis para o servidor.

### Problemas Comuns

1. **Erro de Conexão com o Servidor MCP**:
   - Verifique se o Node.js está instalado e atualizado
   - Reinstale o pacote MCP: `npm install -g @modelcontextprotocol/server-brave-search`

2. **Erro de Autenticação da API**:
   - Verifique se as chaves de API no arquivo `.env` estão corretas
   - Certifique-se de que a chave do Brave Search está ativa

3. **Erro ao Iniciar o Agente**:
   - Verifique os logs para mensagens de erro específicas
   - Certifique-se de que todas as dependências foram instaladas

## Extendendo o Sistema

Depois que o agente Brave estiver funcionando corretamente, você pode expandir o sistema adicionando outros agentes:

1. Implemente o YouTube, seguindo o padrão do agente Brave
2. Adicione o Reddit
3. Adicione o Supabase

Para cada novo agente, você precisará:

1. Criar os arquivos necessários na pasta correspondente em `agentes/`
2. Instalar o servidor MCP apropriado
3. Atualizar o agente central para incluir o novo agente
4. Configurar as variáveis de ambiente para o novo serviço

## Executando com Claude Code

O Claude Code é uma ferramenta de linha de comando que permite delegar tarefas de codificação ao Claude diretamente do terminal. Para usar o Claude Code com este projeto:

1. Certifique-se de ter o Claude Code instalado e configurado
2. Navegue até o diretório do projeto
3. Use o Claude Code para fazer alterações ou extensões:

```bash
# Exemplo de comando para extender o sistema com o agente YouTube
claude-code "Implemente o agente YouTube seguindo o mesmo padrão do agente Brave"

# Exemplo para resolver problemas
claude-code "Estou recebendo o erro [DESCREVA O ERRO]. Como posso resolver?"

# Exemplo para adicionar novas funcionalidades
claude-code "Adicione suporte para pesquisas de imagens no agente Brave"
```

O Claude Code pode ajudar com:
- Implementação de novos agentes
- Correção de bugs
- Melhorias na interface de usuário
- Adição de novas funcionalidades
