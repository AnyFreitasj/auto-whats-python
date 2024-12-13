# auto-whats-python
Projeto de Automação para Envio de Mensagens no WhatsApp Web
Este projeto tem como objetivo automatizar o envio de mensagens para um número de telefone específico através do WhatsApp Web, utilizando Python e a biblioteca pyautogui para simular interações com a interface gráfica.

Funcionalidades
Envio Automático de Mensagens: Envia uma mensagem personalizada para um número de telefone especificado.
Número de Mensagens Personalizável: Permite enviar um número configurável de mensagens consecutivas.
Integração com WhatsApp Web: Abre o WhatsApp Web no navegador e envia as mensagens automaticamente, interagindo com a interface do WhatsApp Web como um usuário real.
Controle de Tempo: Utiliza intervalos entre o envio das mensagens para simular um comportamento humano e evitar bloqueios ou interrupções.

Como Funciona
O código abre o WhatsApp Web no navegador, redirecionando para o número de destino e iniciando a conversa.
Após o carregamento da página, o script utiliza a biblioteca pyautogui para simular a digitação da mensagem e o envio repetido.
O número de mensagens a serem enviadas pode ser facilmente configurado pelo usuário.
A automação é feita de forma simples e eficaz, com intervalos entre cada envio para garantir um comportamento mais natural.

Tecnologias Utilizadas
Python: Linguagem de programação utilizada para a automação.
pyautogui: Biblioteca para automação de GUI, usada para simular a digitação e pressionamento de teclas.
webbrowser: Para abrir o WhatsApp Web no navegador.

Requisitos
Python 3.x
Bibliotecas: pyautogui, time, webbrowser
WhatsApp Web autenticado no navegador (QR Code já escaneado).
