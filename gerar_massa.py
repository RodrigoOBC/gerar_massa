import pandas as pd
import numpy as np
import random as rd
import openpyxl
from pip._vendor.msgpack.fallback import xrange
from tratar_df import gerador_lista
from gerador_aleatorio import gerador

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
        vetor.append(gerador().cpf_funcional(True))
        vetor.append(email)
        data.append(vetor)
        vetor = []
    df = pd.DataFrame(data, columns=["Nome","cpf","email"])
    writer = pd.ExcelWriter('massa.xlsx')
    df.to_excel(writer, sheet_name='Sheet_name_1', index=None)
    writer.save()

    print("terminou")
