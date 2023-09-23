import tiktoken

enconder = tiktoken.encoding_for_model("gpt-3.5-turbo")

lista_de_tokens = enconder.encode("voce e um rapaz de bits")
print(lista_de_tokens)
print(len(lista_de_tokens))
custo = (len(lista_de_tokens)/1000) * 0.0015
print(f"Custo de antrada{custo}")