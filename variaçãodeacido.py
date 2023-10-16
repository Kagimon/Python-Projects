import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
REVERSE = "\033[m"
lista_x = []
lista_y = []
lista_z = []
massa_entrada_gasosa_fundo = float(input('Insira a vazão de efluente a ser tratado em kg/h: '))
fração_acido_entrada_fundo = float(input('Insira a fração de ácido no efluente: '))
fração_acido_saida_topo = float(input('Insira a fração de acido no efluente tratado: '))
massa_saida_aquosa_fundo = float(input('Insira a vazão de efluente aquoso em kg/h: '))
projeção_vazão = float(input('Insira por quanto tempo quer projetar o processo? '))
medida_utilizada = str(input(f''
                             f'\nInforme a medida utilizada'
                             f'\n{GREEN}[h]{REVERSE} para horas'
                             f'\n{BLUE}[d]{REVERSE} para dias'
                             f'\n{CYAN}[m]{REVERSE} para meses'
                             f'\n{RED}[a]{REVERSE} para anos: ')).lower()
conversão = int(input(f'Manter a medida{CYAN}[1]{REVERSE}'
                      f'\nConverter a medida {GREEN}[2]{REVERSE}: '))
if conversão == 1:
    medida_utilizada = medida_utilizada
elif conversão == 2 and medida_utilizada == "h":
    projeção_vazão = 60 * projeção_vazão
    medida_utilizada = 'min'
elif conversão == 2 and medida_utilizada == 'd':
    medida_utilizada = str(input(f'Converter para horas{RED}(h){REVERSE}'
                               f'\nConverter para minutos{CYAN}(min): ')).lower()
    if medida_utilizada == "h":
        projeção_vazão = projeção_vazão * 24
    else:
        projeção_vazão = projeção_vazão * 1440
elif conversão == 2 and medida_utilizada == 'm':
    medida_utilizada = str(input(f'Converter para dias{RED}[d]{REVERSE}'
                          f'\nConverter para horas{CYAN}[h]')).lower()
    if medida_utilizada == 'd':
        projeção_vazão = projeção_vazão * 30
    else:
        projeção_vazão = projeção_vazão * 24 * 30
else:
    medida_utilizada = str(input(f'Converter para meses {GREEN}[m]{REVERSE}'
                          f'\nConverter para dias {BLUE}[d]')).lower()
    if medida_utilizada == "m":
        projeção_vazão = projeção_vazão * 12
    else:
        projeção_vazão = projeção_vazão * 12 * 30
if medida_utilizada == "min":
    massa_entrada_gasosa_fundo /= 60
    massa_saida_aquosa_fundo /= 60
elif medida_utilizada == "h":
    massa_entrada_gasosa_fundo = massa_entrada_gasosa_fundo
    massa_saida_aquosa_fundo = massa_saida_aquosa_fundo
elif medida_utilizada == "d":
    massa_entrada_gasosa_fundo *= 24
    massa_saida_aquosa_fundo *= 24
elif medida_utilizada == "m":
    massa_entrada_gasosa_fundo *= 24 * 30
    massa_saida_aquosa_fundo *= 24 * 30
else:
    massa_entrada_gasosa_fundo *= 24 * 30 * 12
    massa_saida_aquosa_fundo *= 24 * 30 * 12
count = 0
fração_ar_entrada_fundo = 1 - fração_acido_entrada_fundo
fração_ar_saida_topo = 1 - fração_acido_saida_topo
massa_de_acido_entrada_fundo = fração_acido_entrada_fundo * massa_entrada_gasosa_fundo
massa_de_ar = fração_ar_entrada_fundo * massa_entrada_gasosa_fundo
massa_de_acido_saida_topo = (massa_de_ar * fração_acido_saida_topo) / (fração_ar_saida_topo)
massa_de_acido_saida_fundo = massa_de_acido_entrada_fundo - massa_de_acido_saida_topo
fração_de_acido_saida_fundo = (massa_de_acido_saida_fundo / massa_saida_aquosa_fundo)
fração_de_agua_saida_fundo = 1 - fração_de_acido_saida_fundo
massa_de_agua = fração_de_agua_saida_fundo * massa_saida_aquosa_fundo
massa_de_saida_topo = massa_de_acido_saida_topo + massa_de_ar
eixo_x = int(input(f""
                   f"\n{REVERSE}Qual o eixo x do gráfico?"
                     f"\n{RED}[1]{REVERSE} Vazão de entrada do efluente gasoso"
                     f"\n{GREEN}[2]{REVERSE} Vazão de entrada de água pura"
                     f"\n{CYAN}[3]{REVERSE} Vazão de saida de gás tratado"
                     f"\n{BLUE}[4]{REVERSE} Vazão de saida de efluente aquoso: "))
if eixo_x == 1:
    massa_x = massa_entrada_gasosa_fundo
    nome_x = 'efluente gasoso'
elif eixo_x == 2:
    massa_x = massa_de_agua
    nome_x = 'água pura'
elif eixo_x == 3:
    massa_x = massa_de_saida_topo
    nome_x = 'gás tratado'
else:
    massa_x = massa_saida_aquosa_fundo
    nome_x = 'efluente aquoso'
eixo_y = int(input("Qual o eixo y do gráfico?"
                     f"\n{RED}[1]{REVERSE} Vazão de entrada do efluente gasoso"
                     f"\n{GREEN}[2]{REVERSE} Vazão de entrada de água pura"
                     f"\n{CYAN}[3]{REVERSE} Vazão de saida de gás tratado"
                     f"\n{BLUE}[4]{REVERSE} Vazão de saida de efluente aquoso: "))
if eixo_y == 1:
    massa_y = massa_entrada_gasosa_fundo
    nome_y = 'efluente gasoso'
elif eixo_y == 2:
    massa_y = massa_de_agua
    nome_y = 'água pura'
elif eixo_y == 3:
    massa_y = massa_de_saida_topo
    nome_y = 'gás tratado'
else:
    massa_y = round.massa_saida_aquosa_fundo
    nome_y = 'efluente aquoso'
eixo_z = int(input("Qual o eixo z do gráfico?"
                     f"\n{RED}[1]{REVERSE} Vazão de entrada do efluente gasoso"
                     f"\n{GREEN}[2]{REVERSE} Vazão de entrada de água pura"
                     f"\n{CYAN}[3]{REVERSE} Vazão de saida de gás tratado"
                     f"\n{BLUE}[4]{REVERSE} Vazão de saida de efluente aquoso: "))
if eixo_z == 1:
    massa_z = massa_entrada_gasosa_fundo
    nome_z = 'efluente gasoso'
elif eixo_z == 2:
    massa_z = massa_de_agua
    nome_z = 'água pura'
elif eixo_z == 3:
    massa_z = massa_de_saida_topo
    nome_z = 'gás tratado'
else:
    massa_z = massa_saida_aquosa_fundo
    nome_z = 'efluente aquoso'
while True:
    count += 1
    massa_x_convertida = count * massa_x
    if 1e+3 <= massa_x_convertida:
        massa_x_convertida = np.format_float_scientific(round(massa_x_convertida,2), precision=2, exp_digits=1)
    else:
        massa_x_convertida = massa_x_convertida
    massa_y_convertida = count * massa_y
    if 1e+3 <= massa_y_convertida:
        massa_y_convertida = np.format_float_scientific(round(massa_y_convertida,2), precision=2, exp_digits=1)
    else:
        massa_y_convertida = massa_y_convertida
    massa_z_convertida = massa_z * count
    if massa_z_convertida >= 1e+3:
        massa_z_convertida = np.format_float_scientific(round(massa_z_convertida,2), precision=2, exp_digits=1)
    else:
        massa_z_convertida = massa_z_convertida
    lista_x.append(massa_x_convertida)
    lista_y.append(massa_y_convertida)
    lista_z.append(massa_z_convertida)
    if count == projeção_vazão:
        break
tabela ={f'Vazão de {nome_x} kg/{medida_utilizada}':lista_x,
         f'Vazão de {nome_y} kg/{medida_utilizada}':lista_y,
         f'Vazão de {nome_z} kg/{medida_utilizada}':lista_z}
pd.set_option('display.max_rows', 22000)
pd.set_option('display.max_columns', 3)
pd.set_option('display.expand_frame_repr', False)
df = pd.DataFrame(tabela)
lista_x= [float(i) for i in lista_x]
lista_y= [float(i) for i in lista_y]
lista_z= [float(i) for i in lista_z]
print(df)
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(lista_x, lista_y, lista_z, 'red')
ax.set_xlabel(f'Vazão de {nome_x} em kg/{medida_utilizada}', fontsize=15)
ax.set_ylabel(f'Vazão de {nome_y} em kg/{medida_utilizada}', fontsize=15)
ax.set_zlabel(f'Vazão de {nome_z} em kg/{medida_utilizada}', fontsize=15)
ax.scatter3D(lista_x, lista_y, lista_z, c=(lista_z), cmap='cividis')
plt.show()

