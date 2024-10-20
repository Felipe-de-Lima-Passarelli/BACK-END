#Um simples chat on-line com o uso da biblioteca flet do Python

import flet as ft

def main(pagina):

    def enviar_mensagem_tunel(mensagem): #Criar o chat para todas as pessoas
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) #Ativar o chat para todas as pessoas

    def enviar_mensagem(evento): #Enviar a mensagem para o chat global
        mensagem = f"{conteudo_popup.value}: {caixa_chat.value}"
        pagina.pubsub.send_all(mensagem)
        caixa_chat.value = ""
        pagina.update()

    caixa_chat = ft.TextField(label = "Digite sua mensagem", on_submit = enviar_mensagem)
    botao_chat = ft.ElevatedButton("Enviar", on_click = enviar_mensagem)
    chat = ft.Column()

    def fechar_popup(evento): #Fechar o popup
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(chat)
        linha_enviar = ft.Row([caixa_chat, botao_chat])
        pagina.add(linha_enviar)
        mensagem = f"{conteudo_popup.value} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    conteudo_popup = ft.TextField(label = "Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click = fechar_popup)
    popup = ft.AlertDialog(open= False, modal= True, title= titulo_popup, content= conteudo_popup, actions=[botao_popup])

    def abrir_popup(evento): #Abrir o popup
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    titulo = ft.Text("Hashzap")
    botao = ft.ElevatedButton("Iniciar Chat", on_click = abrir_popup)

    pagina.add(titulo)
    pagina.add(botao)

ft.app(main, view=ft.AppView.WEB_BROWSER) #Iniciar o aplicativo no navegador com o parâmetro view
