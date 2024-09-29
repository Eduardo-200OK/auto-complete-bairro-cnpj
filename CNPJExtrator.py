import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from time import sleep

dic_cnpj_bairro = {}
lista_bairro = []

class CNPJExtrator:

    def __init__(self, file_path, column, output):
        self.column = int(column)  # Converter para inteiro
        self.file_path = file_path
        self.output = output

    def execute(self):
        print(self.file_path)
        df = pd.read_excel(self.file_path)
        print(df)

        # Usar o índice da coluna que foi passado
        coluna_d = df.iloc[:, self.column]

        # Remover caracteres indesejados
        lista_cnpj = [str(cnpj).replace('.', '').replace('-', '').replace('/', '').replace(' ', '') for cnpj in coluna_d]

        print(lista_cnpj)

        def consultar_cnpj(cnpjs):
            url = f'https://api.invertexto.com/v1/cnpj/{cnpjs}?token=661|xqfbRfFda6qReBvlbBRhuX3hFw6DdQ1f'
            print(f"URL:[{url}]")

            response = requests.get(url, timeout=5)
            print(f"Status Code: [{response.status_code}]")

            if response.status_code == 200:
                data = json.loads(response.text)
                bairro = data['endereco']['bairro']
                print(f"BAIRRO: [{bairro}] CNPJ:[{cnpjs}]\n")
                lista_bairro.append(bairro)
                sleep(4)
                return bairro

            else:
                bairro = "INEXISTENTE"
                print(f"{bairro} CNPJ:[{cnpjs}]")
                lista_bairro.append(bairro)
                sleep(4)
                return bairro
        
        def processar_cnpj():
            for count, cnpj in enumerate(lista_cnpj, start=1):
                print(f"Contagem: {count}")
                consultar_cnpj(cnpj)

        processar_cnpj()
        
        # Salvar o DataFrame no arquivo de saída especificado
        df_resultado = pd.DataFrame({
            'CNPJ': lista_cnpj,
            'Bairro': lista_bairro
        })
        df_resultado.to_excel(self.output, index=False)  # Especificar o caminho completo para o arquivo de saída
