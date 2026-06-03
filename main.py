from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

app = FastAPI()

# Puxa a chave de forma segura do ambiente
CHAVE_GEMINI = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=CHAVE_GEMINI)

# Usamos o modelo flash, que é super rápido e gratuito
model = genai.GenerativeModel('models/gemini-3.5-flash')

class Feedback(BaseModel):
    passenger_name: str
    rating: int
    comment: str
    ride_id: str

@app.post("/webhook/feedback")
async def receber_feedback(feedback: Feedback):
    # Instruções para o Gemini
    prompt = f"""
    Você é um assistente de triagem de corridas de aplicativo de mobilidade.
    Analise a nota e o comentário do passageiro e classifique em uma destas categorias:
    - Crítico (problemas de segurança, direção perigosa, assédio)
    - Sugestão (ideias de melhoria no app ou serviço)
    - Elogio (feedback positivo)
    - Neutro (reclamações leves como atraso pequeno ou comentários genéricos)

    Nota do passageiro: {feedback.rating} estrelas.
    Comentário do passageiro: "{feedback.comment}"

    Responda APENAS em formato JSON válido com as chaves:
    "categoria" (string) e "acao_recomendada" (string). Não adicione nenhuma formatação extra ou crases.
    """

    try:
        # Chama a IA do Google
        resposta = model.generate_content(prompt)
        
        # Limpa o texto caso a IA devolva com formatação markdown
        texto_limpo = resposta.text.replace("```json", "").replace("```", "").strip()
        
        # Converte o texto em um dicionário Python
        analise_ia = json.loads(texto_limpo)
        
        return {
            "status": "sucesso",
            "passageiro": feedback.passenger_name,
            "analise": analise_ia
        }
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}