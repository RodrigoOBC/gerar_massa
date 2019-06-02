import pandas as pd
import numpy as np
import random as rd
import openpyxl
from pip._vendor.msgpack.fallback import xrange
from tratar_df import gerador_lista
from gerador_aleatorio import gerador

def cpf_funcional():
    n = [rd.randrange(10) for i in xrange(9)]

    # calcula digito 1 e acrescenta ao numero
    s = sum(x * y for x, y in zip(n, range(10, 1, -1)))
    d1 = 11 - s % 11
    if d1 >= 10:
        d1 = 0
    n.append(d1)

    # calcula digito 2 e acrescenta ao numero
    s = sum(x * y for x, y in zip(n, range(11, 1, -1)))
    d2 = 11 - s % 11
    if d2 >= 10:
        d2 = 0
    n.append(d2)


    return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)

if __name__ == '__main__':
    print("digite a quantidade da massa desejada")
    vezes = int(input())
    vetor = []
    x = 0
    data = []
    df_nome = gerador_lista(df_name=r"TB_Nomes.csv",coluna='nome',colunas=['index','nome','sexo']).manipular_df()
    df_sobrenome = gerador_lista(df_name=r"sobrenome.csv",coluna='sobrenomes').manipular_df2()
    df_email = gerador_lista(df_name=r"email.csv",coluna='email').manipular_df2()
    for i in range(0,vezes):
        nome = rd.choice(df_nome)
        sobrenome = rd.choice(df_sobrenome)
        email = rd.choice(df_email)
        email = f"{nome}{sobrenome}{email}".replace(" ","")
        vetor.append(nome + sobrenome)
        vetor.append(gerador().cpf_funcional())
        vetor.append(email)
        data.append(vetor)
        vetor = []

    df = pd.DataFrame(data, columns=["Nome","cpf","email"])
    writer = pd.ExcelWriter('massa.xlsx')
    df.to_excel(writer, sheet_name='Sheet_name_1', index=None)
    writer.save()

    print("terminou")
    