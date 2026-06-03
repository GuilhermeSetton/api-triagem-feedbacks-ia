# 🚗 Triagem Inteligente de Feedbacks com IA

Este projeto é uma API desenvolvida em Python (FastAPI) que utiliza Inteligência Artificial (Google Gemini) para automatizar a triagem e categorização de feedbacks de passageiros em aplicativos de mobilidade.

Foi construído com o objetivo de demonstrar habilidades em Automação, Integração de Sistemas e IA.

## 🎯 O Problema vs. A Solução
Plataformas de mobilidade processam milhões de corridas. Ler e categorizar comentários de passageiros manualmente é um gargalo operacional. 

**A Solução:** Uma API que atua como o "cérebro" de uma automação. Ela recebe o feedback, interpreta o sentimento e o contexto usando IA, e devolve uma ação estruturada.

### 🔄 Pipeline de Automação (Low-Code / No-Code)
Esta API foi desenhada para ser conectada a plataformas como **Make.com** ou **n8n**:
1. **Trigger:** Passageiro avalia a corrida (ex: Typeform, App, Banco de Dados).
2. **Webhook:** A plataforma no-code envia os dados para esta API.
3. **Processamento (IA):** O Google Gemini analisa o texto e categoriza como:
   - 🚨 `Crítico` (Segurança, direção perigosa)
   - 💡 `Sugestão` (Melhorias no app)
   - ⭐ `Elogio` (Feedback positivo)
   - 💬 `Neutro` (Comentários genéricos)
4. **Action:** A plataforma no-code recebe o JSON de volta e executa ações automáticas (Ex: Se for "Crítico", abre um ticket urgente no Jira e alerta a equipe no Slack).

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **FastAPI** (Criação do endpoint REST de alta performance)
- **Uvicorn** (Servidor ASGI)
- **Google Generative AI (Gemini 3.5 Flash)** (LLM para análise de linguagem natural)
- **python-dotenv** (Gerenciamento seguro de credenciais)

## 🚀 Como rodar o projeto localmente

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio