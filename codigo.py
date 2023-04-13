from time import sleep
import pyautogui


# dando entrada na imagem
recusar = r"E:\Repos-Github\Auto-Accept-Lol\recusar.png"
partida_aceita = r"E:\Repos-Github\Auto-Accept-Lol\xd2.png"

result = False

# procurando as imgs
while result == False:
    contagem = 0
    contador = 0
    print('Iniciando...')
    while not pyautogui.locateCenterOnScreen(recusar):
        contagem += 1
        print(f'Procurando partida {contagem}')
        sleep(2)
    # clicar em aceitar partida
    pyautogui.click(1027, 717, duration=0.2)
    result = True
    sleep(5)
    # procurando a imagem partida aceita
    while not pyautogui.locateOnScreen(partida_aceita, confidence=0.7):
        sleep(3)
        contador += 1
        print(f'Esperando entrar no lobby {contador}')
        if contador == 6:
            result = False
            break

# printar que aceitou partida
print('Partida aceita')
