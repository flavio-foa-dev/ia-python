# ia-python
IA | Python

### Criação e utilização de um ambiente virtual
  python3 -m venv .venv
  pip freeze > requirements.txt

  Ative o ambiente virtual criado do diretório .venv
  source .venv/bin/activate


  pip install openai



- Ajustar os parâmetros do Playground como temperatura e comprimento máximo para controlar a criatividade e a saída do GPT, visando gerar respostas mais coerentes e adaptadas aos contextos desejados.
- Utilizar a biblioteca da OpenAI para fazer requisições à API e gerar respostas de um modelo GPT-3.5, - aprendendo a passar mensagens de sistema e usuário, assim como proteger a chave da API para garantir segurança.
- Esconder chaves de identificação em variáveis de ambiente para proteger informações sensíveis ao fazer integrações de API.

Utilizar a API do GPT-3 para categorizar produtos em um contexto de e-commerce, ajustando parâmetros para obter várias respostas e explorando a documentação da API para entender seu funcionamento e as opções disponíveis.
Aprimorar o prompt do sistema para direcionar as respostas do modelo GPT com estratégias como especificar o formato de saída desejado e fornecer exemplos para guiar as respostas.
Criar uma função de categorização de produtos, utilizando um prompt template para inserir dinamicamente parâmetros como categorias válidas e nome do produto, permitindo uma interação mais flexível e organizada com o código.