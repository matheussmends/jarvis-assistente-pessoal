# JARVIS - Assistente Pessoal

Projeto open-source de assistente pessoal com integração com a Alexa (Alexa-hosted skill) e respostas inteligentes via IA.

## Estrutura

- `alexa_skill/` → Lógica usada diretamente no Alexa Developer Console.
- `app/` → Estrutura de backend local (FastAPI) para testes e futuras integrações.

## Como rodar localmente

```bash
uvicorn app.routes.handler:router --reload
