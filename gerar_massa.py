import pandas as pd
import numpy as np
import random as rd
import openpyxl
from pip._vendor.msgpack.fallback import xrange


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
    input()
    vetor = []
    x = 0
    data = []
    df_nome = pd.read_csv("TB_Nomes.csv", sep=",", engine='python')
    df_nome.columns = ["Index", "Nomes", "sexo"]
    df_nome = df_nome["Nomes"]
    df_nome = df_nome.to_list()
    df_sobrenome = pd.read_csv("sobrenome.csv", sep=",", engine='python')
    df_sobrenome = df_sobrenome["sobrenomes"]
    df_sobrenome = df_sobrenome.to_list()
    df_email = pd.read_csv("email.csv", sep=",", engine='python')
    df_email = df_email["email"]
    df_email = df_email.to_list()
    for i in range(0,vezes):
        nome = rd.choice(df_nome)
        sobrenome = rd.choice(df_sobrenome)
        email = rd.choice(df_email)
        email = f"{nome}{sobrenome}{email}".replace(" ","")
        vetor.append(nome + sobrenome)
        vetor.append(cpf_funcional())
        vetor.append(email)
        data.append(vetor)
        vetor = []

    df = pd.DataFrame(data, columns=["Nome","cpf","email"])
    writer = pd.ExcelWriter('massa.xlsx')
    df.to_excel(writer, sheet_name='Sheet_name_1', index=None)
    writer.save()

    print("terminou")