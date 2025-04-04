# Agente Central

Este é o agente coordenador principal do sistema. Ele recebe consultas do usuário, analisa o conteúdo e decide qual(is) agente(s) especializado(s) acionar para resolver a tarefa.

## Funcionalidades

- Análise de consultas do usuário
- Decisão sobre qual agente especializado utilizar
- Coordenação de respostas de múltiplos agentes
- Apresentação de resultados de forma coerente

## Ferramentas Disponíveis

O agente central pode acionar as seguintes ferramentas:

- `use_brave_search` - Para pesquisas na web
- `use_youtube_agent` - Para busca e análise de vídeos
- `use_reddit_agent` - Para informações de comunidades e discussões
- `use_supabase_agent` - Para gerenciamento de dados

## Como Funciona

1. Recebe a consulta do usuário
2. Analisa o conteúdo para determinar a intenção
3. Escolhe o(s) agente(s) especializado(s) apropriado(s)
4. Envia consultas específicas para cada agente
5. Combina as respostas em um formato coerente
6. Apresenta o resultado ao usuário

## Prompt do Sistema

O agente central utiliza o seguinte prompt de sistema:

```
Você é um agente coordenador principal que delega tarefas para agentes 
especializados. Analise a consulta do usuário e escolha o agente mais adequado:

- Use o agente Brave para pesquisas na web e informações gerais
- Use o agente YouTube para buscar ou analisar vídeos
- Use o agente Reddit para informações de comunidades e discussões
- Use o agente Supabase para gerenciar dados e banco de dados

Coordene as respostas e forneça uma resposta clara e útil ao usuário.
Se a consulta exigir a combinação de informações de múltiplos agentes, não hesite em usar
vários agentes para criar uma resposta completa.
```

## Exemplo de Uso

Para uma consulta como: "Quais são os vídeos de programação mais populares no YouTube e o que as pessoas estão dizendo sobre eles no Reddit?"

O agente central:
1. Identifica que precisa de informações do YouTube e do Reddit
2. Chama o agente YouTube para buscar os vídeos populares
3. Chama o agente Reddit para buscar discussões sobre esses vídeos
4. Combina as informações em uma resposta coerente

## Implementação

O agente central é implementado no arquivo `agent.py` utilizando a biblioteca pydantic-ai. A função `create_central_agent()` cria e configura o agente central e todos os agentes especializados necessários.