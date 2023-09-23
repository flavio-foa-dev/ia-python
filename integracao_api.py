import openai
import dotenv
import os
dotenv.load_dotenv()

openai.organization = os.getenv('OPENAI_ORGANIZATION')
openai.api_key =  os.getenv("OPENAI_API_KEY")
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "system",
            "content": "Gere nomes de constantes em python"
        },
        {
            "role": "user",
            "content": "Gere 5 funcaoes"
        }
    ]
)

print(response)