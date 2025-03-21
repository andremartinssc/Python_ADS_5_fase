import pyautogui
import time
import subprocess
import keyboard  # Biblioteca para melhorar a entrada de texto

# Passo 1: Abrir o Bloco de Notas
subprocess.Popen(['notepad.exe'])

# Passo 2: Esperar o Bloco de Notas abrir
time.sleep(2)

# pyautogui.write('Meu robo está vivo e está fazendo análises de dados', interval=0.1)
# Passo 3: Digitar a mensagem (usando keyboard para evitar problemas com acentos)
keyboard.write('Meu robo está vivo e está fazendo análises de dados', delay=0.1)  # Escreve a mensagem com acentos corretamente

# Passo 4: Aguardar 5 segundos para visualizar
time.sleep(5)

# Passo 5: Fechar o Bloco de Notas
pyautogui.hotkey("alt", "f4")

# Passo 6: Confirmar para não salvar, se necessário
time.sleep(1)
pyautogui.press("left")
pyautogui.press("enter")
