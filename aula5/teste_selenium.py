import os
from openpyxl import Workbook

# Obtém automaticamente o diretório da área de trabalho do usuário
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
nome_arquivo = os.path.join(desktop, "meu_arquivo_teste.xlsx")

# Cria uma nova planilha
wb = Workbook()
ws = wb.active
ws.title = "Planilha Aula"

# Salva o arquivo Excel no desktop do usuário
wb.save(filename=nome_arquivo)
wb.close()  # Fecha a planilha

print(f"Arquivo salvo em: {nome_arquivo}")
