import pyautogui
import time
import subprocess
import webbrowser

# Número de destino e mensagem
numero_destino = "+5545991440524"  # Substitua pelo número de destino
mensagem = "Eu te amo!"  # Mensagem a ser enviada
numero_de_mensagens = 50  # Quantidade de mensagens a serem enviadas

# Abrir o WhatsApp Web no navegador
webbrowser.open(f"https://web.whatsapp.com/send?phone={numero_destino}&text={mensagem}")

# Aguardar o WhatsApp Web carregar e a tela estar pronta
time.sleep(15)  # Aguarde um tempo adequado para o WhatsApp Web carregar (ajuste conforme necessário)

# Enviar a mensagem várias vezes
for i in range(numero_de_mensagens):
    # 3. Escrever a mensagem
    pyautogui.write(mensagem)  # Digita a mensagem
    pyautogui.press('enter')  # Envia a mensagem
    print(f"Mensagem {i+1} enviada!")  # Feedback visual

    time.sleep(2)  # Espera 2 segundos antes de enviar a próxima mensagem

print(f"{numero_de_mensagens} mensagens enviadas!")
