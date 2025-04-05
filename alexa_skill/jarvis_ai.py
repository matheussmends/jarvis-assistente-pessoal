from transformers import pipeline

# Carrega o modelo local para resposta de texto
chatbot = pipeline("text-generation", model="distilgpt2")

def ask_jarvis(pergunta: str) -> str:
    try:
        resposta = chatbot(pergunta, max_length=100, do_sample=True, temperature=0.7)
        return resposta[0]["generated_text"].strip()
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        return "Desculpe, algo deu errado ao tentar responder, Senhor."
