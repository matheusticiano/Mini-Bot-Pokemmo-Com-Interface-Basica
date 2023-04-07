from time import sleep
import pyautogui

# Define algumas constantes que serão usadas ao longo do programa
X_SETA = 1363
Y_SETA = 196
REGIAO_SETA = (1341, 176, 43, 40)   # Região que a seta da mensagem aparece
contador = 1  # Numeros de pps do ataque do seu pokemon


def pesca():  # Função que simula o ato de pescar
    pyautogui.press('3')
    sleep(4)


def checa_seta():  # Função que verifica se a seta está visível e clica nela para mudar de área
    while True:
        seta_loc = pyautogui.locateOnScreen('pokemmo/files/seta.PNG', region=REGIAO_SETA, confidence=0.6)
        if seta_loc is not None:
            pyautogui.click(seta_loc.left + seta_loc.width/2, seta_loc.top + seta_loc.height/2)
            sleep(2)
        else:
            break


def atack():  # Função que simula o ataque do personagem
        pyautogui.press('E')
        pyautogui.press('S')
        pyautogui.press('E')


def checa_pokemon_e_contador():  # Função que verifica a presença de um pokemon e atualiza o contador em função disso
    global contador
    while True:
        poke1_loc = pyautogui.locateOnScreen('pokemmo/files/poke_1.PNG', region=(0, 890, 429, 156), confidence=0.8)
        poke2_loc = pyautogui.locateOnScreen('pokemmo/files/poke_2.PNG', region=(0, 890, 429, 156), confidence=0.8)
        poke3_loc = pyautogui.locateOnScreen('pokemmo/files/poke_3.PNG', region=(0, 890, 429, 156), confidence=0.8)
        if contador == 0:  # Se o contador chegar a zero, o personagem se cura no cp, volta para o local de pesca e reseta o contador
            voltar_spot()
            contador += 32
        elif poke1_loc is not None:  # Se encontrar um pokemon, ataca e decrementa o contador
            atack()
            sleep(6)
            contador -= 1
        elif poke2_loc is not None:  # Se encontrar um pokemon, ataca e decrementa o contador
            atack()
            sleep(6)
            contador -= 1
        elif poke3_loc is not None:  # Se encontrar um pokemon, ataca e decrementa o contador
            atack()
            sleep(6)
            contador -= 1
        else:  # Se o contador chegar a zero, volta para o local de pesca e reseta o contador
            break


def voltar_spot():  # Função que simula a ação de se cura no cp e voltar ao local de pesca
    sleep(5)
    pyautogui.press('5')
    sleep(4)
    pyautogui.keyDown('e')
    sleep(8)
    pyautogui.keyUp('e')
    sleep(0.2)
    pyautogui.keyDown('s')
    sleep(3)
    pyautogui.keyUp('s')
    sleep(0.2)
    pyautogui.keyDown('a')
    sleep(0.7)
    pyautogui.keyUp('a')
    sleep(0.2)
    pyautogui.press('1')
    sleep(0.2)
    pyautogui.keyDown('w')
    sleep(3)
    pyautogui.keyUp('w')
    sleep(0.2)
    pyautogui.keyDown('d')
    sleep(0.3)
    pyautogui.keyUp('d')
    sleep(0.2)
    pyautogui.keyDown('w')
    sleep(2)
    pyautogui.keyUp('w')
    sleep(0.2)
    pyautogui.keyDown('a')
    sleep(0.2)
    pyautogui.keyUp('a')
    sleep(0.2)
    pyautogui.keyDown('w')
    sleep(2.4)
    pyautogui.keyUp('w')
    sleep(0.2)
    pyautogui.keyDown('d')
    sleep(0.1)
    pyautogui.keyUp('d')
