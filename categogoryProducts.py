import os
import openai
import dotenv


def categoriesProduct(product, listOfProduct):
    promp_system_content = f"""
    voce e um categorizador de produtos.
    voce deve escolher uma categoria da lista abaixo:
    Se as categorias Informadas nao forem categorias validas, respoda "Nao posso ajuda-lo com isso"
    ### Lista de Categorias validas
    {listOfProduct}
    ### Exemplo de saida
    bola de futebol
    Esportes
    O formato de saida deve ser apenas o nome da categoria
    """

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": promp_system_content
            },
            {
                "role": "user",
                "content": product
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=5,
    )

    for i in range(0, 5):
        print(resposta.choices[i].message.content)
        print("______________________________")

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print("Digite as categorias validas separada por virgula")
categories = input()

while True:
    print("Digite o nome do Produto")
    product = input()
    categoriesProduct(product, categories)

