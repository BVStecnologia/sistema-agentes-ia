# Agente Brave Search

Este agente especializado se integra com a API do Brave Search para realizar buscas na web e fornecer informações atualizadas em resposta às consultas dos usuários.

## Funcionalidades

- **Pesquisas na Web**: Realiza buscas na internet usando o Brave Search
- **Filtragem Inteligente**: Analisa e filtra os resultados mais relevantes
- **Formatação de Respostas**: Estrutura as informações de maneira clara e compreensível

## Ferramentas Disponíveis

O agente utiliza ferramentas fornecidas pelo servidor MCP do Brave Search:

- `brave_web_search`: Para pesquisas gerais na web
- `brave_local_search`: Para buscar informações sobre locais e estabelecimentos

## Configuração

Para utilizar este agente, é necessário:

1. Obter uma chave de API do Brave Search
2. Configurar a variável de ambiente `BRAVE_API_KEY`
3. Instalar o pacote MCP: `npm install -g @modelcontextprotocol/server-brave-search`

## Uso

O agente Brave é projetado para funcionar tanto de forma independente quanto integrado com o agente central.

### Exemplo de Consultas

- "Quais são as notícias mais recentes sobre inteligência artificial?"
- "Busque informações sobre o clima em São Paulo hoje"
- "Encontre restaurantes italianos próximos ao Central Park"
