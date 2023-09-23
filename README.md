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