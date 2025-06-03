import whisper
from langchain.llms import Ollama

whisper_model = whisper.load_model("base") 

print("————  Transcrevendo áudio  ————")
result = whisper_model.transcribe("audio.mp3")
texto_transcrito = result["text"]
print("\n————  Texto transcrito:  ————\n")
print(texto_transcrito)

llm = Ollama(model="llama2")

prompt = f"""
Resuma o seguinte texto em tópicos com os principais pontos-chave. Seja conciso e direto.

Texto:
{texto_transcrito}

Resposta:
"""

resumo = llm.invoke(prompt)

print("\n————  Pontos-chave:  ————\n")
print(resumo)
