import rpa as r
import pyautogui as p
import pandas as pd
import os

r.init(visual_automation=True, chrome_browser=True)

r.url('https://br.advfn.com/ferramentas-de-investimento/monitor')
p.sleep(3)
janela = p.getActiveWindow()
janela.maximize()
p.sleep(2)
# Aqui, use seu login do site(faca o cadastro no site)
r.type('//*[@id="afnmainbodid"]/div[1]/div[2]/div[2]/div/form/div[2]/input', 'Usuariologin')
p.sleep(3)
# Aqui, use sua senha do site
r.type('//*[@id="password-input"]', 'usuario123[enter]')
p.sleep(5)
r.click('//*[@id="monitor-selector"]/div/ul/li[2]/button')
p.sleep(3)
p.click(x=76, y=287)
p.sleep(7)

r.table('//*[@id="monitorApp_monGrid_grid_table"]', 'cotacoes.csv')
dados = pd.read_csv('cotacoes.csv')
dados.to_csv(r'bolsa.csv', mode='a', index=None, header=True)
csv_xlsx = pd.read_csv(r'bolsa.csv')
csv_xlsx.to_excel(r'bolsa.xlsx')
p.sleep(4)
r.close()

os.startfile(r'C:\RPA\bolsa.xlsx')