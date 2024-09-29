import CNPJextrator as ce
import argparse

def main():

    paser = argparse.ArgumentParser(description="CPNJ para bairro")

    paser.add_argument("file_path", type=str, help="Caminho da pasta para o xlsx. Ex: /home/docs/planilha1.xlsx")
    paser.add_argument("output", type=str, help="Caminho de saida. Ex: /home/docs/saida1.xlsx")
    paser.add_argument("column", type=str, help="Posicao da coluna em que se encontra o CNPJ. Ex: 3")

    args = paser.parse_args()

    file_path = args.file_path
    output = args.output
    column = args.column

    CNPJextrator = ce.CNPJExtrator(output=output, file_path=file_path, column=column)
    CNPJextrator.execute()

if __name__ == '__main__':
    main()
