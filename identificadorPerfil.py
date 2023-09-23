import os
import openai
import dotenv
import tiktoken

enconder = tiktoken.encoding_for_model("gpt-3.5-turbo")



def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("./data/dados10.csv")

lista_de_tokens = enconder.encode(prompt_sistema + prompt_usuario)
numero_de_tokens = len(lista_de_tokens)
print(f"numero de Tokens {numero_de_tokens}")
custo = (numero_de_tokens / 1000) * 0.0015
print(f"Custo de antrada{custo}")

tamanho_esperado_saida = 2048
modeloGPT = "gpt-3.5-turbo"
if numero_de_tokens >= 4096 - tamanho_esperado_saida:
    modeloGPT = "gpt-3.5-turbo-16k"

print(f"Modelo GPT escolhido {modeloGPT}")

resposta = openai.ChatCompletion.create(
  model = modeloGPT,
  messages=[
    {
      "role": "system",
      "content": prompt_sistema
    },
    {
      "role": "user",
      "content": prompt_usuario
    }
  ],
  temperature=1,
  max_tokens=tamanho_esperado_saida,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(resposta.choices[0].message.content)
