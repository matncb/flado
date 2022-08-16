
import importlib
import aleatorio
import xlsxwriter

N = 100
resultados = []

for i in range(N):
    importlib.reload(aleatorio)
    resultados.append(aleatorio.pegar())

workbook = xlsxwriter.Workbook('dist1_5.xlsx')
worksheet = workbook.add_worksheet()

for i in range(len(resultados)):
    worksheet.write(i, 0, resultados[i])

workbook.close()
