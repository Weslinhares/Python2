# Lógica de Programação:
#Passo 1 - Ler os dados do arquivo
#Passo 2 - Acessar o site do cadastro dos alunos
#Passo 3 - Cadastrar os alunos do arquivo no site.

import pandas as pd
import pyautogui
import time

#Passos para abrir o navegador
#apertar tecla windows do teclado
#digitar a palavra "Opera"
#apertar a tecla Enter
pyautogui.PAUSE = 0.5 #intervalo que o robô terá de fazer para abrir os comandos

pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("Enter")
time.sleep(1) #entre um enter do chrome e depois de digitar, esperar 1 segundo para digitar o site e entrar
pyautogui.write("https://sauer.pro.br/python/automacao/index.html")
pyautogui.press("Enter")
time.sleep(1)
#mouse
pyautogui.click(x=784, y=603)
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("SimplificaPython")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pd.read_csv("alunos.csv")
time.sleep(3)

for linha in tabela.index:
    pyautogui.click(x=730, y=464)
    nome = tabela.loc[linha, "Nome"]
    pyautogui.write(nome) #str serve para informar que o tipo de campo é string (palavra)
    pyautogui.press("tab")

    email = tabela.loc[linha, "Email"]
    pyautogui.write(email)
    pyautogui.press("tab")

    endereco = tabela.loc[linha, "Endereco"]
    pyautogui.write(endereco)
    pyautogui.press("tab")

    telefone = tabela.loc[linha, "Telefone"]
    pyautogui.write(telefone)
    pyautogui.press("tab")

    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.scroll(5000)