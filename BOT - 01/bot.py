import pyautogui
import time

pyautogui.alert('Bot iniciado!')

pyautogui.PAUSE = 0.5

#inicio

pyautogui.hotkey('win','1')

#inicio do for

for c in range(0,3):

    pyautogui.press('tab')
    pyautogui.press('enter')

#ir para a planilha

    pyautogui.hotkey('win','3')
    pyautogui.press('esc')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','c')

#buscar o agente

    pyautogui.hotkey('win','1')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('esc')


#ir para aba finan.

    pyautogui.click(x=578, y=174)

#voltar para a planilha

    pyautogui.hotkey('win','3')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl','c')

#procurar a nf

    pyautogui.hotkey('win','1')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')

#baixar

    pyautogui.click(x=1309, y=360)
    time.sleep(0.5) 
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('alt','f4')
    time.sleep(1)
    pyautogui.click(x=443, y=95)

#rest / final do for

    print('+1 salvo')