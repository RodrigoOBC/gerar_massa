import pandas as pd

class gerador_lista:

    def __init__(self,df_name, coluna,colunas = 0):

        self.coluna = coluna
        self.colunas = colunas
        self.df_name = df_name

    def manipular_df(self) -> list:
        df = pd.read_csv(self.df_name, sep=",", engine='python')
        df.columns = self.colunas
        df = df[self.coluna]
        df = df.to_list()
        return df

    def manipular_df2(self) -> list:
        df = pd.read_csv(self.df_name, sep=",", engine='python')
        df = df[self.coluna]
        return df.to_list()
