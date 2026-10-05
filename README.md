# API de triagem de feedbacks com IA

API em Python (FastAPI) que recebe a avaliação de um passageiro de aplicativo de mobilidade e usa o Gemini para classificá-la em uma categoria e sugerir uma ação.

## O que faz

Recebe nome do passageiro, nota, comentário e id da corrida. Devolve um JSON com:

- `categoria`: `Crítico` (segurança, direção perigosa, assédio), `Sugestão`, `Elogio` ou `Neutro`
- `acao_recomendada`: texto curto com o próximo passo

Foi pensada para ser chamada por webhook a partir de ferramentas de automação como n8n ou Make: a ferramenta envia o feedback, recebe o JSON e decide o que fazer (por exemplo, abrir um chamado quando a categoria é `Crítico`).

## Como rodar

Requer Python 3.10 ou mais novo e uma chave da API do Gemini.

```bash
git clone https://github.com/GuilhermeSetton/api-triagem-feedbacks-ia.git
cd api-triagem-feedbacks-ia
python -m venv venv
source venv/bin/activate        # no Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # depois edite o .env e coloque a sua chave
uvicorn main:app --reload
```

A API sobe em `http://127.0.0.1:8000`. A documentação interativa fica em `http://127.0.0.1:8000/docs`.

## Exemplo

Requisição:

```bash
curl -X POST http://127.0.0.1:8000/webhook/feedback \
  -H "Content-Type: application/json" \
  -d '{"passenger_name": "Ana", "rating": 1, "comment": "O motorista avançou dois sinais vermelhos.", "ride_id": "R-1024"}'
```

Formato da resposta (os dois textos de `analise` são gerados pelo modelo):

```json
{
  "status": "sucesso",
  "passageiro": "Ana",
  "analise": {
    "categoria": "...",
    "acao_recomendada": "..."
  }
}
```

## Tecnologias

- FastAPI e Uvicorn
- Pydantic, para validar a entrada
- Google Generative AI (Gemini)
- python-dotenv, para ler a chave da API do arquivo `.env`

## Limitações

- Não tem testes automatizados.
- Não mede a taxa de acerto da classificação.
- Quando a chamada ao Gemini falha, a API devolve `{"status": "erro"}` com código HTTP 200.
