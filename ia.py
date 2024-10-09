import openai

chave_api = "SUA-CHAVE"

openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):

    lista_mensagens.append(
        {"eole":"user", "content": mensagem}
    )

    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens,
    )
    return resposta.choices[0].message.content

lista_mensagens = []
while True:
    texto = input("Digite aqui: ")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append({"role": "user", "content": resposta})
        print("sono", resposta)